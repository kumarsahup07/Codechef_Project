import csv
inventory = {}
# Inventory dictionary to store products (product_name: [quantity, price])
def load_inventory():
    """Load inventory from CSV file into the dictionary."""
    try:
        with open("inventory.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["Product Name"]
                quantity = int(row["Quantity"])
                price = float(row["Price"])
                inventory[name] = [quantity, price]
        print("Inventory loaded successfully.\n")
    except FileNotFoundError:
        print("No existing inventory file found. Starting with empty inventory.\n")

def save_inventory():
    """Save the current inventory to a CSV file."""
    with open("inventory.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Product Name", "Quantity", "Price"])
        for name, details in inventory.items():
            writer.writerow([name, details[0], details[1]])
    print("Inventory saved to inventory.csv\n")

def add_product():
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))
    
    if name in inventory:
        inventory[name][0] += quantity  # Update quantity if product exists
    else:
        inventory[name] = [quantity, price]
    
    print(f"Product '{name}' added successfully!\n")

def view_inventory():
    if not inventory:
        print("Inventory is empty.\n")
        return
    print("Current Inventory:")
    print("Name\tQuantity\tPrice")
    for name, details in inventory.items():
        print(f"{name}\t{details[0]}\t${details[1]:.2f}")
    print()

def update_product():
    name = input("Enter product name to update: ")
    if name in inventory:
        quantity = int(input("Enter new quantity: "))
        inventory[name][0] = quantity
        print(f"Updated '{name}' stock to {quantity}\n")
    else:
        print("Product not found!\n")

def delete_product():
    name = input("Enter product name to delete: ")
    if name in inventory:
        del inventory[name]
        print(f"Deleted '{name}' from inventory\n")
    else:
        print("Product not found!\n")

def search_product():
    name = input("Enter product name to search: ")
    if name in inventory:
        quantity, price = inventory[name]
        print(f"{name}: Quantity = {quantity}, Price = ${price:.2f}\n")
    else:
        print("Product not found!\n")

def main():
    load_inventory()

    while True:
        print("Inventory Management System")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Update Stock")
        print("4. Delete Product")
        print("5. Search Product")
        print("6. Save & Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_product()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            update_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            search_product()
        elif choice == "6":
            save_inventory()
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()