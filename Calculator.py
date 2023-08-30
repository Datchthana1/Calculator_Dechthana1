import Test as T
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
        print("โปรดเลือกอีกครั้ง เนื่องจากไม่สามารถระบุตัวแปรได้")
        Result = "Cannot Detect"
    Text = f"ผลลัพท์ของคุณคือ : {Result}"
    Value = False
    print(Text)
    return Result
BoolValue = True
while BoolValue == True:
    Condition = str(input("ต้องการใช้คำสั่งใด การบวก = 1 การลบ = 2 การคูณ = 3 การหาร = 4 :"))
    Number1 = float(input("หมายเลขที่ 1 :"))
    Number2 = float(input("หมายเลขที่ 2 :"))
    Conditions(Condition,Number1,Number2)
    Loop = str(input("คุณต้องการใช้เครื่องคิดเลขอีกหรือไม่ 1 = ต้องการ 2 = ไม่ต้องการ : "))
    if Loop == "1":
        print("การเลือกของคุณคือ : ต้องการทำซ้ำ")
        BoolValue = True
    else:
        print("การเลือกของคุณคือ : ไม่ต้องการทำซ้ำ")
        BoolValue = False
        User = T.UserName()
print("-------------------------------------------------------------------")