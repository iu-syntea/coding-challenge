# Code Challenge: Senior Backend Developer

## Overview

In this code challenge, you will be implementing three simple microservices for a conversational AI system using Python 3.9+ and FastAPI. The purpose of these microservices is to:

1. Provide an API to ask questions and return answers
2. Find the best matching answers from a knowledge base
3. Store conversation history and expose API to fetch last conversations

You will also create a Docker Compose file to run the entire system.

**Time Constraint**: You have up to 4 hours to complete this task. It is okay if the task is not 100% completed, but please submit your best effort within the given time frame.

## Requirements

1. **API Service**: Implement a FastAPI service that exposes a single endpoint for asking questions. The endpoint should accept a text input representing the user's question and return a JSON response containing the best matching answer from the knowledge base.

2. **Answer Matching Service**: Implement a FastAPI service that takes a question as input and returns the best matching answer from a predefined knowledge base. The knowledge base can be a simple list of question-answer pairs. The service should use a simple algorithm to find the best match (e.g., cosine similarity, Jaccard similarity, or any other text matching technique).

3. **Conversation History Service**: Implement a FastAPI service to store the conversation history and expose an API to fetch the last conversations. You can choose the most appropriate storage type for this service (e.g., in-memory, file-based, or a database).

4. **Communication**: Use an appropriate communication method between the services. You can choose between synchronous HTTP calls, message queues, or any other method that fits the use case.

5. **Docker Compose**: Create a `docker-compose.yml` file to run all three services and any additional infrastructure needed (e.g., message broker, database).

## Evaluation Criteria

Your solution will be evaluated based on the following criteria:

1. Correctness and completeness of the implementation
2. Code quality, readability, and organization
3. Proper use of FastAPI features and best practices
4. Efficiency and performance of the answer matching algorithm
5. Scalability and maintainability of the overall solution

## Submission

Please submit your solution as a PR to this repository. Your PR should include

1. The source code for all three services, organized into separate folders
2. A `docker-compose.yml` file for running the entire system
3. A `INSTRUCTIONS.md` file with instructions on how to build and run the services

Good luck!