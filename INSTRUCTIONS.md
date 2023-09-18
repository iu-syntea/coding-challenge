# iu-coding-challenge

## Overview
This document provides instructions for running the iu-coding-challenge using Docker Compose. 

## Prerequisites
Before you begin, ensure you have the following prerequisites installed on your system:
- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Running the Project

1. Clone the git branch from GitHub.

2. Change your working directory to the project directory.

3. Start the docker container:
    ```bash 
    docker-compose up

4. Query different services:
   1. **api-service:** http://localhost:8000/matching_service/questions/?q=what%20is%20the%20capital
   2. **matching-service:** http://localhost:8001/questions/?user_question=what%20is%20the%20capital%20south
   3. **history-service:** http://localhost:8002/logs/

To display all the available questions and answers: http://localhost:8001/questions 

## Decision-Making and Future Directions
In the course of developing this solution, I had to make several decisions balancing between a simple solution development, scalability, and time constraints. Here are the key decisions made and considerations for future work:

### Current data storage
* **Matching Service**: I've opted for a memory store to load and manage the Question and Answers csv file efficiently.
* **History Service**: To store the conversation history, I've chosen a file system-based logging approach.
### Future Directions
1. **Exception Handling and API Status Codes:** Implement robust exception handling and appropriate API status codes. 
2. **Testing**: it's essential to add both unit and integration tests into the development pipeline. 
3. **Event-Driven Architecture**: Implement an event-driven communication approach among microservices. Leveraging technologies like Kafka as an event store can be beneficial, especially for displaying the conversational history.
4. **Scalability**: The current memory store used by the matching-service has limitations in terms of scaling and sharding. Consider transitioning to an in-memory distributed datastore like Redis for enhanced scalability. 
5. **Performance Enhancement**: Even with a distributed datastore, the performance is still subject to the time required for calculating matching scores. Two potential solutions:
   1. Parallel Processing: Implement a queuing system that can perform matching score calculations in parallel. This approach divides the computation time needed for a single query among multiple workers. 
   2. Job Queue: For exceptionally large datasets or situations where providing a sufficient number of workers is challenging, consider implementing a queuing API. In this scenario, requests would only create new jobs that are queued in a job queue, allowing for efficient handling of resource-intensive tasks.

I added some examples into the codebase in the branch [faster-matching-service](https://github.com/amribr/coding-challenge/compare/u/amribrahim/qa-api-services...amribr:coding-challenge:u/amribrahim/faster-matching-service?expand=1), aiming to optimize the performance of matching score calculations. It is important to note that while these optimizations have the potential to boost performance, their effectiveness is constrained, and they come with several limitations. This approach does not effectively shard the data, resulting in the entire dataset being loaded into all instances of the matching-service instances.
