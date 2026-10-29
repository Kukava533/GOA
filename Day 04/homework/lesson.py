
#1 შექმენი კალკულატორი

num1 = int(input("Enter your number: "))
num2 = int(input("Enter your number: "))
operation = input("Choose your operation /, -, *, **, +, //, %:" )


if operation == "+":
    print(" your result is " , num1 + num2)
elif operation == "-":
    print(" your result is " , num1 - num2)
elif operation == "*":
    print(" your result is " , num1 * num2)
elif operation == "/":
    print(" your result is " , num1 / num2)
elif operation == "**":
    print(" your result is " , num1 ** num2)
elif operation == "//":
    print(" your result is " , num1 // num2)
elif operation == "%":
    print(" your result is " , num1 % num2)
else:
    print("only numbers allowed")



#2 მომხმარებელს შემოაყვანინე პროდუქტის ფასი: 
# თუ ფასი 0 - 50 ფასდაკლება არ არის
# თუ ფასი 51 - 100 - 10% ფასდაკლება
# თუ ფასი 101 - 200 - 20% ფასდაკლება
# თუ ფასი 200-ზე მეტია მაშინ - 30%

product_price = int(input("Enter your product price: "))

if product_price >= 0 and product_price <= 50:
    discount = 0
    print("There is no discount.")
elif product_price >= 51 and product_price <= 100:
     discount = 10
     print("10 discount")
elif product_price >= 101 and product_price <= 200:
    discount = 20
    print("20 discount")
elif product_price >= 200:
    discount = 30
    print("30 discount")

final_price = product_price - discount
print(final_price)

# 3 მომხმარებელმა შეიყვანოს username  და  password
# თუ სწორია - "log in successful"
# თუ username არასწორია  - "wrong username"
# თუ password არასწორია - "wrong password"
# თუ არცერთი არ არის სწორი - "wrong log in"

username = input("Enter your username: ")
password = str(input("Enter your password: "))
correct_username = "Nikmen"
correct_password = "Busuna120"

if username == correct_username and password == correct_password:
    print("log in successful")
elif username != correct_username and password == correct_password:
    print("wrong username")
elif username == correct_username and password != correct_password:
    print("wrong password")
else:
    print("wrong log in")



