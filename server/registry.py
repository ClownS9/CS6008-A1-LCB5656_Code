import json
from typing import Any, Dict, Optional, Type

from action import Action


class PacketRegistry:
    _registry = Dict[str, Type["Packet"]] = {}

    @classmethod
    def register(cls, action_name: str, msg_class: Type["Packet"]):
        cls._registry[action_name] = msg_class

    @classmethod
    def get(cls, action_name: str) -> Optional[Type["Packet"]]:
        return cls._registry.get(action_name)


class Packet:
    def __init__(self, action: Action, *payloads: Any):
        self.action = action
        self.payloads = payloads

    def __str__(self) -> str:
        data = {"a": self.action.name}
        data.update({f"p{i}": v for i, v in enumerate(self.payloads)})
        return json.dumps(data, separators=(",", ":"))

    def __bytes__(self) -> bytes:
        return str(self).encode("utf-8")

    @classmethod
    def from_json(cls, json_str: str) -> "Packet":
        try:
            obj = json.loads(json_str)
            action_name = obj.get("a")
            msg_cls = PacketRegistry.get(action_name)

            if not action_name:
                raise ValueError("Action name is missing 'a' field.")

            if not msg_cls:
                raise ValueError(f"No registered msg from action '{action_name}")

            payloads = [
                v
                for k, v in sorted(
                    ((int(k[1:]), v) for k, v in obj.items() if k.startswith("p")),
                    key=lambda x: x[0],
                )
            ]

            return msg_cls(*payloads)
        except (json.JSONDecodeError, ValueError, TypeError) as e:
            raise ValueError(f"Deserialization has failed: {e}") from e


class RegisterAction:
    def __init__(self, action: Action):
        self.action = action

    def __call__(self, cls):
        PacketRegistry.register(self.action.name, cls)
        return cls
