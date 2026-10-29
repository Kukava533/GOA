


#1 
# num = int(input("enter your number:")) 
# sum = 0
# while num > 0:
#     n = num % 10
#     sum += num
#     num = num // 10
#     print("number sum is", sum)


# #2
# num = int(input("enter number: "))
# product = 1
# while num > 0:
#     j = num % 10
#     product *= j
#     num = num // 10
#     print("product is: ", product)


# #3 ???
# num = int(input("enter number: "))
# count = 0
# if num > 0:
#     count += 1
#     print(count)


#4 
num = int(input("enter number: "))
five_count = 0
while num > 0:
    u = num % 10
    if u == 5:
        five_count += 1
    num = num // 10
    print(five_count)