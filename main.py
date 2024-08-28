print("Привіт! Ця програма працює як щоденник в кортрий ти можешь записувати свої справи на кожен день! ")
mondays=[]
tuesdays=[]
wednesdays=[]
thursdays=[]
fridays=[]
saturdays=[]
sandays=[]

monday=input("Введіть справу на понеділок (0 - закінчити введення)")

while monday != '0':
    mondays.append(monday)
    monday = input("Введіть справу на понеділок (0 - закінчити введення)")
tuesday=input("Введіть справу на вівторок (0 - закінчити введення)")
while tuesday != '0':
    tuesdays.append(tuesday)
    tuesday = input("Введіть справу на вівторок (0 - закінчити введення)")
wednesday=input("Введіть справу на середу (0 - закінчити введення)")
while wednesday != '0':
    wednesdays.append(wednesday)
    wednesday = input("Введіть справу на середу (0 - закінчити введення)")
thursday=input("Введіть справу а четвер (0 - закінчити введення)")
while thursday != '0':
    thursdays.append(thursday)
    thursday = input("Введіть справу а четвер (0 - закінчити введення)")
friday=input("Введіть справу на п'ятницю (0 - закінчити введення)")
while friday != '0':
    fridays.append(friday)
    friday = input("Введіть справу на п'ятницю (0 - закінчити введення)")
saturday = input("Введіть справу на суботу (0 - закінчити введення)")
while saturday != '0':
    saturdays.append(saturday)
    saturday = input("Введіть справу на суботу (0 - закінчити введення)")
sanday = input("Введіть справу на неділю (0 - закінчити введення)")
while sanday != '0':
    sandays.append(sanday)
    sanday = input("Введіть справу на неділю (0 - закінчити введення)")
print("Список справ:" )
print("Понеділок:", mondays)
print("Вівторок:", tuesdays)
print("Середа:", wednesdays)
print("Чертер:", thursdays)
print("П'ятниця:", fridays)
print("Субота:", saturdays)
print("Неділя:", sandays)
