from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ConversationBase(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=255,
        description="Conversation title",
    )
class ConversationCreate(ConversationBase):
    pass
class ConversationUpdate(BaseModel):
    title: str | None = Field(
        default=None,
        min_length=1,
        max_length=255,
    )

    status: str | None = None
class ConversationResponse(ConversationBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    status: str
    created_at: datetime
    updated_at: datetime