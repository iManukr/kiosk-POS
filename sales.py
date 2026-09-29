class SalesLog:
    def __init__(self):
        # List requirement
        self.sales = []

        # Set requirement
        self.unique_products = set()

    def add_sale(self, item, quantity, total):
        """
        Records one sale.
        Each sale is stored as a tuple.
        """
        # Tuple requirement
        sale = (item, quantity, total)

        self.sales.append(sale)
        self.unique_products.add(item)

    def is_empty(self):
        """
        Checks if there are no sales yet.
        """
        return len(self.sales) == 0

    def total_revenue(self):
        """
        Calculates total money made.
        """
        total = 0

        for sale in self.sales:
            total = total + sale[2]

        return total

    def best_seller(self):
        """
        Finds the product sold in the highest quantity.
        """
        if self.is_empty():
            return None, 0

        quantities = {}

        # Count quantity sold per product
        for sale in self.sales:
            item = sale[0]
            quantity = sale[1]

            if item in quantities:
                quantities[item] = quantities[item] + quantity
            else:
                quantities[item] = quantity

        # Find best seller
        best_item = ""
        best_quantity = 0

        for item in quantities:
            if quantities[item] > best_quantity:
                best_quantity = quantities[item]
                best_item = item

        return best_item, best_quantity