from fastapi import FastAPI

import clients

app = FastAPI()


@app.get('/')
def get_health_status():
    """Get the health status of the API."""
    return {'health': 'OK'}


@app.get('/matching_service/questions/')
async def find_similar_question(q: str):
    qa_match = clients.get_best_matching_question(q)
    clients.log_interaction_to_history(q, qa_match)
    return qa_match
