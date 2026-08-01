from uuid import UUID

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.repositories.conversation_repository import ConversationRepository
from app.schemas.conversation import (
    ConversationCreate,
    ConversationResponse,
    ConversationUpdate,
)
from app.services.conversation_service import ConversationService
from typing import List

router = APIRouter(
    prefix="/api/v1/conversations",
    tags=["Conversations"],
)

def get_conversation_service(
    db: Session = Depends(get_db),
) -> ConversationService:

    repository = ConversationRepository(db)

    return ConversationService(repository)
@router.post(
    "",
    response_model=ConversationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_conversation(
    conversation: ConversationCreate,
    service: ConversationService = Depends(
        get_conversation_service
    ),
):
    return service.create_conversation(conversation)
@router.get(
    "",
    response_model=list[ConversationResponse],
)
def get_conversations(
    service: ConversationService = Depends(get_conversation_service),
):
    return service.get_conversations()
@router.get(
    "/{conversation_id}",
    response_model=ConversationResponse,
)
def get_conversation(
    conversation_id: UUID,
    service: ConversationService = Depends(get_conversation_service),
):
    return service.get_conversation(conversation_id)
@router.patch(
    "/{conversation_id}",
    response_model=ConversationResponse,
)
def update_conversation(
    conversation_id: UUID,
    conversation: ConversationUpdate,
    service: ConversationService = Depends(get_conversation_service),
):
    return service.update_conversation(
        conversation_id,
        conversation,
    )
@router.delete(
    "/{conversation_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_conversation(
    conversation_id: UUID,
    service: ConversationService = Depends(get_conversation_service),
):
    service.delete_conversation(conversation_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)