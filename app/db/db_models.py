from typing import List

from sqlalchemy.orm import declarative_base, mapped_column, relationship, Mapped
from sqlalchemy import UUID, Column, String, Boolean, ForeignKey, Float, Integer, DateTime
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    user_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username: Mapped[String] = mapped_column(String(50), nullable=False, unique=True)
    email: Mapped[String] = mapped_column(String(128), nullable=False, unique=True)
    password: Mapped[String] = mapped_column(String(128), nullable=False)
    is_active: Mapped[Boolean] =mapped_column(Boolean, default=True)
    token: Mapped[String] = mapped_column(String(256), nullable=True, unique=True)

    user_wallet: Mapped['Wallet'] = relationship(back_populates='owner')
    items: Mapped[List['Item']] = relationship(back_populates='owner')

    def set_password(self, password):
        self.password = f'fake_hash_{password}'


class Wallet(Base):
    __tablename__ = "wallets"
    wallet_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    owner_id: Mapped[UUID] = mapped_column(ForeignKey('users.user_id'))
    owner: Mapped[User] = relationship(back_populates='user_wallet')
    balance: Mapped[Float] = mapped_column(Float, default=0.0)

    owner: Mapped['User'] = relationship(back_populates='user_wallet')

class Item(Base):
    __tablename__ = "items"
    item_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    name: Mapped[String] = mapped_column(String(128), nullable=False, default='Item')
    price: Mapped[Float] = mapped_column(Float, nullable=False, default=99.9)
    quantity: Mapped[Integer] = mapped_column(Integer, nullable=True, default=0)
    owner_id: Mapped[UUID] = mapped_column(ForeignKey('users.user_id'))

    owner: Mapped['User'] = relationship(back_populates='items')
