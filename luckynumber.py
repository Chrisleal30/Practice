def lucky_number(name):
    number = len(name) * 17
    return number

name = input("What is your name?")

print("Hi"+" "+str(name)+" "+"your lucky number is"+" "+ str(lucky_number(name)))
