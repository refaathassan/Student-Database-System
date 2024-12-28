import traceback
import numpy as np

# Define a student class with initialization and methods for display and average grade calculation
class student:
    def __init__(self, name, age, grads):
        # Constructor to initialize student attributes: name, age, and grades
        self.name = name
        self.age = age
        self.grads = grads

    def display(self):
        # Method to display student information: name, age, and grades
        print("the name : ", self.name, "\nthe age : ", self.age, "\n the grad: ", self.grads)

    def avarage_grade(self):
        # Method to calculate and display the average grade of the student
        grads = self.grads
        print("the average grade is : ", np.sum(np.array(grads)) / len(grads))  # Uses numpy to sum the grades and compute the average

# Exception handling function to handle different types of errors
def exception_handling(ex):
    # Handling specific exceptions and prompting the user to retry the program
    if isinstance(ex, FileNotFoundError):
        print("please make sure you have a file to save")
        main_program()
    elif isinstance(ex, PermissionError):
        print("please make sure you have a permission to open and write in this file")
        main_program()
    elif isinstance(ex, IndexError):
        print("please make sure you chose a correct line index")
        main_program()
    elif isinstance(ex, ValueError):
        print("please make sure you enter an integer number as a choice")
        main_program()
    else:
        # Catch-all for any other exception
        main_program()

# Main function where the user input is taken and handled
def main_program():
    try:
        sub_list = []  # List to store the grades entered by the user
        name = input("please enter your name  : ")  # Get student's name
        age = int(input("enter your age:  "))  # Get student's age (convert to integer)
        sub_num = int(input("enter the number of subjects :  "))  # Get number of subjects
        for i in range(sub_num): 
            sub_list.append(int(input("enter the subject grade :  ")))  # Collect grades for each subject

        # Create an instance of the student class with the provided data
        stu = student(name, age, sub_list)

        # Infinite loop to keep asking the user for actions
        while True:
            # Ask the user to choose an action
            user_in = int(input("please enter the option:\n1-display info \n2-display average\n3-start from the beginning\nyour choice : "))
            
            # Use match-case to handle user choice
            match user_in:
                case 1:
                    stu.display()  # Display student information
                case 2:
                    stu.avarage_grade()  # Display the average grade
                case 3:
                    1 / 0  # Artificial error to simulate starting over (ZeroDivisionError)
                case _:
                    print("please enter a valid choice")  # Handle invalid choices

    # Catching any exceptions that may occur during the program execution
    except Exception:
        exception_handling(Exception)  # Call the exception handling function

# Start the main program
main_program()
