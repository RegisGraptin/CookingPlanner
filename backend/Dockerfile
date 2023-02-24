FROM python:3.9

# Poetry installation : https://stackoverflow.com/questions/53835198/integrating-python-poetry-with-docker
ENV POETRY_VERSION = 1.3.2
RUN pip install "poetry==$POETRY_VERSION"

COPY poetry.lock pyproject.toml /

RUN poetry install

COPY recipes.json /

WORKDIR /cookingplanner
COPY ./cookingplanner .


WORKDIR /
COPY ./docker-entrypoint.sh .
RUN chmod +x 'docker-entrypoint.sh'

EXPOSE 8000

ENTRYPOINT [ "/docker-entrypoint.sh" ]
