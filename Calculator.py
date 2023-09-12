import Test as T
import numpy as np
Name = T.FnameAndLname()
print(f"Welcome to MY ProJect Calculator ")
def Conditions(Condition,Number1,Number2):
    if Condition == "1":
        print("การบวก")
        Result = Number1 + Number2
    elif Condition == "2":
        Result = Number1 - Number2
        print("การลบ")
    elif Condition == "3":
        print("การคูณ")
        Result = Number1 * Number2
    elif Condition == "4":
        print("การหาร")
        Result = Number1 / Number2
    else:
        print("Please do it again ,We cannot Define what do you want?")
        Result = "Cannot Detect"
    Text = f"Your Result is  : {Result}"
    Value = False
    print(Text)
    return Result
BoolValue = True
while BoolValue == True:
    Condition = str(input("What do you want to do? \nplus = 1 negative = 2 mutiple = 3 divide = 4 :"))
    Number1 = float(input("Number 1 :"))
    Number2 = float(input("Number 2 :"))
    Conditions(Condition,Number1,Number2)
    Loop = str(input("Do you want to use again? 1 = Yes 2 = No : "))
    if Loop == "1":
        print("You choosed : Yes i do ")
        BoolValue = True
    else:
        print("You choosed : No i do")
        BoolValue = False
        User = T.UserName()
print("-------------------------------------------------------------------")