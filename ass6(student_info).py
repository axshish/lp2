print("-----Student Information Program-----")

student_records = {}

def add_student():
    num_records = int(input('How many student records do you want to store? '))
    for _ in range(num_records):
        first_name, last_name = input("Enter the student's first and last name: ").split()
        contact_number = input("Enter contact number: ")
        marks = input('Enter Marks: ')
        student_records[(first_name, last_name)] = (contact_number, marks)

def sort_students():
    sorted_names = sorted(student_records.keys(), key=lambda x: (x[0], x[1]))
    for first_name, last_name in sorted_names:
        print(first_name, last_name)

def find_minimum_marks():
    all_marks = [details[1] for _, details in student_records.items()]
    min_marks = min(all_marks)
    print("Minimum marks:", min_marks)

def find_maximum_marks():
    all_marks = [details[1] for _, details in student_records.items()]
    max_marks = max(all_marks)
    print("Maximum marks:", max_marks)

def search_contact_number():
    search_name = input('Enter the first name of the student: ')
    for first_name, last_name in student_records:
        if first_name == search_name:
            print("Contact number:", student_records[first_name, last_name][0])
            break
    else:
        print("Student not found.")

def main():
    while True:
        print('Choose an operation: ')
        print('1: Sort students by name')
        print('2: Find minimum marks')
        print('3: Find maximum marks')
        print('4: Search contact number using first name')
        print('5: Exit')
        
        choice = input('Option: ')
        
        if choice == '1':
            sort_students()
        elif choice == '2':
            find_minimum_marks()
        elif choice == '3':
            find_maximum_marks()
        elif choice == '4':
            search_contact_number()
        elif choice == '5':
            print('Thank you for using the program!')
            break
        else:
            print('Invalid choice. Please choose again.')

if __name__ == "__main__":
    add_student()
    main()
