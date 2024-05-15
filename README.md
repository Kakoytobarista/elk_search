# FastAPI API Service with Elasticsearch Integration

## Setup Instructions:
1. Install Docker and Docker Compose on your system if not already installed.
2. Clone this repository to your local machine
```
https://github.com/Kakoytobarista/elk_search
```
3. Navigate to the infra dir from the root dir.
```
cd infra
```
4. Run the following command to build and start the project using Docker Compose:
   ```shell
   docker-compose up -d --build
5. Once the project is up and running, you can check the Docker container endpoints documentation by visiting:
```
http://localhost:8000/docs
```
ENDPOINT FOR CREATING RECORD:
```
http://localhost:8000/docs#/search/store_document_search__post
```
ENDPOINT FOR GETTING DATA:
```
http://localhost:8000/docs#/search/search_documents_search__get
```
_____

## Running Tests:

1. To run tests for the project, navigate to the root directory of the project in your terminal.
2. Execute the following command to set the Python path (You have to do it from the root dir):
```shell
export PYTHONPATH=$(realpath "src")
```
3. Run the tests using the following command:

```
pytest src/tests
```
