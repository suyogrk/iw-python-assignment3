import csv
from functions import Functions

class Students:

    def __init__(self):
        self.__students_list = []
        self.__deposit_required = 20000
        self.__pay_per_installment = 10000
        f = open("students.csv", "r")
        with f as student_file:
            reader = csv.DictReader(student_file)
            for row in reader:
                self.__students_list.append(row)
            pass

    def enroll_student(self):
        Functions.clear()
        print("Welcome to EDUCEMY Student Enrollment System")
        name = input("Enter student name: ")
        email = input("Enter student email: ")
        age = input("Enter student age: ")

        print(f"""
        How many installments have been paid?
        1. 1 installment of 10000
        2. 2 installments of 20000
        """)
        num_of_installments = 0
        while True:
            try:
                num_of_installments = int(input("Enter number of installments: "))
            except:
                print("Please enter a number")
                continue

            while num_of_installments not in [1,2]:
                print("Number of installments can only be 1 or 2")
                continue

            print(f"{num_of_installments} installments have been paid.")
            break
        student_dict = self.generate_student_dict(name, email, age, num_of_installments)
        self.__students_list.append(student_dict)
        self.save_data()

    def display_all_student_details(self):
        format = "{:<5} {:<15} {:15} {:5} {:25} {:20} {:20} {:15} {:15} {:5}"
        print(format.format("Id", "Name", "Email","Age", "Installment Amount", "Total paid", "Installment due", "Total due", "Total returned", "Status"))
        for student in self.__students_list:
            id, name, email, age, install_amt, total_paid, install_due, total_due, total_returned, status = student.values()
            print(format.format(id, name, email, age, install_amt, total_paid, install_due, total_due, total_returned, status))

    def display_student_information(self):
        search_id = input("Enter Id of student")
        student_index = self.find_student_by_id(search_id)
        if student_index is None:
            print("Student not found")
        else:
            student = self.__students_list[student_index]
            self.print_student_details(student)

    def print_student_details(self, student):
        print(f"""
        Name: {student['name']}
        Email: {student['email']}
        Age: {student['age']}
        Total Paid: {student['total_paid']}
        Installment Due: {student['installment_due']}
        Total Due: {student['total_due']}
        Total Returned: {student['total_returned']}
        Course status: {student['status']}
        """)

    def find_student_by_id(self, search_id):
        for i in range(len(self.__students_list)):
            if(search_id == self.__students_list[i]['id']):
                return i
        return None

    def update_student_information(self):
        pass

    def leave_course(self):
        pass

    def complete_course(self):
        pass

    def generate_student_dict(self, name, email, age, num_of_installments):
        id = self.generate_student_id()
        installment_paid = num_of_installments * self.__pay_per_installment
        installment_due = 2 - num_of_installments
        total_due = installment_due * self.__pay_per_installment
        status = "incomplete"

        return {
            'id': id,
            'name': name,
            'email': email,
            'age': age,
            'installment_amt': self.__pay_per_installment,
            'total_paid': installment_paid,
            'installment_due': installment_due,
            'total_due': total_due,
            'total_returned': 0,
            'status': status
        }

    def generate_student_id(self):
        try:
            previous_id = int(self.__students_list[-1]["id"])
            print(previous_id)
        except:
            previous_id = len(self.__students_list)

        return previous_id + 1


    def save_data(self):
        with open("students.csv", "w") as students_file:
            fieldnames = ['id', 'name', 'email', 'age', 'installment_amt', 'total_paid', 'installment_due', 'total_due','total_returned','status']
            writer = csv.DictWriter(students_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.__students_list)
