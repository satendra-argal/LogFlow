# LogFlow

LogFlow is a web application designed to track and analyze user activity logs. It allows you to manage activity logs by adding, retrieving, and analyzing them with various filters and statistics.

## Features

- **Add Logs**: Post user activity logs with associated metadata.
- **Retrieve Logs**: Get user activity logs with filtering options (by date range and activity type).
- **Activity Statistics**: Retrieve statistics such as activity counts per user and the most frequent activity.

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Migrations**: Flask-Migrate
- **Frontend**: React.js (for future enhancements)
- **Docker**: Containerization for both backend and database
- **CORS**: Cross-Origin Resource Sharing for API accessibility

## 1. Setup Instructions

### 1.1. Prerequisites

- Docker
- Docker Compose
- Python (for development and testing)

### 1.2. Clone the Repository

```bash
git clone https://github.com/satendra-argal/LogFlow.git
cd LogFlow
```
## 2. API Endpoints

### 2.1. POST /logs
Add a new activity log.

Request Body
```bash
[
{
  "user_id": "12",
  "activity": "Login",
  "timestamp": "2025-01-16T10:00:00",
  "custom_metadata": {
    "device": "laptop"
  }
}
```

### 2.3. GET /logs/stats
Get activity statistics such as the activity count per user and the most frequent activity in the specified date range.

Query Parameters
start: Start date (ISO 8601 format)
end: End date (ISO 8601 format)
Response
```bash
{
  "user_activity_count": {
    "12": 10
  },
  "most_frequent_activity": "Login"
}
```
## 3. Docker Setup

If you are running the app via Docker, ensure the following setup:

- **Docker Compose**: Used to handle multi-container environments.
- **Backend Service (`flask-backend`)**: Built from the `./backend` directory and exposes port 5000.
- **Frontend Service (`react-frontend`)**: Built from the `./frontend` directory and exposes port 3000.
- **PostgreSQL Database (`postgres-db`)**: Exposed via the `postgres-db` service and uses port 5432.

### 3.1. Example Docker Compose Command to Start the App

To start the app, use the following command:

```bash
docker-compose up --build
```
## 4. Testing the Application

### 4.1. Test the API

You can test the endpoints using Postman, Curl, or any HTTP client.

- **POST /logs**: Add logs
- **GET /logs/{user_id}**: Fetch logs for a user
- **GET /logs/stats**: Get activity stats

### 4.2. Test the Frontend

Visit [http://localhost:3000](http://localhost:3000) to see the React frontend, which can be connected to the backend APIs for user interaction.
