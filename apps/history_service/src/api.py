from datetime import datetime
from uuid import UUID, uuid4

from fastapi import FastAPI
from pydantic import BaseModel, Field

import config
from store import ConversationHistoryLog

app = FastAPI()
store = ConversationHistoryLog(config.LOG_FILE)


class QAMatchModel(BaseModel):
    question: str
    answer: str
    score: float


class ConversationLogModel(BaseModel):
    uuid: UUID = Field(default_factory=uuid4)
    ts: datetime
    user_question: str
    matched_question: QAMatchModel | None


@app.get('/')
def get_health_status():
    """Get the health status of the API."""
    return {'health': 'OK'}


@app.post('/logs/')
def write_log(log_entry: ConversationLogModel):
    """Write a conversation log entry to the store."""
    store.write(log_entry.model_dump_json())
    return log_entry


@app.get('/logs/')
def get_all_logs():
    """Retrieve all conversation logs."""
    for record in store.get_all():
        yield ConversationLogModel.model_validate_json(record)
