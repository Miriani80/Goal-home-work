#2)შექმენით დროში მოგზაურობის პროგრამა, რომელიც მომხმარებელს შეეკითხება მის ამჟამინდელ ასაკს, ამჟამინდელ წელს, რამდენი წლით სურს დროში მოგზაურობა, შემდეგ კი პროგრამა დაბეჭდავს დროში მოგზაურობის შემდეგ რომელი წელი იქნება და რამდენი წლის იქნება მომხმარებელი დროში მოგზაურობის შემდეგ
import datetime

# მომხმარებლისგან მოთხოვნილი ინფორმაციის შეყვანა
current_age = int(input("შეიყვანეთ თქვენი ამჟამინდელი ასაკი: "))
current_year = datetime.datetime.now().year
years_to_travel = int(input("რამდენი წლით სურს მოგზაურობა დროში: "))

# გამოთვალება დროში მოგზაურობის შემდეგი წელი და მისი ასაკი
future_year = current_year + years_to_travel
future_age = current_age + years_to_travel

#print
print(f"დროში მოგზაურობის შემდეგ თქვენ იქნებით {future_year} წელს და თქვენი ასაკი იქნება {future_age} წელი.")