FROM python:3.9

RUN apt-get -y update
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry --version

WORKDIR /cookingplanner

RUN poetry 

