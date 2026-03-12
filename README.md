# DoIt
A simple todo application built with FastAPI and SQLite.

## Overview
DoIt is a straightforward todo application designed to allow users to manage their personal to-do lists. Its core value proposition is to provide an easy-to-use interface for adding, completing, and deleting tasks without requiring user authentication.

## Features
* Add new todos
* Complete existing todos
* Delete todos
* View all todos

## Requirements
* FastAPI
* SQLite
* Pytest
* Uvicorn
* Pydantic

## Installation
1. Clone the repository
2. Install the dependencies using `pip install -r requirements.txt`
3. Run the application using `uvicorn main:app --host 0.0.0.0 --port 8000`

## Usage
1. Open a web browser and navigate to `http://localhost:8000`
2. Add new todos by filling in the title and clicking the "Add Todo" button
3. Complete existing todos by clicking the checkbox next to the todo title
4. Delete todos by clicking the "Delete" button next to the todo title
5. View all todos by navigating to `http://localhost:8000/todos`