from ..ingredients.veggies.Veggies import Veggies
from ..ingredients.pepperoni.Pepperoni import Pepperoni
from ..ingredients.cheese.Cheese import Cheese
from ingredient_factories.PizzaIngredientFactory import PizzaIngredientFactory
from ingredients.cheese.Mozzarella import Mozzarella
from ingredients.clams.FreshClams import FreshClams
from ingredients.dough.ThickCrustDough import ThickCrustDough
from ingredients.pepperoni.SlicedPepperoni import SlicedPepperoni
from ingredients.sauce.PlumTomatoSauce import PlumTomatoSauce
from ingredients.veggies.BlackOlives import BlackOlives
from ingredients.veggies.EggPlant import EggPlant
from ingredients.veggies.Spinach import Spinach


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):

    def create_cheese(self):
        return Mozzarella()

    def create_clams(self):
        return FreshClams()

    def create_dough(self):
        return ThickCrustDough()

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_sauce(self):
        return PlumTomatoSauce()

    def create_veggies(self):
        return [BlackOlives(), EggPlant(), Spinach()]
