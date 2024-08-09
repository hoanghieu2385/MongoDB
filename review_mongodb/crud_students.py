from pymongo import MongoClient

# MongoDB connection
connection_string = "mongodb://localhost:27017"
try:
    client = MongoClient(connection_string)
    database_name = "T2308M"
    collection_name = "students"

    db = client[database_name]
    collection = db[collection_name]

    if collection is None:
        print("Cannot connect")
    else:
        print("Connected successfully")
except Exception as e:
    print("Error connecting to MongoDB:", e)
    
# Menu function
def menu():
    while True:
        print("\n======== Menu ========")
        print("1. Add a new student")
        print("2. Find student by ID")
        print("3. Update student by ID")
        print("4. Delete student by ID")
        print("5. Show all students")
        
        choice = input("\nEnter your choice: ")
        if choice == "1":
            addStudent()
            
        elif choice == "2":
            findStudentByID()
            
        elif choice == "5":
            showAll()
            
        else:
            print("Invalid choice, please try again.")
        

# def addStudent():
#     student_id = input("Enter student ID: ")
#     student_name = input("Enter student name: ")
#     class_id =  input("Enter class ID: ")
#     class_name = input("Enter class name: ")
    
#     subject = []
#     while True:
#         subject_name = input("Enter subject name: ")
#         subject.append({"name": subject_name})
#         choice = input("Do you want to add another subject? (y/n): ")
#         if choice.lower() != "y":
#             break

#     student_info = {
#         "student_id": student_id,
#         "student_name": student_name,
#         "class": {
#             "class_id": class_id,
#             "class_name": class_name
#         },
#         "subject": subject
#     }
    
#     collection.insert_one(student_info)
#     print("Student added successfully!")
    
# # def findStudentByID():
# #     id_input = input("Enter student ID: ")
# #     student = collection.find_one({"student_id": id_input})
# #     if student:
# #         print("\nStudent found:")
# #         print(f"ID: {student['student_id']}")
# #         print(f"Name: {student['student_name']}")
# #         print(f"Class:")
# #         print(f"- Class ID: {student['class']['class_id']}")
# #         print(f"- Class name: {student['class']['class_name']}")
# #         print(f"Subjects:")
# #         for subject in student['subject']:
# #             print(f"- {subject['name']}")
# #     else:
# #         print("Student not found")

# def findStudentByID():
#     id_input = input("Enter student ID: ")
#     match_query = {"$match": {"student_id": id_input}}
#     pipline = [match_query]
#     results = collection.aggregate(pipline)

#     if results:
#         print("\nStudent found:")
#         for student in results:
#             print(f"ID: {student['student_id']}")
#             print(f"Name: {student['student_name']}")
#             print(f"Class:")
#             print(f"\t- Class ID: {student['class']['class_id']}")
#             print(f"\t- Class name: {student['class']['class_name']}")
#             print(f"Subjects:")
#             for sub in student['subject']:
#                 print(f"\t- {sub['name']}")
#     else:
#         print("Student not found")
    
# def updateStudentByID():
#     id_input = input("Enter student ID: ")
#     student = collection.find_one({"student_id": id_input})
#     if student:
#         print("\nStudent found:")
#         print(f"ID: {student['student_id']}")
#         print(f"Name: {student['student_name']}")
#         print(f"Class:")
#         print(f"- Class ID: {student['class']['class_id']}")
#         print(f"- Class name: {student['class']['class_name']}")
#         print(f"Subjects:")
#         for subject in student['subject']:
#             print(f"- {subject['name']}")
            
#         choice = input("\nDo you want to update this student? (y/n): ")
#         if choice.lower() == "y":
#             student_name = input("Enter updated student name: ")
#             class_id =  input("Enter updated class ID: ")
#             class_name = input("Enter updated class name: ")
#             collection.update_one({"student_id": id_input}, {"$set": {"student_name": student_name, "class.class_id": class_id, "class.class_name": class_name}})
#             print("Student updated successfully!")

# def deleteStudentByID():
#     id_input = input("Enter student ID: ")
#     collection.delete_one({"student_id": id_input})
#     print("Student deleted successfully!")

# def showAll():
#     for student in collection.find():
#         print("ID: ", student["student_id"])
#         print("Name: ", student["student_name"])
#         print("Class: ")
#         print("\t- Class ID: ", student["class"]["class_id"])
#         print("\t- Class name: ", student["class"]["class_name"])
#         print("Subjects: ")
#         for sub in student["subject"]:
#             print("\t- ", sub["name"])
        
def addManyStudents():
    student = []

    while True:
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        class_id = input("Enter class ID: ")
        class_name = input("Enter class name: ")
        subject = []
        while True:
            subject_name = input("Enter subject name: ")
            subject.append({"name": subject_name})
            choice = input("Do you want to add another subject? (y/n): ")
            if choice.lower() != "y":
                break
        student.append({"student_id": student_id,
                        "student_name": student_name,
                        "class": {"class_id": class_id,
                                    "class_name": class_name},
                        "subject": subject})
        choice = input("Do you want to add another student? (y/n): ")
        if choice.lower() != "y":
            break
        
def deleteManyStudents():
    while True:
        student_id = input("Enter student ID: ")
        collection.delete_many({"student_id": student_id})
        choice = input("Do you want to delete another student? (y/n): ")
        if choice.lower() != "y":
            break
        
def showAll():
    for student in collection.find():
        print("ID: ", student["student_id"])
        print("Name: ", student["student_name"])
        print("Class: ")
        print("\t- Class ID: ", student["class"]["class_id"])
        print("\t- Class name: ", student["class"]["class_name"])
        print("Subjects: ")
        for sub in student["subject"]:
            print("\t- ", sub["name"])

if __name__ == "__main__":
    menu()