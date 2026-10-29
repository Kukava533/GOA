

#1 იპოვე რიცხვი 1 დან 100მდე და დათვალე ყველა ლუწი რიცხვის ჯამი 

total = 0
for i in range(1, 50):
    if i % 2 == 0:
        total += i
print(total)
    

#2 გაიარე რიცხვები 1 დან 100მდე და დათვალე რამდენი რიცხვი იყოფა 3 ზე უნდაშთოდ.
n = 0
for i in range(1,100):
    if i % 3 == 0:
        n += 1
print(n)

#3 გაიარე რიცხვები 1 დან 100მდე თუ რიცხვი იყოფა 5 ზე მაშინ 
# დაბეჭტე devided by 5 თუ იყოფა 5 ზეც და 10ზეც დაბიჭტე devided by 5 and by 10

for i in range(1,100):
    if i % 5 == 0:
        print("devide by 5")
    elif i % 5 and i % 10 == 0:
        print("devide by 5 and by 10")
    else:
        print("this number is not devided")
    
 
#4 წარმოიდგინე რომ გაქვს ასაკი 1 - 80 თითოეული ასაკისთვის დაბეჭტე შესაბამისი კატეგორია:

for age in range(1, 80):
    if age > 0 and age <= 12:
        print("child")
    elif age >= 13 and age <= 17:
        print("teenager")
    elif age >= 18 and age <= 64:
        print("you are adult")
    elif age > 65:
        print("senior")



#5 იპოვე 1დან 100 მდე ყველა რიცხვის ჯამი რომელიც 3 ის ჯერადია მაგრამ 5 ის ჯერადი არ არის
sum = 0
for i in range(1,101):
    if i % 3 == 0 and i % 5 != 0:
        print("divaded by 3")
        sum += i
print(sum)


