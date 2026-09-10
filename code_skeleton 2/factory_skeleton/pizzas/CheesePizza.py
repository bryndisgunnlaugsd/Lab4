from ingredient_factories.PizzaIngredientFactory import PizzaIngredientFactory
from pizzas.Pizza import Pizza


class CheesePizza(Pizza):

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self._ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print(f'preparing: {self.get_name()}')
        self._dough = self._ingredient_factory.create_dough()
        self.cheese = self._ingredient_factory.create_cheese()
        self.sauce = self._ingredient_factory.create_sauce()