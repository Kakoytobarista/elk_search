# FastAPI API Service with Elasticsearch Integration

## Setup Instructions:
1. Install Docker/Docker Compose, python3 on your system if not already installed.
2. Clone this repository.
    ```shell
    git clone https://github.com/Kakoytobarista/elk_search.git```
3. Navigate to the infra dir from the root dir (ROOT DIR: elk_search)
   ```shell
   cd infra
   ```
4. Run the following command to build and start the project using Docker Compose:
   ```shell
   docker-compose up -d --build
   ```
5. Once the project is up and running, you can check the Docker container endpoints documentation by visiting:
    ```text
    http://localhost:8000/docs
    ```
PS:
I've pre-populated elk with data so you can search by these words:
   ```text
       We are searching text hello
       We are searching text bye
       We are searching text hi
       We are searching text hey
       We are searching text bye bye
   ```

ENDPOINT FOR CREATING RECORD:
   ```text
   http://localhost:8000/docs#/search/store_document_search__post
   ```
ENDPOINT FOR GETTING DATA:
   ```text
   http://localhost:8000/docs#/search/search_documents_search__get
   ```
_____

## Running Tests:
For running tests, make sure that ELK working on 9200 (better way to use docker-compose up the first and then tests)
1. To run tests for the project, navigate to the src dir and run commands (if you dont have poetry, install it)
    ```shell
    poetry shell
    poetry install
    ```
2. Navigate to root dir and execute the following command to set the Python path:
    ```shell
    export PYTHONPATH=$(realpath "src")
    ```
3. Run the tests using the following command:
    ```shell
    pytest src/tests
    ```
