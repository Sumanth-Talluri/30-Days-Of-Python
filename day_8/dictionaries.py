dog = {}

dog['name'] = 'snoopy'
dog['color'] = 'white'
dog['breed'] = 'shitzu'
dog['legs'] = 'black'
dog['age'] = '5'
print(dog)

student = {
    'first_name': 'Alex',
    'last_name': 'jones',
    'gender': 'male',
    'age': 15,
    'marital_status': 'single',
    'skills': ['HTML', 'CSS', 'Python'],
    'country': 'India',
    'city': 'Chennai',
    'address': 'Ramapuram'
}
print(student)

print(len(student))

print(type(student['skills']))

student['skills'].append('Javascript')
print(student)

print(student.keys())

print(student.values())

print(student.items())

del student['address']
print(student)

del student
