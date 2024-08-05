from pymongo import MongoClient

# MongoDB Cloud connection
connection_string = "mongodb+srv://hoanghieu:Minhhieu2382005@t2308m.rkvnzot.mongodb.net/"
try:
    client = MongoClient(connection_string)
    database_name = "sample_mflix"
    collection_name1 = "users"
    collection_name2 = "movies"

    db = client[database_name]
    collection_user = db[collection_name1]
    collection_movies = db[collection_name2]

    if collection_user is None:
        print("Cannot connect")
    else:
        print("Connected successfully")
except Exception as e:
    print("Error connecting to MongoDB:", e)

### Match User function ###
def demo_match(email):
    match_query = {"$match": {"email": email}}
    pipline = [match_query]
    results = collection_user.aggregate(pipline)
    for users in results:
        # print("Email: " + users["email"])
        print("Name: " + users["name"])
        print("Password: " + users["password"])

def demo_group(type):
    match_query = {"$match": {"type": type}}
    group_query = {"$group":
        {"_id": "$type",
        "movie_count": {"$sum": 1}}
        }
    pipline = [match_query, group_query]
    results = collection_movies.aggregate(pipline)
    
    # for movie_count in results:
    #     print(movie_count)
    
    count = 0
    for result in results:
        print(f"\n{type} has {result['movie_count']} movies")
        count += 1
    
    if count == 0:
        print(f"\nNo movies found for type: {type}")
        

### Menu function ###
def menu():
    while True:
        print("\n======== Menu ========")
        print("1. Match User")
        print("2. Group Type")

        choice = input("\nEnter a number: ")
        if choice == "1":
            email = input("Enter email: ")
            demo_match(email)

        elif choice == "2":
            type = input("Enter type: ")
            demo_group(type)



        else:
            print("Invalid choice")
        
if __name__ == "__main__":
    menu()