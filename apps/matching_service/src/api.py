from fastapi import FastAPI
from pydantic import BaseModel

import config
from store import MemoryStore
from utils import calculate_jaccard_similarity

app = FastAPI()
store = MemoryStore()


class QAModel(BaseModel):
    id: int
    question: str
    answer: str


class QAMatchModel(BaseModel):
    id: int
    question: str
    answer: str
    score: float


@app.get('/')
def get_health_status():
    """Get the health status of the API."""
    return {'health': 'OK'}


@app.get('/questions')
def get_all_questions():
    for record in store.get_all_records():
        yield QAModel(id=record.id, question=record.question, answer=record.answer)


@app.get('/questions/')
def find_similar_question(user_question: str):
    best_match = None
    best_score = 0

    for record in store.get_all_records():
        score = calculate_jaccard_similarity(user_question, record.question)
        if score > config.MATCHING_MIN_SCORE and score > best_score:
            best_score = score
            best_match = QAMatchModel(
                id=record.id,
                question=record.question,
                answer=record.answer,
                score=score
            )

    return best_match
