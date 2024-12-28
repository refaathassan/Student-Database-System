import traceback
import numpy as np
class student:
    def __init__(self,name,age,grads):
        self.name=name
        self.age=age
        self.grads=grads
    def display(self):
        print("the name : ",self.name,"\nthe age : ",self.age,"\n the grad: ",self.grads)
    def avarage_grade(self):
        grads=self.grads
        print("the avarege grade is : ",np.sum(np.array(grads))/len(grads))

def exception_handling(ex):
    if isinstance(ex,FileNotFoundError):
        print("please make sure you have a file to save")
        main_program()
    elif isinstance(ex,PermissionError):
        print("please make sure you have a permission to open and write in this file")
        main_program()
    elif isinstance(ex,IndexError):
        print("please make sure you choised a correct line index")
        main_program()
    elif isinstance(ex,ValueError):
        print("please make sure you enter a integar number as a choice")
        main_program()
    else:
        main_program()

def main_program():
    
    try:
            sub_list=[]
            name=input("please enter the your name  : ")
            age=int(input("enter your age:  "))
            sub_num=int(input("enter the number of subjects :  "))
            for i in range(sub_num): sub_list.append(int(input("enter the subject grade :  ")))
            stu=student(name,age,sub_list)
            while True:
                user_in=int(input("please enter the option:\n1-display info \n2-display avarege\n3-start from the beginning\nyour choice : "))
                match user_in:
                    case 1: 
                        stu.display()
                    case 2: stu.avarage_grade() 
                    case 3: 1/0
                    case _: print("please enter a valid choise")
    except Exception:
            exception_handling(Exception)

main_program()