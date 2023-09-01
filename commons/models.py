# Importing database column types from SQLAlchemy
from sqlalchemy import Column, Integer, String
# Importing our database 'Base' to make tables
from .database import Base
from commons import constants

# This makes a new table called 'questions_answers'
class QuestionAnswer(Base):
    __tablename__ = constants.TABLE_QA

    # The 'id' column. Every row gets a unique number!
    id = Column(Integer, primary_key=True, index=True)
    # The 'question' column. We put questions here.
    question = Column(String, index=True)
    # The 'answer' column. We put answers that go with the questions here.
    answer = Column(String)
