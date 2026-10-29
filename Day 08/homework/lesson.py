

#1

num = int(input("enter your number: "))


if num < 0:
    num *= -1

sum = 0
count = 0
if num == 0:
    count = 1
else:
    while num > 0:
        g = num % 10
        sum += g
        count += 1
        num //= 10
print(f"this number sum is: {sum}")
print(f"this number count is: {count}")
    