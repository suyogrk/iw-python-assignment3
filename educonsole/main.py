import sys
from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def main():
    finish_operation = False
    while not finish_operation:
        print("""
        Welcome To EDUCEMY
        What would you like to do
        
        1. View Courses
        2. Enroll in course
        3. Display your information
        4. Update your information
        5. Leave the course
        6. Mark Course as completed
        7. Exit Application 
        """)

        main_prompt = input('What would you like to do?')

        if main_prompt == '1':
            pass
        elif main_prompt == '2':
            pass
        elif main_prompt == '3':
            pass
        elif main_prompt == '4':
            pass
        elif main_prompt == '5':
            pass
        elif main_prompt == '6':
            pass
        elif main_prompt == '7':
            sys.exit()
        else:
            clear()
            print(f"""ERROR:\nInput must be in range 1-7""")
            continue

        finish_prompt = input('Would you like to perform more operations?(y/n)')
        if finish_prompt in ['n', 'N']:
            finish_operation = True;
            clear()
            print("""
            Thank You for Visiting EDUCEMY.
            Have a good day
            """)

if __name__ == '__main__':
    main()
