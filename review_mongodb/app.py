from random import choice
from pymongo import MongoClient

# MongoDB connection
connection_string = "mongodb://localhost:27017"
try:
    client = MongoClient(connection_string)
    database_name = "T2308M"
    collection_name = "role"

    db = client[database_name]
    collection = db[collection_name]

    if collection is None:
        print("Cannot connect")
    else:
        print("Connected successfully")
except Exception as e:
    print("Error connecting to MongoDB:", e)

# Add role function
def addRole():
    id = input("Enter id: ")
    role_name = input("Enter name: ")
    is_active = True
    collection.insert_one({"id": id,
                            "name": role_name,
                            "is_active": is_active})
    print(f"\nNew role: {role_name} Added.")

def editRoleName(id):
    condition = {"id": id}
    new_value = input("Enter new name: ")
    collection.update_one(condition, {"$set": {"name": new_value}})
    
def deleteRole(id):
    showAll()
    collection.delete_one({"id": id})
    print("\nRole Deleted.")
    
def showAll():
    for role in collection.find():
        print(
            "id: " + role["id"] + ", ",
            "Name: " + role["name"] + ", ",
            "Active: " + str(role["is_active"]),
        )

# Menu function
def Menu():
    while True:
        print("\n======== Menu ========")
        print("1. Add Role")
        print("2. Edit Role Name")
        print("3. Delete Role")
        print("4. Show All")
        
        choice = input("\nPlease enter a number: ")
        if choice == "1":
            showAll()
            addRole()
        
        elif choice == "2":
            showAll()
            id = input("\nEnter id: ")
            editRoleName(id)
        
        elif choice == "3":
            showAll()
            id = input("\nEnter id: ")
            deleteRole(id)
        
        elif choice == "4":
            showAll()
        
        else:
            print("Invalid choice. Please try again.")  
if __name__ == "__main__":
    Menu()