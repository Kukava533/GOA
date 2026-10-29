
#1 მომხმარებელს შეაყვანინე ტემპერატურა:
# თუ 0 - ზე ნაკლებია - "freezing"
# თუ 0 - 15 - "cold"
# თუ 16 - 25 - "normal"
# თუ 26 - 35 - "hot"
# თუ 36+ - "very hot"

temp = int(input("Enter Temperature: "))
if temp < 0:
    print("its Freezing")
elif temp > 0 and temp <= 15:
    print("Its cold")
elif temp >= 16 and temp <= 25:
    print("Its normal")
elif temp >= 26 and temp <= 35:
    print("Its hot")
else:
    print("its very hot")

# მომხმარებელს შეაყვანინე სამკუთხედი სამი გვერდი:
# თუ ყველა ტოლია - "equalateral"
# თუ ორი ტოლია - "isosceles"
# თუ ყველა განსხვავებულია - "scalene"

p1 = int(input("enter p1: "))
p2 = int(input("enter p2: "))
p3 = int(input("enter p3: "))

if p1 == p2 and p1 == p3:
    print("equalateral")
elif p1 == p2 or p1 == p3 or p2 == p3:
    print("isosceles")
else:
    print("scalene")
# მომხმარებელს შეაყვანინე ასაკი და გაიგე ბილეთის ფასი:
# თუ ასაკი 0 - 5 - "free"
# თუ ასაკი 6 - 17 - "5 lari"
# თუ ასაკი 18 - 64 - "10l lari"
# თუ ასაკი 65+ - "5lari"

age = int(input("enter your age: "))

if age >= 0 and age == 5:
    print("free")
elif age >= 6 or age == 17:
    print("5 lari")
elif age >= 18 or age == 64:
    print("10 lari") 
elif age > 65:
    print("5 lari")
else:
    print("The numbers cannot be negative or zero.")

# მომხმარებელს შეაყვანინე პაროლი:
# თუ პაროლი "**" არის "access granted"
# სხვა შემთხვევაში - "wrong password"

password = input("enter your password: ")

if password == "**":
    print("access granted")
else:
    print("wrong password")

# შეაყვანინე მომხმარებელს 2 რიცხვი a და b:
# გამოიტანე:"a is greater""b is greater""they are equal"

a = int(input("Enter  your First number: "))
b = int(input("Enter your Secound number: "))

if a > b:
    print("a is greater")
elif b > a:
    print("b is greater")
elif a == b:
    print("they are equal")