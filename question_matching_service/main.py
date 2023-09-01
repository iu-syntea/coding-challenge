# We're getting FastAPI, a web framework to make APIs
from fastapi import FastAPI, Depends
# Importing Session to interact with the database
from sqlalchemy.orm import Session

# Importing our database and models
from commons.database import SessionLocal, engine
from commons import models

# For text processing and finding similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import numpy as np  # For number stuff like finding the maximum

tfidf_vectorizer = TfidfVectorizer()
questions_cache = []
vectors_cache = None
matching_threshold = 0.5

# Make the tables in the database
models.Base.metadata.create_all(bind=engine)

# Create the FastAPI app
app = FastAPI()

# This function gets a new database session
def get_db():
    db = SessionLocal()
    try:
        yield db  # Use the database
    finally:
        db.close()  # Close it when done

@app.post("/match/")
def match_question(question: str, db: Session = Depends(get_db)):
    try:
        global vectors_cache
        global questions_cache

        # Get questions and answers from the database
        questions_answers = db.query(models.QuestionAnswer).all()

        # Check if the cache is stale
        if len(questions_cache) != len(questions_answers):
            questions_cache = [x.question for x in questions_answers]
            vectors_cache = tfidf_vectorizer.fit_transform(questions_cache).toarray()

        # Vectorize the new question
        new_vector = tfidf_vectorizer.transform([question]).toarray()

        # Calculate similarity scores
        similarity_scores = linear_kernel(new_vector, vectors_cache).flatten()

        # Find the index of the most similar question
        matched_index = np.argmax(similarity_scores)

        # Extract just the answers
        answers = [x.answer for x in questions_answers]

        # Check if similarity is above threshold
        if similarity_scores[matched_index] >= matching_threshold:
            return {"question": question, "answer": answers[matched_index]}
        else:
            return {"question": question}
    except Exception as e:
        return f"Question Macthing Service Failed: {e}"