#!/bin/sh

poetry run uvicorn cookingplanner.main:app --reload
