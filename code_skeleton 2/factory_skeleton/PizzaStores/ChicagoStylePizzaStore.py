from PizzaStores.PizzaStore import PizzaStore
from ingredient_factories.ChicagoPizzaIngredientFactory import ChicagoPizzaIngredientFactory
from pizzas.CheesePizza import CheesePizza
from pizzas.ClamPizza import ClamPizza
from pizzas.PepperoniPizza import PepperoniPizza
from pizzas.Pizza import Pizza
from pizzas.PizzaType import PizzaType
from pizzas.VeggiePizza import VeggiePizza


class ChicagoStylePizzaStore(PizzaStore):
    def create_pizza(self, pizza_type: PizzaType) -> Pizza:
        ingredient_factory = ChicagoPizzaIngredientFactory()
        pizza = None

        if pizza_type == PizzaType.CHEESE:
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name("Chicago Style Cheese Pizza")

        elif pizza_type == PizzaType.PEPPERONI:
            pizza = PepperoniPizza(ingredient_factory)
            pizza.set_name("Chicago Style Pepperoni Pizza")

        elif pizza_type == PizzaType.CLAM:
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name("Chicago Style Clam Pizza")

        elif pizza_type == PizzaType.VEGGIE:
            pizza = VeggiePizza(ingredient_factory)
            pizza.set_name("Chicago Style Veggie Pizza")

        return pizza