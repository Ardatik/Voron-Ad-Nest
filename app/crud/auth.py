import uuid
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.user import User


def get_user_by_id(db: Session, user_id: uuid.UUID) -> User | None:
    stmt = select(User).where(User.id == user_id)
    result = db.execute(stmt).scalar_one_or_none()
    return result
