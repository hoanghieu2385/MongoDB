from pymongo import MongoClient

# MongoDB connection
connection_string = "mongodb://localhost:27017"
try:
    client = MongoClient(connection_string)
    database_name = "T2308M"
    collection_name = "products"

    db = client[database_name]
    collection = db[collection_name]

    if collection is None:
        print("Cannot connect")
    else:
        print("Connected successfully")
except Exception as e:
    print("Error connecting to MongoDB:", e)

# Menu function
def Menu():
    while True:
        print("\n======== Menu ========")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. Show All Product")

        choice = input("\nEnter a number: ")
        if choice == "1":
            name = input("Enter name product: ")
            price = input("Enter price product: ")
            addProduct(name, price)
        elif choice == "2":
            showAllProduct()
            name = input("Enter name product: ")
            newPrice = input("Enter new price product: ")
            updatePriceProduct(name, newPrice)
        elif choice == "3":
            name = input("Enter name product want to delete: ")
            deleteProduct(name)
        elif choice == "4":
            showAllProduct()
        else:
            print("Invalid choice")

# Add product function
def addProduct(name, price):
    try:
        price = float(price)
        product = {"name": name, "price": price}
        collection.insert_one(product)
        print("\nProduct Added.")
        showAllProduct()
    except ValueError:
        print("Invalid price format. Please enter a valid number.")

# Update product price function
def updatePriceProduct(name, newPrice):
    try:
        newPrice = float(newPrice)
        condition_product = {"name": name}
        newPrice = {"$set": {"price": newPrice}}
        collection.update_one(condition_product, newPrice)
        print("\nProduct Updated.")
        showAllProduct()
    except ValueError:
        print("Invalid price format. Please enter a valid number.")

# Delete product function
def deleteProduct(name):
    if collection is not None:
        condition_product = {"name": name}
        collection.delete_one(condition_product)
        print("\nProduct Deleted.")
        showAllProduct()

# Show all products function
def showAllProduct():
    for product in collection.find():
        print("Name:", product["name"], ", Price:", str(product["price"]))

if __name__ == "__main__":
    Menu()
