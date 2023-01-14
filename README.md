
# Cooking Planner

## Besoin ?

- Qu'est ce que je vais manger durant la semaine ?

=> Préparer mes recettes en avance de la semaine (recette + course)
=> Organisation des personnes
=> Possibilité d'innover dans leur choix

[] Choix -> Ne souhaite pas commander en ligne / Aller au restaurant
=> Trop chère / Contrôler le budget
=> Manger seinement
=> Possibilité de cuisiner
=> Contrainte de temps => Préparer en avance pour être rapide 
=> Pas de possibilité de cuisiner en dehors de chez soi


## Questions

-> Qu'est ce que je peux me faire à manger ?
-> Quels recettes de cuisines je souhaite faire pour une semaine ?
-> Quels ingrédients j'ai besoin pour créer mes recettes ?
-> Quels est le temps que je suis prêt à allouer pour ces recettes ?
-> Est-ce que je dois préparer des repas pour le travail ?
-> Quel nouveau plat je souhaite essayer ? 
-> Organiser & utiliser les restes d'autres repas.
...

La cuisine doit être fun et non une contrainte
=> Changer l'image de la cuisine et manger correctement
Agréable et bon


## Solution 

- Création d'une liste de recette pour une semaine.
- Contrainte sur le nombre de repas.
- Contrainte sur l'usage des restes possibles / Préparation des repas en grande quantité
- Contrainte sur le temps de préparation.
- Contrainte sur le budget.






TODO :: Decompose readme for backend and front end
TODO :: Here global things
TODO :: Docker build backend


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


# Concurence

- Analyse the concurrency
        - https://jow.fr/
        - https://whisk.com/
        - Restover

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