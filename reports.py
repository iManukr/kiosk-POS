class Reports:
    def __init__(self, inventory, sales_log):
        self.inventory = inventory
        self.sales_log = sales_log

    def print_stock(self):
        """
        Prints all products in aligned columns.
        """
        print("\n--- CURRENT STOCK ---")
        print(f"{'ITEM':<15} | {'PRICE':<10} | {'QUANTITY':<10}")
        print("-" * 40)

        if len(self.inventory.products) == 0:
            print("No products in stock.")
        else:
            for product in self.inventory.products.values():
                print(
                    f"{product.name:<15} | "
                    f"KES {product.price:<6} | "
                    f"{product.quantity:<10}"
                )

        print("------------------------\n")

    def print_sales_report(self):
        """
        Prints all sales, total revenue, unique products, and best seller.
        """
        print("\n--- SALES REPORT ---")

        if self.sales_log.is_empty():
            print("No sales made today yet.")
            return

        for sale in self.sales_log.sales:
            item = sale[0]
            quantity = sale[1]
            total = sale[2]

            print(f"Sold {quantity} x {item} = KES {total}")

        total_revenue = self.sales_log.total_revenue()
        unique_count = len(self.sales_log.unique_products)
        best_item, best_quantity = self.sales_log.best_seller()

        print("-" * 30)
        print(f"TOTAL REVENUE: KES {total_revenue}")
        print(f"UNIQUE PRODUCTS SOLD: {unique_count}")
        print(f"BEST SELLER: {best_item} ({best_quantity} sold)")
        print("------------------------\n")

    def print_search(self, term):
        """
        Prints search results.
        """
        results = self.inventory.search(term)

        print(f"\n--- SEARCH RESULTS FOR '{term}' ---")

        if len(results) == 0:
            print("No matches found.")
        else:
            for product in results:
                print(
                    f"{product.name}: "
                    f"KES {product.price}, "
                    f"Quantity: {product.quantity}"
                )

        print("------------------------\n")