from uuid import UUID

from app.repositories.conversation_repository import ConversationRepository
from app.schemas.conversation import (
    ConversationCreate,
    ConversationUpdate,
)
from fastapi import HTTPException

class ConversationService:

    def __init__(
        self,
        repository: ConversationRepository,
    ):
        self.repository = repository
    def create_conversation(
    self,
    conversation_data: ConversationCreate,
):
        return self.repository.create(conversation_data)
    def get_conversations(self):
        return self.repository.get_all()
    

    def get_conversation(
        self,
        conversation_id: UUID,
    ):

        conversation = self.repository.get_by_id(
            conversation_id
        )

        if conversation is None:
            raise HTTPException(
                status_code=404,
                detail="Conversation not found",
            )

        return conversation
    def update_conversation(
    self,
    conversation_id: UUID,
    update_data: ConversationUpdate,
):

        conversation = self.get_conversation(
            conversation_id
        )

        return self.repository.update(
            conversation,
            update_data,
        )
    def delete_conversation(
    self,
    conversation_id: UUID,
):

        conversation = self.get_conversation(
            conversation_id
        )

        self.repository.delete(conversation)