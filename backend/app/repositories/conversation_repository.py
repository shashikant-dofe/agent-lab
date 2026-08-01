from uuid import UUID

from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.conversation import Conversation
from app.schemas.conversation import (
    ConversationCreate,
    ConversationUpdate,
)


class ConversationRepository:
    def __init__(self, db: Session):
            self.db = db
    def create(
    self,
    conversation_data: ConversationCreate,
) -> Conversation:

        conversation = Conversation(
            title=conversation_data.title,
        )

        self.db.add(conversation)
        self.db.commit()
        self.db.refresh(conversation)

        return conversation
    def get_all(self) -> list[Conversation]:
        stmt = (
            select(Conversation)
            .order_by(Conversation.created_at.desc())
        )

        result = self.db.execute(stmt)

        return result.scalars().all()
    def get_by_id(
    self,
    conversation_id: UUID,
) -> Conversation | None:

        stmt = select(Conversation).where(
            Conversation.id == conversation_id
        )

        result = self.db.execute(stmt)

        return result.scalar_one_or_none()
    def update(
        self,
        conversation: Conversation,
        update_data: ConversationUpdate,
    ) -> Conversation:

        if update_data.title is not None:
            conversation.title = update_data.title

        if update_data.status is not None:
            conversation.status = update_data.status

        self.db.commit()
        self.db.refresh(conversation)

        return conversation
    def delete(
    self,
    conversation: Conversation,
) -> None:

        self.db.delete(conversation)
        self.db.commit()