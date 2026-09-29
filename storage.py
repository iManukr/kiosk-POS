import os
from inventory import Inventory


class Storage:
    def __init__(self):
        self.stock_file = "stock.txt"
        self.sales_file = "sales_history.txt"
        self.alert_file = "restock_alerts.txt"

    def load_inventory(self):
        """
        Loads inventory from file.
        If file does not exist, creates default stock.
        """
        inventory = Inventory()

        if os.path.exists(self.stock_file):
            file = open(self.stock_file, "r")

            for line in file:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split(",")

                if len(parts) == 3:
                    name = parts[0].strip().title()
                    price = int(parts[1])
                    quantity = int(parts[2])

                    inventory.add_product(name, price, quantity)

            file.close()

        else:
            # Default stock
            inventory.add_product("Bread", 60, 20)
            inventory.add_product("Milk", 50, 30)
            inventory.add_product("Sugar", 150, 15)

        return inventory

    def save_inventory(self, inventory):
        """
        Saves current inventory to stock.txt
        """
        file = open(self.stock_file, "w")

        for product in inventory.products.values():
            file.write(product.to_file_line())

        file.close()

    def save_sales(self, sales_log):
        """
        Appends today's sales to sales_history.txt
        """
        if sales_log.is_empty():
            return

        file = open(self.sales_file, "a")

        for sale in sales_log.sales:
            file.write(f"{sale[0]},{sale[1]},{sale[2]}\n")

        file.close()

    def save_alerts(self, inventory):
        """
        Saves low stock alerts.
        """
        file = open(self.alert_file, "w")
        file.write("=== RESTOCK ALERTS ===\n")

        low_items = inventory.low_stock_products(5)

        if len(low_items) == 0:
            file.write("No low stock items.\n")
        else:
            for product in low_items:
                file.write(f"- {product.name}: only {product.quantity} left\n")

        file.close()