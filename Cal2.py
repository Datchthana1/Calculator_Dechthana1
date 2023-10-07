ButtonEqual = False
count = 1
numberlist = [0]
while ButtonEqual != True:
    number = int(input("Enter your number : "))
    if count == 1:
        pass
    else:
        numberlist.append(number)
    condition = str(input("Enter you condition +:plus -:miner *:mutiple /:divide =:equal : "))
    if condition == "+":
        for i in numberlist:
            number = number + i
    elif condition == "-":
        for i in numberlist:
            number -= i
    elif condition == "*":
        for i in numberlist:
            number -= i
    elif condition == "/":
        for i in numberlist:
            number -= i
    elif condition == "=":
        ButtonEqual = True
    count += 1
    print(number)

## ยังไม่เสร็จ 
##Calculator can excuted more 2 number