# Theater-Service-REST-API
Implementation of a simple REST service in the subject area "Theater Service" using CRUD operations. The software implementation is based on the Python programming language using the Flask framework, the JSON data storage model, and the Pytest framework for system testing.


## Prerequisites

Before running the project, ensure you have the following installed:

- Python (>=3.6)
- Flask
- Pytest

You can install Flask and Pytest using the following pip command:

```
pip install -r requirements.txt
```

## Usage

1. Clone the repository:

```
git clone https://github.com/HenashArtem/Theater-Service-REST-API.git
```

2. Navigate to the project directory:

```
cd Theater-Service-REST-API
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the Flask application:

```
python app.py
```

5. Once the server is running, you can access the API endpoints using a REST client or by making HTTP requests programmatically.

## API Endpoints

### Performances

- `GET /performances`: Get all performances
- `GET /performances/<performance_id>`: Get a specific performance
- `POST /performances`: Add a new performance
- `PUT /performances/<performance_id>`: Update a performance
- `DELETE /performances/<performance_id>`: Delete a performance

### Plays

- Similar endpoints for managing plays

### Theatres

- Similar endpoints for managing theatres

### Users

- Similar endpoints for managing users

## Running Tests

To run the tests, execute the following command:

```
pytest tests/test_{service_for_testing}.py
```

For example, the following command will run test_performances.py:

```
pytest tests/test_performances.py
```

