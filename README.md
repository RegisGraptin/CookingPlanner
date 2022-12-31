
# Cooking Planner

Description: TODO
Given a week, we want to generate for each dish a recipe. 
This allow us to organize the shopping list, the dishes, the recipes...


## Running

```bash
export PYTHONPATH="${PYTHONPATH}:./cookingplanner/"
poetry run python ./cookingplanner/main.py --update name_of_strategy
```

### Run web services 

```bash
poetry run uvicorn main:app --reload
```

Swagger 

http://127.0.0.1:8000/docs

### Parameters

- `--update`: indicates we want to scrap online website for getting recipes.
- `strategy`: indicates the types of strategy we want to apply to generate the next week.
        - `unique`: Strategy of having a different recipe each day of the week.


## Linter & Testing

A hook is define for each commit. We ensure that the linting and the test execution is correct.

Pre-commit

```shell
poetry run pre-commit run --all-files
```

### Pylint

```bash
poetry run pylint ./cookingplanner/
```

### Pytest

Run the tests.

```bash
poetry run pytest
```

Possibility to see the code coverage.

```bash
poetry run pytest --cov
```

## Activate the environment

poetry shell


## TODO: 

- Have a precise naming for each class. (Structuration of the project + diagram)
- Write the readme description of this project (what for ? execution ?)
- Think about the organisation of a web services (backend)


- Recipe Storage: Json encoding and decoding is not really good.
- Recipe source field : Passed it directly in a dictionary and not as a variable ? (serialization issue)



## TODO :


- Go to MVP : basic scrap, basic week generation, basic website => go to prod quick

- `scraping_url`: Have a better organization on the generation of new urls. (Pending)
        Idea : Given a url and a website, we could have different manner of generating new urls.
        Thus this process should be delegated on the main class extractor (Marmiton, Recette-du-coin, ...)

## MVP 

- Hypothesis 1 : We generate only a main dish at the moment. In future version we could think on the decomposition of a meal in entree, main meal, dessert...


# MONGO DB links

https://www.tutorialspoint.com/python_data_science/python_nosql_databases.htm

https://pymongo.readthedocs.io/en/stable/tutorial.html

https://pymongo.readthedocs.io/en/stable/installation.html