Symbol = ""
total = 0
count = 0
while Symbol != "=":
    print(float(total))
    number = float(input("Enter your number : "))
    Symbol = input("Enter your Symbol \n + : plus, - : miner, / : divide, * : mutiply,% : module, = : equal : ")
    if count == 0:
        if Symbol == "/":
            total = number**2
        elif Symbol == "*":
            total = 1
        else :
            total = 0
    if Symbol == "+":
        total = total + number
    elif Symbol == "-":
        total = total - number 
    elif Symbol == "/":
        total = total / number
    elif Symbol == "*":
        total = total * number
    elif Symbol == "%":
        total = total % number
    count += 1