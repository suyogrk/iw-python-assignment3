class Courses:
    def __init__(self):
        self.__name = 'EDUCEMY python course'
        self.__cost = 20000
        self.__time_in_weeks = 12
        self.__details = 'An introduction to computer science as a tool to solve ' \
                         'real-world analytical problems using Python'

    def cost(self):
        return self.__cost;

    def display_details(self):
        print(f"""
        Course Name: {self.__name}
        Course Time: {self.__time_in_weeks}
        Course Cost: {self.__cost}
        Course Description: {self.__details}                     
        """)
