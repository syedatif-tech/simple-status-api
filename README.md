# Simple Status API

A lightweight REST API built with Flask that provides basic application
health and status endpoints.

This project is intentionally small and can be used as a starting point for
experiments, API testing, monitoring examples, or containerized applications.

## Endpoints

| Endpoint | Method | Description |
| --- | --- | --- |
| `/` | GET | Basic API information |
| `/health` | GET | Health check |
| `/status` | GET | Current service status and timestamp |

## Getting Started

Clone the repository and create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment and install dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
python app.py
```

The service will be available at:

```text
http://localhost:5000
```

## Running Tests

```bash
pytest
```

## Example

Request:

```bash
curl http://localhost:5000/health
```

Response:

```json
{
  "status": "healthy"
}
```

## License

This project is available under the MIT License.
