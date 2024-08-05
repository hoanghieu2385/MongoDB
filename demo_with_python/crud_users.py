from pymongo import MongoClient

print("Demo connect to MongoDB")

connection_string = "mongodb://localhost:27017/"
client = MongoClient(connection_string)
database_name = "T2308M"
collection_name = "users"

db = client[database_name]
collection = db[collection_name]

# if collection is None:
#     print("Cannot connect")
# else:
#     print("Connected successfully")
#     for user in collection.find():
#         print("")
#         print(user["username"])
#         print(user["fullname"])

def menu():
    while(True):
        print("\n======== Menu ========")
        # print("1. Add User")
        # print("2. Update User")
        # print("3. Delete User")
        
        print("1. Add Many User")
        print("3. Delete Many User")
        print("2. Update Many User")
        print("4. Show All User")
        
        choice = input ("\nEnter a number: ")
        # if choice == "1":
        #     username = input("Enter Username: ")
        #     fullname = input("Enter Fullname: ")
        #     addUser(username, fullname)

        # elif choice == "2":
        #     username = input("Enter Username: ")
        #     newFullName = input("Enter New Fullname: ")
        #     updateUser(username, newFullName)
            
        # elif choice == "3":
        #     username = input("Enter Username: ")
        #     deleteUser(username)
            
        if choice == "1": 
            users = []
            for manyUser in range(3):
                username = input("Enter Username: ")
                fullname = input("Enter Fullname: ")
                users.append(
                    {"username": username,
                    "fullname": fullname }
                )
            addUsers(users)
            
        elif choice == "2":
            users = []
            for updateManyUser in range(2):
                username = input("Enter Username: ")
                if collection is not None:
                    condition_user = {"username":username}
                    newFullName = input("Enter New Fullname: ")
                    newFullName = {"$set":{"fullname":newFullName}}
                    users.append(
                        {"username": condition_user,
                        "fullname": newFullName}
                    )
            updateUsers(users)
            
        elif choice == "3":
            users = []
            for deleteManyUser in range(2):
                username3 = input("Enter Username: ")
                users.append(
                    {"username": username3}
                )
            deleteUsers(users)
        
        elif choice == "4":
            showAllUser()
            
        else:
            print("Invalid input")

### One CRUD ###
# def addUser(username, fullname):
#     print("Add User Method")
#     user = {"username":username, "fullname":fullname}
#     collection.insert_one(user)
#     print("User Added.")

# def updateUser(username, newFullName):
#     condition_user = {"username":username}
#     newFullName = {"$set":{"fullname":newFullName}}
#     collection.update_one(condition_user, newFullName)
#     print("\nUser Updated.")    

# def deleteUser(username):
#     if collection is not None:
#         condition_user = {"username":username}
#         collection.delete_one(condition_user)
#         print("\nUser Deleted.")

### Many CRUD ###
def addUsers(users):
    # print("Many insert")
    collection.insert_many(users)
    print("Users Added")
    
def updateUsers(users):
    filter_list = [{"username": user["username"]} for user in users]
    update = {"$set": {"fullname": users[0]["fullname"]["$set"]["fullname"]}}
    collection.update_many({"$or": filter_list}, update)
    print("\nUsers Updated")

    
def deleteUsers(users):
    filter_list = [{"username": user["username"]} for user in users]
    collection.delete_many({"$or": filter_list})
    print("\nUsers Deleted")

def showAllUser():
    if collection is None:
        print("Cannot connect")
    else:
        print("Connected successfully")
        for user in collection.find():
            print(user["username"])
            print(user["fullname"])

if __name__ == "__main__":
    menu()