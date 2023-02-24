# Cooking Planner - Backend

## Run the project

### Create a env file

Create a `.env` file that will contain the environment variables for the project. You can have a look at the `.env.example` to see what the environment variables are and which values you need to set. 

You can create multiple env files. One for testing, for development and one for production. 

// TODO :: Write a guide to explain in detail the .env variables, especially for specifying the values that can be used in prod or in testing only.

### Run it locally

In this project, we use [`Poetry`](https://python-poetry.org/) as a python package manager. If you are not familiar with it, you can simply take a look on the documentation in the website and [install it](https://python-poetry.org/docs/#installing-with-the-official-installer). Then, to install the dependencies of this project run:

```bash
poetry install
```

Finally, you can run a backend instance with the `docker-entrypoint.sh`

```bash
./docker-entrypoint.sh
```

You should now have a backend running on : `0.0.0.0:8000`

### Docker process

After creating your `.env` file, you can simply run a backend instance with docker:

```bash
sudo docker build . --file ./Dockerfile --tag cookingplanner-backend
sudo docker run --env-file .env -p 8000:8000 -t cookingplanner-backend:latest
```

## Linter & Testing

For the backend, we have set a linter, with `pylint`. We also had test created with `pytest`. 
For the testing, we have set a `.test.env` specifically for this purpose. 

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


# Some references - MONGO DB

https://www.tutorialspoint.com/python_data_science/python_nosql_databases.htm

https://pymongo.readthedocs.io/en/stable/tutorial.html

https://pymongo.readthedocs.io/en/stable/installation.html
