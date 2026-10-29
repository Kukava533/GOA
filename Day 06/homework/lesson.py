
#1 გაიარე რიცხვები 1 დან 100მდე და დაითვალე: 
# რამდენია ლუწი რამდენია კენტი რამდენია 10ზე მეტი და 50ზე ნაკლები

odd_counter = 0
even_counter = 0
number4 = 0
for i in range(1,101):
    if i % 2 == 0:
        even_counter += 1
    elif i % 2 != 0:
        odd_counter += 1
    if i > 10 and i < 50:
        number4 += 1
print(odd_counter)
print(even_counter)
print(number4)



