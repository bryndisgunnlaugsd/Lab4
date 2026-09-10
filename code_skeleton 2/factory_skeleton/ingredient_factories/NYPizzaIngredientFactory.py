from ingredient_factories.PizzaIngredientFactory import PizzaIngredientFactory
from ingredients.cheese.ReggianoCheese import ReggianoCheese
from ingredients.clams.FreshClams import FreshClams
from ingredients.dough.ThinCrustDough import ThinCrustDough
from ingredients.pepperoni.SlicedPepperoni import SlicedPepperoni
from ingredients.sauce.MarinaraSauce import MarinaraSauce
from ingredients.veggies.Garlic import Garlic
from ingredients.veggies.Mushroom import Mushroom
from ingredients.veggies.Onion import Onion
from ingredients.veggies.RedPepper import RedPepper


# CONCRETE Factory 1: knows how to build the New York family of ingredirents
# This is the only class that ever mentions ThinCrustDough, MarinaraSauce, 
# ReggianoCheese or FreshClams
# Anything that wants NY-style ingredients goes through this class instead of 
# initiating those ingredient classes directkly

class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def create_cheese(self):
        return ReggianoCheese()

    def create_clams(self):
        return FreshClams()

    def create_dough(self):
        return ThinCrustDough

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_sauce(self):
        return MarinaraSauce()

    def create_veggies(self):
        return [Garlic(), Mushroom(), Onion(), RedPepper()]