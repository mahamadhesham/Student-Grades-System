def show_menu():
    print("1. Add student")
    print("2. Show student")
    print("3. Search student")
    print("4. Calculate Average")
    print("5. Exit")
def Add_student(name,grade):
    file=open("grades.txt", "a")
    file.write(name +":"+ grade + "\n")
    file.close()
    return "Student Added"
def Show_student():
    file=open("grades.txt", "r")
    content=file.read()
    file.close()
    return content
def Search_student(word):
    file=open("grades.txt", "r")
    content=file.read()
    file.close()
    if word in content:
        return "Found"
    else:
        return "Not found"
def calculate_Average():
    file=open("grades.txt", "r")
    lines=file.readlines()
    total=0
    count=0
    for line in lines:
        parts=line.strip().split(":")
        amount=float(parts[1])
        total=total+amount
        count=count+1
    file.close()
    average=total/count
    return average
operations={
    "1": Add_student,
    "2":Show_student,
    "3":Search_student,
    "4":calculate_Average
}
def main():
    while True:
        show_menu()
        choice=input("Choose: ")
        if choice=="5":
            print("Goodbye")
            break
        if choice not in operations:
            print("Invalid choice")
            break
        if choice =="1":
            name=input("Enter name: ")
            grade=input("Enter grade: ")
            result=operations[choice](name,grade)
            print(result)
        elif choice=="2":
           result=operations[choice]()
           print(result)
        elif choice=="3":
            word=input("Enter word: ")
            result=operations[choice](word)
            print(result)
        elif choice=="4":
            result=operations[choice]()
            print(result)
main()