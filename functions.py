## compares two numbers and returns them in increasing order

def order_numbers(number1, number2):
    if number2 > number1: 
        return number1,number2
    else: 
        return number2,number1

arrange = order_numbers(200,100)
print(arrange)