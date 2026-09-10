from ingredient_factories.PizzaIngredientFactory import PizzaIngredientFactory
from pizzas.Pizza import Pizza


class PepperoniPizza(Pizza):

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self._ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print(f'preparing: {self.get_name()}')
        self._dough = self._ingredient_factory.create_dough()
        self._cheese = self._ingredient_factory.create_cheese()
        self._sauce = self._ingredient_factory.create_sauce()
        self._veggies = self._ingredient_factory.create_veggies()
