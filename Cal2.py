number = 0
symbol = ""
total = 0
while number != 0 or symbol != "=":
    number = 0
    symbol = ""
    symbol = str(input("Enter your symbol (+,-,*,/) :"))
    number = int(input("Enter number : "))
    if symbol == "+":
        total += number
    elif symbol == "-":
        total -= number
    elif symbol == "*":
        total *= number
    elif symbol == "/":
        total /= number
    print(number)