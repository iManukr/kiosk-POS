from product import Product


class Inventory:
    def __init__(self):
        # Dictionary requirement
        # Format:
        # {"Bread": Product object, "Milk": Product object}
        self.products = {}

    def contains(self, name):
        """
        Checks if product exists in inventory.
        """
        return name in self.products

    def add_product(self, name, price, quantity):
        """
        Adds a brand new product.
        """
        self.products[name] = Product(name, price, quantity)

    def restock(self, name, amount):
        """
        Restocks an existing product.
        """
        if name in self.products:
            self.products[name].restock(amount)
            return True

        return False

    def sell(self, name, quantity):
        """
        Attempts to sell a product.
        Returns:
        success, message, total
        """
        if name not in self.products:
            return False, f"{name} is not in stock.", 0

        product = self.products[name]

        if not product.has_enough_stock(quantity):
            return False, f"Not enough {name}. Only {product.quantity} left.", 0

        product.reduce_stock(quantity)
        total = product.sale_total(quantity)

        return True, "Sale completed.", total

    def search(self, term):
        """
        Searches products using partial matching.
        """
        term = term.lower()
        results = []

        for product in self.products.values():
            if term in product.name.lower():
                results.append(product)

        return results

    def low_stock_products(self, threshold=5):
        """
        Returns products whose quantity is below threshold.
        """
        low_items = []

        for product in self.products.values():
            if product.quantity < threshold:
                low_items.append(product)

        return low_items