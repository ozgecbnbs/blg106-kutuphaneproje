from datetime import datetime
from typing import List, Optional
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import String, Integer, Text, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app import db

class User(db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(256), nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=func.now())

    # İlişkiler
    incelemeler: Mapped[List["Inceleme"]] = relationship(back_populates="kullanici", cascade="all, delete-orphan")

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

class Kitap(db.Model):
    __tablename__ = 'kitaplar'

    id: Mapped[int] = mapped_column(primary_key=True)
    baslik: Mapped[str] = mapped_column(String(128), nullable=False)
    yazar: Mapped[str] = mapped_column(String(128), nullable=False)
    yayin_yili: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    eklendigi_tarih: Mapped[datetime] = mapped_column(default=func.now())

    # İlişkiler
    incelemeler: Mapped[List["Inceleme"]] = relationship(back_populates="kitap", cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Kitap {self.baslik} - {self.yazar}>'

class Inceleme(db.Model):
    __tablename__ = 'incelemeler'

    id: Mapped[int] = mapped_column(primary_key=True)
    icerik: Mapped[str] = mapped_column(Text, nullable=False)
    puan: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    kitap_id: Mapped[int] = mapped_column(ForeignKey('kitaplar.id'), nullable=False)
    olusturulma_tarihi: Mapped[datetime] = mapped_column(default=func.now())

    # İlişkiler
    kullanici: Mapped["User"] = relationship(back_populates="incelemeler")
    kitap: Mapped["Kitap"] = relationship(back_populates="incelemeler")

    def __repr__(self):
        return f'<Inceleme id={self.id} puan={self.puan} user_id={self.user_id} kitap_id={self.kitap_id}>'
