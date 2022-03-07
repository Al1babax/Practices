def laskin(num1, num2, operator):
    if operator == "+":
        return num1+num2
    elif operator == "-":
        return num1-num2
    elif operator == "*":
        return num1*num2
    else:
        return "Operator is not valid."


print(laskin(2, 5, "+"))
print(laskin(2, 5, "-"))
print(laskin(2, 5, "*"))
