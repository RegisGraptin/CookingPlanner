# Backend Application

## CookingPlanncer package


```
sudo docker build .
sudo docker run -p 8000:8000 2b71b2c4c3a5
```

sudo docker exec -it 2b71b2c4c3a5 bash

# Testing 

Production or Testing more are present in our script in order to load the corresponding database.


# Entry point


generate


```bash
export PYTHONPATH="${PYTHONPATH}:./cookingplanner/"
poetry run python ./cookingplanner/main.py --update name_of_strategy
```

- `--update`: indicates we want to scrap online website for getting recipes.
- `strategy`: indicates the types of strategy we want to apply to generate the next week.
        - `unique`: Strategy of having a different recipe each day of the week.



# URLs 

http://0.0.0.0:8000/week/work/unique



## Planning

- The '/week/work/unique' return empty/null fields for the dish. 
    - Add testes to reproduce this issues
    - Correct the issue



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



# MONGO DB links

https://www.tutorialspoint.com/python_data_science/python_nosql_databases.htm

https://pymongo.readthedocs.io/en/stable/tutorial.html

https://pymongo.readthedocs.io/en/stable/installation.html
