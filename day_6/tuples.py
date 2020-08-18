tp = ()

tp_brothers = ('alpha', 'bravo', 'charlie')
tp_sisters = ('alita',)

tp_siblings = tp_brothers + tp_sisters
print(tp_siblings)

print(len(tp_siblings))

tp_siblings += ('fathername',)
tp_siblings += ('mothername',)
family_members = tp_siblings
print(family_members)

siblings, parents = family_members[:4], family_members[4:]
print(siblings)
print(parents)

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
animal_products = ('milk', 'curd')
food_stuff = fruits + vegetables + animal_products
print(food_stuff)

if len(food_stuff) % 2 == 0:
    print(food_stuff[(len(food_stuff)//2)-1])
    print(food_stuff[len(food_stuff)//2])
else:
    print(food_stuff[len(food_stuff)//2])

newtp = food_stuff[:3] + food_stuff[-3:]
print(newtp)

del food_stuff

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
if 'Estonia' in nordic_countries:
    print("Estonia is a nordic country")
if 'Iceland' in nordic_countries:
    print("Iceland is a nordic country")
