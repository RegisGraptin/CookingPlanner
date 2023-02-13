FROM python:3.9

ENV POETRY_VERSION = 1.3.2
RUN pip install "poetry==$POETRY_VERSION"

# TODO :: Switch the way we install poerty
# TODO :: https://stackoverflow.com/questions/53835198/integrating-python-poetry-with-docker

# RUN apt-get -y update
# RUN curl -sSL https://install.python-poetry.org | python3 -

# RUN poetry --version

# # Project initialization:
# RUN poetry config virtualenvs.create false \
#   && poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

# TODO :: Put the files in a user repository instead of the /
# TODO :: Clean architecture
# TODO :: Define also as a parameter the path for the 'recipes.json'. + do the same with other files.


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
