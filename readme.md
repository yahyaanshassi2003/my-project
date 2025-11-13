# Idea Manager Flask App

A simple Flask web application to manage ideas. Users can **add**, **edit**, **delete**, and **view ideas**. The app uses **SQLite** for database storage and supports testing via **pytest**.

---

## Table of Contents

- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Environment Setup](#environment-setup)  
- [Running the App Locally](#running-the-app-locally)  
- [Database Initialization](#database-initialization)  
- [Running Tests](#running-tests)  
- [Project Structure](#project-structure)  

---

## Features

- List all ideas with timestamps  
- Add new ideas with title and description  
- Edit existing ideas  
- Delete ideas  
- Flash messages for success and error feedback  
- Error handling for 404 pages  

---

## Prerequisites

Before running the app, ensure you have:

- **Python 3.10+** installed  
- **pip** (Python package manager)  
- **virtualenv** (optional, but recommended)  

---

## Environment Setup

1. **Clone the repository**

```bash
git clone <repository-url>
cd <repository-folder>



Create a virtual environment (optional, but recommended)

python -m venv venv


Activate the virtual environment

On macOS/Linux:

source venv/bin/activate


On Windows:

venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Set environment variables

Create a .env file in the root directory:

SECRET_KEY=your_secret_key_here
DATABASE=database/app.db


SECRET_KEY: Used by Flask for sessions and security

DATABASE: Path to SQLite database file (default: database/app.db)

Running the App Locally

Ensure your virtual environment is activated.

Run the Flask application:

python app.py


Open your browser and visit:

http://127.0.0.1:5000/


Database Initialization


The database is automatically initialized when the app starts. The init_db() function ensures that the ideas table exists.

If you want to manually initialize or reset the database:

Open Python in the project directory:

python


Run the following:

from app import create_app
from database.db import init_db

app = create_app()
with app.app_context():
    init_db()


This creates a SQLite database file (default: database/app.db) and a table ideas with the following schema:

CREATE TABLE IF NOT EXISTS ideas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

Running Tests

Tests are written using pytest and include basic functionality tests for:

Index page accessibility

Adding an idea

Ensure your virtual environment is activated.

Install testing dependencies (if not already installed):

pip install pytest


Run tests:

pytest


Tests use a separate test database test.db to avoid affecting your main database.

Example tested scenarios:

- Accessing homepage returns status code 200
- Adding a new idea stores it in the database and returns a success message