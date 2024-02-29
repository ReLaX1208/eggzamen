class Pizza:

    def __init__(self, name, dough, sauce, toppings, price):
        """
        Args:
            name
            dough
            sauce
            toppings
            price
        Returns:
            None
        """
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings
        self.price = price
    def preapre(self):
        """
        Args:
            name
            dough
            sauce
            toppings
            price
        Returns:
            None
        """
        return f"готовим {self.name}, с {self.dough} тестом, с {self.sauce} соусом, с {self.toppings} начинками"
    def bake(self):
        """
        Args:
            name
            dough
            sauce
            toppings
            price
        Returns:
            str
        """
        return f"запекаем {self.name}"
    def cut(self):
        """
        Args:
            None
        Returns:
            str
        """
        return f"Режем {self.name}"
    def box(self):
        """
        Args:
            None
        Returns:
            str
        """
        return f"Забоксиваем {self.name}"
class PepperoniPizza(Pizza):
    def __init__(self):
        """
        Args:
            None
        Returns:
            None
        """
        super().__init__("Пицца пепперони", "Tonkoe", "Tomatniy", "Пепперони", 3500)
class BBQPizza(Pizza):
    def __init__(self):
        """
        Args:
            None
        Returns:
            None
        """
        super().__init__("Пицца BBQ", "Tonkoe", "barbeque", "Капуста", 6500)
class SeafoodPizza(Pizza):
    def __init__(self):
        """
        Args:
            None
        Returns:
            None
        """
        super().__init__("Пицца Морская", "Tonkoe", "Morskoi", "Voda", 5500)

class Order:
    def __init__(self):
        """
        Args:
            None
        Returns:
            None
        """
        self.pizzas: list[Pizza] = []
    def add_pizza(self, pizza: Pizza):
        """
        Args:
            pizza
        Returns:
            None
        """
        self.pizzas.append(pizza)
        print(f"{pizza.name} доблена")
    def calculate_total(self):
        """
        Args:
            None
        Returns:
            str
        """
        return sum(pizza.price for pizza in self.pizzas)
class Terminal:
    def __init__(self):
        """
        Args:
            None
        Returns:
            None
        """
        self.menu: dict[int, Pizza] = {1: PepperoniPizza(), 2: BBQPizza(), 3: SeafoodPizza(),}
        self.order = Order()
    def display_menu(self):
        """
        Args:
            None
        Returns:
            str
        """
        for key, pizza in self.menu.items():
            print(f"{key}. {pizza.name} -  {pizza.price}")
    def take_order(self):
        """
        Args:
            None
        Returns:
            str
        """
        while True:
            self.display_menu()
            choice = int(input())
            if choice in self.menu:
                self.order.add_pizza(self.menu[int(choice)])
            elif choice == 0:
                return True
            else:
                print("net takogo")
                continue
        
                

    def confirm_order(self):
        """
        Args:
            None
        Returns:
            str
        """
        if self.order:
            print(self.order.calculate_total())
            a = input("Podtverzhdaete? Y/N")
            if a.lower() == "y":
                print("zakaz")
                return True
            else:
                print("otmena")
                self.order = None
                return False
        else:
            print("no order")
            return False
    def take_payment(self):
        """
        Args:
            None
        Returns:
            str
        """
        for pizza in self.order.pizzas:
            print(pizza.preapre())
            print(pizza.bake())
            print(pizza.cut())
            print(pizza.box())
        print("thanks")
def main():
    """
        Args:
            None
        Returns:
            str
        """
    t = Terminal()
    odder_done = t.take_order()
    if odder_done:
        t.confirm_order()
        t.take_payment()
        
if __name__ == "__main__":
    main()