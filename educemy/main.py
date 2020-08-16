import sys
from courses import Courses
from students import Students
from functions import Functions

def main():
    course = Courses()
    students = Students()
    finish_operation = False
    while not finish_operation:
        print("""
        Welcome To EDUCEMY
        What would you like to do
        
        1. View Courses
        2. Enroll in course
        3. Display all students
        4. Display student information
        5. Update Student Information
        6. Delete Student Information
        7. Complete course for student
        8. Clear Display
        9. Exit Application 
        """)

        main_prompt = input('What would you like to do?')

        if main_prompt == '1':
            course.display_details()
        elif main_prompt == '2':
            students.enroll_student()
        elif main_prompt == '3':
            students.display_all_student_details()
        elif main_prompt == '4':
            students.display_student_information()
            pass
        elif main_prompt == '5':
            students.update_student_information()
            pass
        elif main_prompt == '6':
            pass
        elif main_prompt == '7':
            pass
        elif main_prompt == '8':
            Functions.clear()
        elif main_prompt == '9':
            sys.exit()
        else:
            print(f"""ERROR:\nInput must be in range 1-7""")
            continue

        finish_prompt = input('Would you like to perform more operations?(y/n)')
        if finish_prompt in ['n', 'N']:
            finish_operation = True
            Functions.clear()
            print("""
            Thank You for Visiting EDUCEMY.
            Have a good day
            """)

if __name__ == '__main__':
    main()
