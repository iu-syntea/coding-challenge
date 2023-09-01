# Importing required modules from FastAPI and SQLAlchemy
from fastapi import FastAPI, Depends  # FastAPI for the web framework, Depends for dependency injection
from sqlalchemy.orm import Session  # Session to interact with the database

# Importing custom modules
from commons.database import SessionLocal, Base, engine  # Our database engine and session
from commons.models import QuestionAnswer  # The model that represents questions and answers in our database

# Create a FastAPI application
app = FastAPI()  # This is like telling the computer we're going to make a new web service

# Creating tables in the database
Base.metadata.create_all(bind=engine)  # This is like setting up the 'rooms' (tables) in our 'house' (database)

# This function helps us talk to the database
def get_db():
    db = SessionLocal()  # Open a new 'conversation' with the database
    try:
        yield db  # Have the 'conversation'
    finally:
        db.close()  # Say 'goodbye' to the database

# This is a place in our web service where we can store questions and answers
@app.post("/store/")
def store_conversation(question: str, answer: str, db: Session = Depends(get_db)):
    new_qa = QuestionAnswer(question=question, answer=answer)  # Make a new 'box' (record) to put our question and answer in
    db.add(new_qa)  # Put the 'box' in our 'storage room' (database table)
    db.commit()  # Make sure the 'box' stays there
    return {"status": "Stored"}  # Tell the user we did it

# This is a place where we can look at the most recent questions and answers
@app.get("/fetch_last/")
def fetch_last(n: int = 5, db: Session = Depends(get_db)):
    # Go into the 'storage room' and find the last 'n' 'boxes' (records)
    last_n_qa = db.query(QuestionAnswer).order_by(QuestionAnswer.id.desc()).limit(n).all()  
    return last_n_qa  # Show these 'boxes' to the user
