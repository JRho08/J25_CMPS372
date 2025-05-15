class Transaction:
    def __init__(self, inventory):
        self.inventory = inventory
        self.items = []

    def add_item_by_name(self, item_name):
        for item in self.inventory:
            if item["name"].lower() == item_name.lower():
                self.items.append(item)
                return True
        return False

    def calculate_total(self):
        return sum(item["price"] for item in self.items)

    def clear_items(self):
        self.items = []

    def display_items(self):
        print("Item Name\tPrice")
        for item in self.inventory:
            print(f"{item['name']}\t${item['price']}")


class Purchase(Transaction):
    def __init__(self, inventory, report):
        super().__init__(inventory)
        self.report = report

    def process(self):
        print("Which product would you like to purchase?")
        self.display_items()

        while True:
            item_name = input("Which item would you like to buy? ")
            if self.add_item_by_name(item_name):
                print("Item added.")
            else:
                print("Item not found.")
            cont = input("Anything else? (Y/N): ").lower()
            if cont != 'y':
                break

        total = self.calculate_total()
        print(f"Your Total is ${total}")
        print("Thank you for shopping at Target!")
        self.report.append(total)
        self.clear_items()


class Return(Transaction):
    def process(self):
        print("Which product would you like to return?")
        self.display_items()

        while True:
            item_name = input("Which item would you like to return? ")
            if self.add_item_by_name(item_name):
                print("Item added to return list.")
            else:
                print("Item not found.")
            cont = input("Anything else? (Y/N): ").lower()
            if cont != 'y':
                break

        total = self.calculate_total()
        print(f"Your Refund total is ${total}")
        print("Thank you for shopping at Target!")
        self.clear_items()


def manage_inventory(inventory):
    while True:
        print("\nManage Inventory")
        print("The following items are currently stored in the system:")
        print("Item Name\tPrice")
        for item in inventory:
            print(f"{item['name']}\t${item['price']}")

        print("\n1) Add New Item")
        print("2) Remove Item")
        print("3) Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Item Name: ")
            try:
                price = float(input("Item Price: "))
                inventory.append({"name": name, "price": price})
                print("Added Successfully!!")
            except ValueError:
                print("Invalid price!")
        elif choice == "2":
            name = input("Item Name to remove: ")
            found = False
            for item in inventory:
                if item["name"].lower() == name.lower():
                    inventory.remove(item)
                    found = True
                    print("Item Removed Successfully")
                    break
            if not found:
                print("Item Not Found! Please Try Again!")
        elif choice == "3":
            break
        else:
            print("Invalid option. Try again.")


def view_report(report):
    print("\nReports:")
    print(f"Total Customers: {len(report)}")
    print(f"Total Profit: ${sum(report)}")
    input("Click any key to go back to the main menu")


def main():
    inventory = [
        {"name": "Lego Star Wars", "price": 25},
        {"name": "Cookie", "price": 5}
    ]
    report = []

    while True:
        print("\nWelcome to Target! Choose the following options:")
        print("1) Make a Purchase")
        print("2) Make a Return")
        print("3) Manage Inventory")
        print("4) View Report")
        print("5) Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            purchase = Purchase(inventory, report)
            purchase.process()
        elif choice == "2":
            return_item = Return(inventory)
            return_item.process()
        elif choice == "3":
            manage_inventory(inventory)
        elif choice == "4":
            view_report(report)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()