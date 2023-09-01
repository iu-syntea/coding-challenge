import os

DB_URL = os.environ.get('DB_URL')
QA_SERVICE = "http://matching_api:8000/ask"
QA_MATCHING_SERVICE = "http://matching_api:8001/match"
QA_STORAGE_SERVICE = "http://storage_api:8002/store"
QA_FETCH_SERVICE = "http://storage_api:8002/fetch"
TABLE_QA = "questions_answers"