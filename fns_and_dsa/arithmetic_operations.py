def perform_operation(num1, num2, operation):
    if string in ["add", "subtract", 'multiply', "divide"]:
        if string == 'divide' and num2 == 0:
            return "Can't perfom division by Zero"
        else:
            if string == "add":
                return num1 + num2
            elif string == "subtract":
                return num1 - num2
            elif string == "multiply":
                return num1 * num2
            elif string == 'divide':
                return num1 / num2
    else:
        return "Operation cant be handled atm, please try again later"