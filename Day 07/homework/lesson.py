


#1. 1-დან 150-მდე გაიარე რიცხვები for ციკლით და დაითვალე:
#რამდენი რიცხვი იყოფა 2-ზე უნაშთოდ.
#რამდენი რიცხვი იყოფა 7-ზე უნაშთოდ.
#რამდენი რიცხვი იყოფა ერთდროულად 2-ზეც და 7-ზეც.
#საბოლოოდ დაბეჭდე სამივე რაოდენობა.

g = 0
h = 0
k = 0
for i in range(1,150):
    if i % 2 == 0:
        g += 1
    elif i % 7 == 0:
        h += 1
    else:
        i % 2 and i % 7 == 0
        k += 1
print(g)
print(h)
print(k)

#2. 1-დან 200-მდე დაითვალე:
#რამდენი რიცხვია კენტი.
#რამდენი რიცხვია ლუწი.
#რამდენი რიცხვი იყოფა 10-ზე უნაშთოდ.

odd = 0
even = 0
num = 0
for i in range(1,200):
    if i % 2 != 0:
        odd += 1
    elif i % 2 == 0:
        even += 1
    if i % 10 == 0:
        num += 1
print(odd)
print(even)
print(num)

#3. 30-დან 100-მდე დაითვალე:
#რამდენი რიცხვი იყოფა 3-ზე.
#რამდენი რიცხვი იყოფა 4-ზე.
#რამდენი რიცხვი არ იყოფა არც 3-ზე და არც 4-ზე.
num1 = 0
num2 = 0
num3 = 0
for i in range(30, 100):
    if i % 3 == 0:
        num1 += 1
    elif i % 4 == 0:
        num2 += 1
    elif i % 3 != 0 and i % 4 != 0:
        num3 += 1
print(num1)
print(num2)
print(num3)

#4. 1-დან 80-მდე დაითვალე, რამდენი რიცხვი 5-ზე გაყოფისას ტოვებს:
#ნაშთს 0.
#ნაშთს 2.
#ნაშთს 3.

number_1 = 0
number_2 = 0
number_3 = 0
for i in range(1,80):
    if i % 5 == 0:
        number_1 += 1
    elif i % 5 == 2:
        number_2 += 1
    elif i % 5 == 3:
        number_3 += 1
print(number_1)
print(number_2)
print(number_3)

#5  1-დან 100-მდე დაითვალე:
#    რამდენი რიცხვია 20-ზე ნაკლები.
#    რამდენი რიცხვია 20-დან 60-ის ჩათვლით.
#    რამდენი რიცხვია 60-ზე მეტი.
number_4 = 0
number_5 = 0
number_6 = 0
for i in range(1,100):
    if i  < 20:
        number_4 += 1
    elif i <= 60:
        number_5 += 1
    elif i > 60:
        number_6 += 1
print(number_4)
print(number_5)
print(number_6)