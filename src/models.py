from flask_sqlalchemy import SQLAlchemy
from typing import List
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "User"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(nullable=False)
    firstname: Mapped[str] = mapped_column(nullable=False, unique=False)
    lastname: Mapped[str] = mapped_column(nullable=False, unique=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=False)
    post: Mapped[List["Post"]] = relationship(back_populates="author")
    comment: Mapped[List["Comment"]]= relationship(back_populates="author")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "user name": self.username,
            "first name": self.firstname,
            "last name": self.lastname,
            # do not serialize the password, its a security breach
        }


class Post(db.Model):
    __tablename__ = "Post"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"))
    author: Mapped["User"] = relationship(back_populates="posts")

    def serialize(self):
        return {
            "ID": self.id,

        }


class Comment(db.Model):
    __tablename__ = "Comment"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    comment_text: Mapped[str] = mapped_column(nullable=False)
    author: Mapped["User"] = relationship(back_populates="comment")
    frompost: Mapped["Post"] = mapped_column(ForeignKey("Post.id"))


    def serialize(self):
        return {
            "Comment": self.comment_text
        }


class Media(db.Model):
    __tablename__ = "Media"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    type: Mapped[int] = mapped_column(unique=False, nullable=False)
    url: Mapped[str] = mapped_column(nullable=False)
    post_id:  Mapped[List["Post"]] = mapped_column(ForeignKey("Post.id"))


    def serialize(self):
        return {
            "url": self.url,

        }


