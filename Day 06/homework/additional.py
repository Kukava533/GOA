

#1 გაიარე რიცხვები  1დან 50 მდე.დაითვალე სულ 
# რამდენი ისეთი რიცხვია რომელიც იყოფა 3 ზე უნაშთოდ

number = 0
for i in range(1,50):
    if i % 3 == 0:
        number += 1
print("this number is: ", number)


#2 გაიარე რიცხვები  1 დან 100 მდე 
# დაითვალე რამდენი ისეთი რიცხვია, რომელიც მეტია 25 ზე და ნაკლებია 75 ზე 

number1 = 0
for i in range(1, 100):
    if i > 25 and i < 75:
        number1 += 1
print("this number is: ", number1)


#3 გაიარე რიცხვები 1 დან 40 მდე გამოიყენე 
# ორი ცალკე მთვლელი და დაითვალე რამდენი ლუწი რიცხვია და რამდენი კენტი
even = 0
odd = 0
for i in range(1,40):
    if i % 2 == 0:
        even += 1
        print("this number is even: ", i)
    else:
        odd += 1
        print("this number is odd: ", i)

#4 გაიარე 1 დან 60 ჩათვლით რიცხვები დაითვალე 
# რამდენი ისეთი რიცხვია რიმელიც უნაშთოდ იყოფა 4 ზე
number2 = 0
for i in range (1,61):
    if i % 4 == 0:
        number2 += 1
print("this number is: ", number2)


#5 გაიარე რიცხვები 1 დან 80 ჩათვლით დათვალე 
# რამდენი ისეთი რიცხვია რომელიც მეტია 30 ზე და ნაკლებია 60ზე
number3 = 0
for i in range (1,81):
    if i > 30 and i < 60:
        number3 += 1
print("this number is: ", number3)
