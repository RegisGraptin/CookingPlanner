
export PYTHONPATH="${PYTHONPATH}:./cookingplanner/"

Remarks:

Need to think about the recipe storage.
Have a unique object with "origin" field that is unique ? 


## Run script

poetry run python your_script.py

poetry run pytest

Note: Coverage test

poetry run pytest --cov

## Activate the environment

poetry shell

## Linter

```shell
poetry run pylint ./cookingplanner
```

Pre-commit

```shell
poetry run pre-commit run --all-files
```


## TODO: 

- Have a precise naming for each class. (Structuration of the project + diagram)
- Write the readme description of this project (what for ? execution ?)

- Decomposition in scraping for the recipe step.


- Think about the organisation of a web services (backend)



## TODO :

- `scraping_url`: Have a better organization on the generation of new urls. (Pending)




# MONGO DB

https://www.tutorialspoint.com/python_data_science/python_nosql_databases.htm

https://pymongo.readthedocs.io/en/stable/tutorial.html

https://pymongo.readthedocs.io/en/stable/installation.html