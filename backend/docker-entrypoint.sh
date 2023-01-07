#!/bin/sh

poetry run uvicorn cookingplanner.main:app --host 0.0.0.0 --port 8000 --reload
