from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
    ForeignKey,
    Float,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

    character = relationship("Character", back_populates="user", lazy="selectin")


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    uid = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String(50), unique=True, nullable=False)
    emerald = Column(Integer, default=0)
    hair_id = Column(Integer, ForeignKey("hair.id"), nullable=False)
    hair_color = Column(String(20), default="#663333")
    skin_color = Column(String(20), default="#FFCC99")
    x_axis = Column(Float, default=0.0)
    y_axis = Column(Float, default=0.0)

    user = relationship("User", back_populates="character", lazy="joined")
    hair = relationship("Hair", back_populates="character", lazy="joined")
    inventory = relationship("Inventory", back_populates="character", lazy="selectin")


class Hair(Base):
    __tablename__ = "hair"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    animation_json = Column(String(1000))

    character = relationship("Character", back_populates="hair", lazy="selectin")


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    char_id = Column(Integer, ForeignKey("characters.id"))
    item_id = Column(Integer, ForeignKey("items.id"))
    quantity = Column(Integer, default=1)
    slot = Column(String(50), nullable=True)
    hotbar_slot = Column(Integer, nullable=True)  # e.g. 0-5 for hotbar

    character = relationship("Character", back_populates="inventory", lazy="selectin")
    item = relationship("Item", back_populates="inventory_entry", lazy="joined")

    __table_args__ = (
        UniqueConstraint("char_id", "slot", name="uq_char_slot"),
        UniqueConstraint("char_id", "hotbar_slot", name="uq_char_hotbar"),
    )


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    type = Column(
        String(50), nullable=False
    )  # e.g. 'weapon', 'cloak', 'armor', 'consumable', 'useable'
    animation_json = Column(String(1000), nullable=True)
    icon = Column(String(255), nullable=True)
    quantity = Column(Integer, default=1)
    max_stack = Column(Integer, default=1)

    inventory_entry = relationship("Inventory", back_populates="item", lazy="selectin")


class Monster(Base):
    __tablename__ = "monsters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    health = Column(Integer, default=100)
    attack_power = Column(Integer, default=100)
    is_boss = Column(Boolean, default=False)

    drops = relationship("MonsterDrop", back_populates="monster", lazy="selectin")


class MonsterDrop(Base):
    __tablename__ = "monster_drops"

    id = Column(Integer, primary_key=True, index=True)
    monster_id = Column(Integer, ForeignKey("monsters.id"))
    item_id = Column(Integer, ForeignKey("items.id"))
    drop_rate = Column(Float, default=0.1)

    monster = relationship("Monster", back_populates="drops", lazy="joined")
    item = relationship("Item", lazy="joined")

    __table_args__ = (
        UniqueConstraint("monster_id", "item_id", name="uq_monster_item_drop"),
    )


class NPC(Base):
    __tablename__ = "npcs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    dialogue = Column(String(2000), nullable=True)
    has_shop = Column(Boolean)

    shop_items = relationship("ShopItem", back_populates="npc", lazy="selectin")


class NPCShopItem(Base):
    __tablename__ = "npcs_shop_items"

    id = Column(Integer, primary_key=True, index=True)
    npc_id = Column(Integer, ForeignKey("npcs.id"))
    item_id = Column(Integer, ForeignKey("items.id"))
    price = Column(Integer, nullable=False)

    npc = relationship("NPC", back_populates="shop_items", lazy="joined")
    item = relationship("Item", lazy="joined")

    __table_args__ = (UniqueConstraint("npc_id", "item_id", name="uq_npc_item"),)
