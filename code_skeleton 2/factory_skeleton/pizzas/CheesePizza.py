from ingredient_factories.PizzaIngredientFactory import PizzaIngredientFactory
from pizzas.Pizza import Pizza

# CheesePizza is a product (PizzaStore creates it)
# also a client (it consumes a PizzaIngredientFactory to get its ingredients)

class CheesePizza(Pizza):

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self._ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print(f'preparing: {self.get_name()}')
        # Which factory we are given determines what comes back here
        # ThinCrustDough vs. ThickCrustDough
        self._dough = self._ingredient_factory.create_dough()
        self.cheese = self._ingredient_factory.create_cheese()
        self.sauce = self._ingredient_factory.create_sauce()