from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func

from cookingplanner.models.database import Database


Base = Database().Base

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
    is_active  = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), default=func.now())



class Ingredient(Base):
    """Ingredients"""

    __tablename__ = 'ingredients'

    id   = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    # Possibility to add additional information about the ingredient
    # TODO :: https://www.data.gouv.fr/fr/datasets/open-food-facts-produits-alimentaires-ingredients-nutrition-labels/#resources


# Équipement de cuisine
# - Plaque de cuisson 
# - Micro ondes
# - Four 
# - Friteuse
# - Robot cuiseur
# - Mixeur 
# ...
class CookingEquipment(Base):
    """Cooking equipment.

    This can be used for the user to defined his own equipment or for the recipe 
    to defined the needed equipments.
    """

    __tablename__ = 'cooking_equipments'

    id   = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


class Profile(Base):

    __tablename__ = 'profiles'

    id   = Column(Integer, primary_key=True, index=True)
    user = Column(Integer, ForeignKey("users.id"))

    n_persons = Column(Integer)

    # 0: Small budget - 5: No restriction
    cost = Column(Integer)

    # 0 : No spicy - 5: No restriction
    spicy = Column(Integer)

    # 0: Known recipe - 5: Risky every week
    culinary_adventurousness = Column(Integer)

    # 0: beginner - 5: expert
    cooking_level = Column(Integer)

    # 0: No diversity - 7: Unique recipe --> Allow multiple recipes for same week
    recipe_diversity = Column(Integer)

    # Diversity: Multiple ingredients - Macro nutriment
    # 0 - One/Two ingredients - 5 - Large variety
    ingredient_diversity = Column(Integer)


    # Temps de cuisine disponible
    # Cuisiner tout les soirs ? 
    # Autoriser les restes de repas ? Plat unique ?
    cooking_time = Column(Integer)

    # Indicate if we used seasonal ingredient for the recipe
    seasonal_recipe = Column(Boolean, default=False)


    # Possibilité de créer une autre class permettant de prendre en compte les ingrédients qui ne matchent 
    # pas avec l'utilisateur (catégorie d'ingrédient)
    # Régime alimentaire 
    # - Végétarien
    # - Végétalien (végan)
    # - Sans porc 
    # - Sans gluten
    # - Sans produit laitier
    # - Pesco végétarien
    # - Autre ?
    


class ProfileCookingEquipment(Base):
    """Define the Cooking Equipment for a given profile."""

    __tablename__ = "profile_cooking_equipment"

    profile_id           = Column(Integer, ForeignKey('profiles.id'), primary_key=True, nullable=False)
    cooking_equipment_id = Column(Integer, ForeignKey('cooking_equipments.id'), primary_key=True, nullable=False)

class ProfileNotIngredient(Base):
    """Ingredient that should not be in the proposed recipes (Ex: Allergie)."""

    __tablename__ = "profile_not_ingredient"

    profile_id    = Column(Integer, ForeignKey('profiles.id'), primary_key=True, nullable=False)
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'), primary_key=True, nullable=False)


