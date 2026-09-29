class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def restock(self, amount):
        """
        Adds more stock to this product.
        """
        self.quantity = self.quantity + amount

    def has_enough_stock(self, amount):
        """
        Checks if we have enough stock to sell.
        """
        return amount <= self.quantity

    def reduce_stock(self, amount):
        """
        Removes stock after a sale.
        """
        self.quantity = self.quantity - amount

    def sale_total(self, amount):
        """
        Calculates total price for a sale.
        """
        return amount * self.price

    def to_file_line(self):
        """
        Converts product into one line for saving.
        Example:
        Bread,60,20
        """
        return f"{self.name},{self.price},{self.quantity}\n"