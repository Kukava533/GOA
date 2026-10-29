

#1
number1 = 0
number2 = 0
number3 = 0
for i in range(1,100):
    if i % 3 == 0:
        number1 += 1
    elif i % 5 ==0:
        number2 += 1
    elif i % 3 == 0 and i % 5 ==0:
        number3 += 1
print(number1)
print(number2)
print(number3)


# 2 
Single = 0
double = 0
numbers100 = 0
for i in range(1,120):
    if i >= 9:
        Single += 1
        print(Single)
    elif i >= 99:
        double += 1
        print(double)
    else:
        numbers100 += 1
        print(numbers100)



#3
odd = 0
add = 0
numbers = 0
for i in range (1,60):
    if i % 2 != 0:
        odd += 1 + add     
    if i % 10 == 0:
        numbers += 1
print(odd)
print(numbers)

#4
x = 0
y = 0
f = 0
for i in range(1,100):
    if i > 1 and i == 30:
        x += 1
    elif i > 31 and i == 69:
        y += 1
    elif  i > 71 and i == 100:
        f += 1
print(x)
print(y)
print(f)


#5
num1 = 0
num2 = 0
num3 = 0
for i in range(1,51):
    if i % 4 == 1:
        num1 += 1
    elif i % 4 == 2:
        num2 += 1
    elif i % 4 == 0:
        num3 += 1
print(num1)
print(num2)
print(num3)


