#4) დაწერეთ ალგორითმი, რომელიც მომხმარებელს შეეკითხება რიცხვს. თუ რიცხვი ლუწია გაყავით ორზე, სხვა შემთხვევაში გაამრავლეთ სამზე და მიუმატეთ ერთი.


# მომხმარებლის მიერ რიცხვის შეყვანა
number = int(input("შეიყვანეთ რიცხვი: "))

# შემოწმება, არის თუ არა რიცხვი ლუწი
if number % 2 == 0:
    # თუ რიცხვი ლუწია, გაყოფა ორზე
    result = number / 2
else:
    # თუ რიცხვი არ არის ლუწი, გამრავლება სამზე და დამატება ერთი
    result = (number * 3) + 1

# შედეგის გამოყვანა
print(f"შედეგი: {result}")
ახსნა:
number = int(input("შეიყვანეთ რიცხვი: ")): მომხმარებელს ვთხოვთ შეიყვანოს რიცხვი და ვაქცევთ მას int ტიპში.

if number % 2 == 0:: შემოწმდება, არის თუ არა რიცხვი ლუწი. ლუწი რიცხვი წარმოადგენს იმ რიცხვებს, რომლებიც გაყოფილი ორით არ ტოვებენ დანარჩენს (% ოპერატორის გამოყენებით).

result = number / 2: თუ რიცხვი ლუწია, გაყოფა ორზე.

result = (number * 3) + 1: თუ რიცხვი ლუწი არ არის, გამრავლება სამზე და დამატება ერთი.

print(f"შედეგი: {result}"): შედეგის დაბეჭდვა.

ამ პროგრამა ითვალისწინებს რიცხვის შეყვანას და გამოთვლის შედეგს იმაზე დამოკიდებული, არის თუ არა რიცხვი ლუწი.









