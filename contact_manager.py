
# Contact Manager - Simple Dictionary-Based Implementation

# Dictionary to store contacts
contacts = {}

def add_contact():
    """Adds a new contact to the dictionary."""
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number (10 digits): ").strip()

    if not name or not phone.isdigit() or len(phone) != 10:
        print("Invalid input! Please enter a valid name and 10-digit phone number.")
        return

    if name in contacts:
        print("Contact already exists!")
    else:
        contacts[name] = phone
        print(f"Contact '{name}' added successfully!")

def view_contacts():
    """Displays all saved contacts."""
    if not contacts:
        print("No contacts available!")
        return

    print("\nContact List:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def search_contact():
    """Searches for a contact by name."""
    name = input("Enter the name to search: ").strip()
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found!")

def update_contact():
    """Updates an existing contact (name or phone number)."""
    old_name = input("Enter the contact name to update: ").strip()

    if old_name in contacts:
        new_name = input("Enter the new name (press Enter to keep the same): ").strip()
        new_phone = input("Enter new phone number (10 digits, press Enter to keep the same): ").strip()

        if new_phone and (not new_phone.isdigit() or len(new_phone) != 10):
            print("Invalid phone number! Must be 10 digits.")
            return

        # Update name if provided
        if new_name and new_name != old_name:
            contacts[new_name] = contacts.pop(old_name)  # Rename key
            old_name = new_name  # Update reference

        # Update phone number if provided
        if new_phone:
            contacts[old_name] = new_phone

        print(f"Contact '{old_name}' updated successfully!")
    else:
        print("Contact not found!")

def delete_contact():
    """Deletes a contact by name (1 number = 1 name)."""
    if not contacts:
        print("No contacts available to delete!")
        return
    
    name_to_delete = input("Enter name of contact to delete: ").strip()
    
    # Find the contact (case-insensitive)
    phone_to_delete = None
    for phone, name in contacts.items():
        if name.lower() == name_to_delete.lower():
            phone_to_delete = phone
            break
    
    if not phone_to_delete:
        print(f"No contact found with name '{name_to_delete}'")
        return
    
    # Delete the contact
    del contacts[phone_to_delete]
    print(f"Contact '{name_to_delete}' deleted successfully!")

def userChoice(choice):
    """Handles user input and calls the appropriate function."""
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")


if __name__ == '__main__':
    while True:
        print("\n📞 Contact Manager Menu:")
        print("1. Add a Contact")
        print("2. View Contacts")
        print("3. Search for a Contact")
        print("4. Update a Contact")
        print("5. Delete a Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        userChoice(choice)
