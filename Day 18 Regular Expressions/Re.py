import re

paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."
lst = paragraph.split()
lst_set = set(lst)
output = []

for word in lst_set:
    matches = re.findall(word, paragraph, re.I)
    count = len(matches)
    tup = []
    tup.append(count)
    tup.append(word)
    tup = tuple(tup)
    output.append(tup)
print(output)

points = [-12, -4, -3, -1, 0, 4, 8]
print(abs(points[0]) + points[len(points)-1])


def is_valid_variable(a):
    regex_pattern1 = r'^[a-z]|^[A-Z]|^_'
    if re.findall(regex_pattern1, a):
        print(True)
    else:
        print(False)


is_valid_variable('first_name')  # True
is_valid_variable('first-name')  # False
is_valid_variable('1first_name')  # False
is_valid_variable('firstname')  # True

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

cleaned_text = re.sub(r'[#]|[%]|[$]|[@]|[,]|[&]|[;]|[.]|[!]|[?]', '', sentence)
print(cleaned_text)


def most_frequent_words(txt):
    lst = txt.split()
    lst_set = set(lst)
    output = []

    for word in lst_set:
        matches = re.findall(word, txt, re.I)
        count = len(matches)
        tup = []
        tup.append(count)
        tup.append(word)
        tup = tuple(tup)
        output.append(tup)
    print(output)


most_frequent_words(cleaned_text)
