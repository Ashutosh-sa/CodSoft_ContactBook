# Contact Management System

# Data Storage
contacts = []


# User Interface Functions
def add_contact():
  name = input("Enter name: ")
  phone = input("Enter phone number: ")
  email = input("Enter email: ")
  address = input("Enter address: ")
  contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
  contacts.append(contact)
  print("Contact added successfully!")


def view_contacts():
  print("\nContact List:")
  for i, contact in enumerate(contacts, start=1):
    print(f"{i}. Name: {contact['Name']}, Phone: {contact['Phone']}")


def search_contact():
  query = input("Enter a name or phone number to search: ")
  found = False
  for contact in contacts:
    if query.lower() in contact['Name'].lower() or query in contact['Phone']:
      print(
          f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}, Address: {contact['Address']}"
      )
      found = True
  if not found:
    print("Contact not found.")


def update_contact():
  query = input("Enter the name or phone number of the contact to update: ")
  found = False
  for contact in contacts:
    if query.lower() in contact['Name'].lower() or query in contact['Phone']:
      contact['Name'] = input("Enter new name: ")
      contact['Phone'] = input("Enter new phone number: ")
      contact['Email'] = input("Enter new email: ")
      contact['Address'] = input("Enter new address: ")
      print("Contact updated successfully!")
      found = True
  if not found:
    print("Contact not found.")


def delete_contact():
  query = input("Enter the name or phone number of the contact to delete: ")
  found = False
  for contact in contacts:
    if query.lower() in contact['Name'].lower() or query in contact['Phone']:
      contacts.remove(contact)
      print("Contact deleted successfully!")
      found = True
  if not found:
    print("Contact not found.")


# Main Program
while True:
  print("\nContact Management System")
  print("1. Add Contact")
  print("2. View Contact List")
  print("3. Search Contact")
  print("4. Update Contact")
  print("5. Delete Contact")
  print("6. Exit")

  choice = input("Enter your choice (1/2/3/4/5/6): ")

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
    print("Exiting the Contact Management System. Goodbye!")
    break
  else:
    print("Invalid choice. Please enter a valid option.")
