
#1
num = int(input("enter number: "))
reverse = 0 
while num > 0:
    g = num % 10
    reverse = reverse * 10 + g
    num = num // 10
print("number:", reverse)

2
num = int(input("Enter your Number: "))

even_Count = 0
Odd_Count = 0

while num > 0:
    f = num % 10
    if f % 2 == 0:
        even_Count += 1
    else:
        Odd_Count += 1
    num = num // 10
    print("even numbers: ")
    print("odd numbers: ")


#3
num = int(input("enter number: "))
max = 0
while num > 0:
    b = num % 10
    if b > max:
        max = b
    num = num // 10
print(max)