new1 = "Thiry "+"Days "+"Of "+"Python"
new2 = "Coding "+"For "+"All"
company = new2
print(company)
print(len(company))
upper_company = company.upper()
lower_company = company.lower()
cap = new2.capitalize()
tit = new2.title()
swp = new2.swapcase()
print(cap, tit, swp)
cut = new2[:6]
print(new2.index("Coding"))
new3 = new2.replace("Coding", "Python")

new4 = "Python for Everyone"
new4 = new3.replace("Everyone", "All")

new2_lst = new2.split()

new5 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
new5_lst = new5.split(",")

print(new2[0])
print(new2[-1])
print(new2[10])

new4_acr = "PFE"
new2_acr = "CFA"

print(new2.index("C"))
print(new2.index("F"))

print("Coding For All People".rfind("I"))

print("You cannot end a sentence with because because because is a conjunction".find('because'))

print(
    "You cannot end a sentence with because because because is a conjunction"[31:54])

print("You cannot end a sentence with because because because is a conjunction".find("because"))

print(
    "You cannot end a sentence with because because because is a conjunction"[31:54])

print("Coding For All".startswith("Coding"))

print("Coding For All".endswith("coding"))

print('   Coding For All      '.strip())

print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

lst = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(lst))

print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name\tAge\tCountry\nAsabeneh\t250\tFinland")

radius = 10
area = 3.14 * radius ** 2
print(f"The area of a cricle with radius {radius} is {area} meters square.")

print(f"8 + 6 = {8+6}\n8 - 6 = {8-6}\n8 * 6 = {8*6}\n8 / 6 = {8/6:.2f}\n8 % 6 = {8%6}\n8 // 6 = {8//6}\n8 ** 6 = {8**6}")
