import asyncio
import logging
from datetime import datetime

import requests

import config

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(config.LOG_LEVEL)


def get_best_matching_question(question: str):
    """ Fetches matching questions from an external service asynchronously. """
    matching_service_url = config.SERVICE_MATCHING_URL
    params = {'user_question': question}
    response = requests.get(matching_service_url, params=params)
    logger.info(f'Calling {matching_service_url} with (user_question={question})')
    return response.json()


def log_interaction_to_history(user_question, matched_question):
    """ Logs user interactions and matched questions to the history service. """
    history_service_url = config.SERVICE_HISTORY_URL
    logger.info(f'log_interaction_to_history:({user_question}, {matched_question["id"] if matched_question else None})')
    interaction_data = {
        'ts': datetime.utcnow().timestamp(),
        'user_question': user_question,
        'matched_question': matched_question
    }

    response = requests.post(history_service_url, json=interaction_data)
    logger.info(f'log_interaction_to_history: (status={response.status_code}, uuid={response.json().get("uuid")}')
