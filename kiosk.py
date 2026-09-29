from utils import clean_text, get_positive_int
from storage import Storage
from sales import SalesLog
from reports import Reports


class Kiosk:
    def __init__(self):
        self.kiosk_name = clean_text("Enter the kiosk's name: ")
        self.owner_name = clean_text("Enter the owner's name: ")

        self.storage = Storage()
        self.inventory = self.storage.load_inventory()
        self.sales_log = SalesLog()
        self.reports = Reports(self.inventory, self.sales_log)

    def run(self):
        """
        Main program loop.
        """
        print(
            f"\nWelcome to {self.kiosk_name}'s Kiosk Manager, "
            f"run by {self.owner_name}"
        )

        while True:
            self.print_menu()
            choice = input("Enter your choice: ").strip()

            if not choice.isdigit():
                print("Please enter a number between 1 and 6.")
                continue

            choice = int(choice)

            if choice == 1:
                self.reports.print_stock()

            elif choice == 2:
                self.add_or_restock_product()

            elif choice == 3:
                self.sell_product()

            elif choice == 4:
                self.reports.print_sales_report()

            elif choice == 5:
                term = input("Enter product name to search: ").strip().lower()
                self.reports.print_search(term)

            elif choice == 6:
                self.close_shop()
                break

            else:
                print("Invalid choice. Please choose 1 to 6.")

    def print_menu(self):
        """
        Displays the main menu.
        """
        print("\n===== MAIN MENU =====")
        print("1. View Stock")
        print("2. Add/Restock Product")
        print("3. Sell Product")
        print("4. View Sales Report")
        print("5. Search Products")
        print("6. Exit")

    def add_or_restock_product(self):
        """
        Adds a new product or restocks an existing one.
        """
        name = clean_text("Enter product name: ")

        if name == "":
            print("Product name cannot be empty.")
            return

        if self.inventory.contains(name):
            amount = get_positive_int("Enter quantity to add: ")
            self.inventory.restock(name, amount)
            print(f"Restocked {name}.")

        else:
            price = get_positive_int("Enter price: ")
            quantity = get_positive_int("Enter quantity: ")
            self.inventory.add_product(name, price, quantity)
            print(f"Added {name} to inventory.")

    def sell_product(self):
        """
        Sells a product if stock is available.
        """
        name = clean_text("Enter product to sell: ")

        if name == "":
            print("Product name cannot be empty.")
            return

        if not self.inventory.contains(name):
            print(f"{name} is not in inventory.")
            return

        quantity = get_positive_int("Enter quantity to sell: ")

        success, message, total = self.inventory.sell(name, quantity)

        if success:
            self.sales_log.add_sale(name, quantity, total)
            print(f"Sold {quantity} x {name} for KES {total}.")
        else:
            print(message)

    def close_shop(self):
        """
        Saves data and exits.
        """
        print("\nSaving data...")

        self.storage.save_inventory(self.inventory)
        self.storage.save_sales(self.sales_log)
        self.storage.save_alerts(self.inventory)

        print(f"Goodbye, {self.owner_name}!")