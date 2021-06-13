
try:
     answer = 10/0
     number = (float(input("Enter a numeber: ")))
     print(number)
except ValueError: 
    print("Invalid input")

except ZeroDivisionError as err:
    print(err)
    