age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18-age} more years to learn to drive.")

my_age = int(input("Enter my age: "))
your_age = int(input("Enter your age: "))
if my_age > your_age:
    print(f"I am {my_age-your_age} years older than you.")
elif my_age == your_age:
    print("Our ages are same")
else:
    print(f"You are {your_age-my_age} years older than me.")

a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print(f"{a} is greater then {b}")
elif a == b:
    print("Both values are same")
else:
    print(f"{b} is greater then {a}.")

s = int(input("Enter score: "))
if s >= 80 and s <= 100:
    print("A")
elif s >= 70 and s <= 79:
    print("B")
elif s >= 60 and s <= 69:
    print("C")
elif s >= 50 and s <= 59:
    print("C")
else:
    print(F)

month = input("Enter month")
if month in ['September', 'October', 'November']:
    print("Autumn")
elif month in ['December', 'January', 'February']:
    print("Winter")
elif month in ['March', 'April', 'May']:
    print("Spring")
elif month in ['June', 'July', 'August']:
    print("Summer")
else:
    print("Enter month correctly")

fruits = ['banana', 'orange', 'mango', 'lemon']
name = input("Enter a fruit")
if name not in fruits:
    fruits.append(name)
    print(fruits)
else:
    print("That fruit already exist in the list")

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if person.get('skills'):
    if len(person['skills']) % 2 == 0:
        print(person['skills'][(len(person['skills'])//2) - 1],
              person['skills'][(len(person['skills'])//2)])
    else:
        print(person['skills'][len(person['skills'])//2])
else:
    print("No Skills")

if person.get('skills'):
    if 'Python' in person.get('skills'):
        print("Python is one of the skills")
    else:
        print("No Python in skills")
else:
    print("No Skills")

if person.get('skills'):
    if 'Javascript' in person.get('skills') and 'React' in person.get('skills'):
        print('He is a front end developer')
    elif 'Node' in person.get('skills') and 'Python' in person.get('skills') and 'MongoDB' in person.get('skills'):
        print('He is a backend developer')
    elif 'Node' in person.get('skills') and 'React' in person.get('skills') and 'MongoDB' in person.get('skills'):
        print('He is a fullstack developer')
    else:
        print('unknown title')
else:
    print("No Skills")
