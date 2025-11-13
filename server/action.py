import enum


class Action(enum.Enum):
    Accept = enum.auto()
    Decline = enum.auto()
    Connected = enum.auto()
    Disconnected = enum.auto()
    LoginResponse = enum.auto()
    CharSelect = enum.auto()
    CharSelectLoadout = enum.auto()
    Register = enum.auto()
    Chat = enum.auto()
    ModelDelta = enum.auto()
    Target = enum.auto()
    InventoryUpdate = enum.auto()
    EquipItem = enum.auto()
    UnequipItem = enum.auto()
    UseItem = enum.auto()
    HotbarUpdate = enum.auto()
    NPCInteraction = enum.auto()
    NPCShopUpdate = enum.auto()
    MonsterUpdate = enum.auto()
    CharCreate = enum.auto()
