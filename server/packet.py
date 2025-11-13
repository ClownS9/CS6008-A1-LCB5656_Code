from typing import Any, Dict, Optional
from action import Action
from registry import Packet, RegisterAction


@RegisterAction(Action.Accept)
class AcceptPacket(Packet):
    def __init__(self):
        super().__init__(Action.Accept)


@RegisterAction(Action.Decline)
class DeclinePacket(Packet):
    def __init__(self, reason: str):
        super().__init__(Action.Decline, reason)


@RegisterAction(Action.Connected)
class ConnectedPacket(Packet):
    def __init__(self, username: str, password: str):
        super().__init__(Action.Connected, username, password)


@RegisterAction(Action.Disconnected)
class DisconnectedPacket(Packet):
    def __init__(self, uid: int):
        super().__init__(Action.Disconnected, uid)


@RegisterAction(Action.LoginResponse)
class LoginResponsePacket(Packet):
    def __init__(self, success: bool, character_data: list = None, reason: str = ""):
        super().__init__(Action.LoginResponse, success, character_data or [], reason)


@RegisterAction(Action.CharSelect)
class CharSelectPacket(Packet):
    def __init__(self, char_id: int):
        super().__init__(Action.CharSelect, char_id)


@RegisterAction(Action.CharSelectLoadout)
class CharSelectLoadoutPacket(Packet):
    def __init__(
        self,
        success: bool,
        reason: str = "",
        inventory: dict = None,
        hair_name: str = "Bald",
        hair_animation_json: str = "",
        hair_color: str = "#663333",
        skin_color: str = "#FFCC99",
    ):
        super().__init__(
            Action.CharSelectLoadout,
            success,
            reason,
            inventory or {},
            hair_name,
            hair_animation_json,
            hair_color,
            skin_color,
        )


@RegisterAction(Action.Register)
class RegisterPacket(Packet):
    def __init__(self, username: str, password: str, email: str, uid: int):
        super().__init__(Action.Register, username, password, email, uid)


@RegisterAction(Action.Chat)
class ChatPacket(Packet):
    def __init__(self, sender: str, message: str):
        super().__init__(Action.Chat, sender, message)


@RegisterAction(Action.ModelDelta)
class ModelDeltaPacket(Packet):
    def __init__(self, model_data: Dict[str, Any]):
        super().__init__(Action.ModelDelta, model_data)


@RegisterAction(Action.Target)
class TargetPacket(Packet):
    def __init__(self, t_x: float, t_y: float):
        super().__init__(Action.Target, t_x, t_y)


@RegisterAction(Action.InventoryUpdate)
class InventoryUpdatePacket(Packet):
    def __init__(self, items: Dict):
        super().__init__(Action.InventoryUpdate, items)


@RegisterAction(Action.EquipItem)
class EquipItemPacket(Packet):
    def __init__(self, item_id: int):
        super().__init__(Action.EquipItem, item_id)


@RegisterAction(Action.UnequipItem)
class UnequipItemPacket(Packet):
    def __init__(self, item_id: int):
        super().__init__(Action.UnequipItem, item_id)


@RegisterAction(Action.UseItem)
class UseItemPacket(Packet):
    def __init__(self, item_id: int):
        super().__init__(Action.UseItem, item_id)


@RegisterAction(Action.HotbarUpdate)
class HotbarUpdatePacket(Packet):
    def __init__(self, slot_id: int, item_id: Optional[int]):
        super().__init__(Action.HotbarUpdate, slot_id, item_id)


@RegisterAction(Action.NPCInteraction)
class NPCInteractionPacket(Packet):
    def __init__(self, npc_id: int, name: str, dialogue: str):
        super().__init__(Action.NPCInteraction, npc_id, name, dialogue)


@RegisterAction(Action.NPCShopUpdate)
class NPCShopUpdatePacket(Packet):
    def __init__(self, npc_id: int, shop_items: list):
        super().__init__(Action.NPCShopUpdate, npc_id, shop_items)


@RegisterAction(Action.MonsterUpdate)
class MonsterUpdatePacket(Packet):
    def __init__(
        self, mon_id: int, name: str, health: int, attack_power: int, is_boss: bool
    ):
        super().__init__(
            Action.MonsterUpdate, mon_id, name, health, attack_power, is_boss
        )


@RegisterAction(Action.CharCreate)
class CharCreatePacket(Packet):
    def __init__(
        self,
        uid: int,
        name: str,
        emerald: int,
        hair_id: int,
        hair_color: str,
        skin_color: str,
        x_axis: float,
        y_axis: float,
    ):
        super().__init__(
            Action.CharCreate,
            uid,
            name,
            emerald,
            hair_id,
            hair_color,
            skin_color,
            x_axis,
            y_axis,
        )
