import json
import string
import csv


fname = './data/obama_speech.txt'
fhand = open(fname, 'r')
text = fhand.read()
lines = text.split('\n')
line_count = len(lines)
word_count = 0
for line in lines:
    words = line.split()
    for word in words:
        if word == " ":
            continue
        word_count += 1
print(f"File name: {fname}")
print(f"Line Count: {line_count}")
print(f"Word Count: {word_count}")


fname = './data/michelle_obama_speech.txt'
fhand = open(fname, 'r')
text = fhand.read()
lines = text.split('\n')
line_count = len(lines)
word_count = 0
for line in lines:
    words = line.split()
    for word in words:
        if word == " ":
            continue
        word_count += 1
print(f"File name: {fname}")
print(f"Line Count: {line_count}")
print(f"Word Count: {word_count}")


fname = './data/donald_speech.txt'
fhand = open(fname, 'r')
text = fhand.read()
lines = text.split('\n')
line_count = len(lines)
word_count = 0
for line in lines:
    words = line.split()
    for word in words:
        if word == " ":
            continue
        word_count += 1
print(f"File name: {fname}")
print(f"Line Count: {line_count}")
print(f"Word Count: {word_count}")


fname = './data/melina_trump_speech.txt'
fhand = open(fname, 'r')
text = fhand.read()
lines = text.split('\n')
line_count = len(lines)
word_count = 0
for line in lines:
    words = line.split()
    for word in words:
        if word == " ":
            continue
        word_count += 1
print(f"File name: {fname}")
print(f"Line Count: {line_count}")
print(f"Word Count: {word_count}")


def most_spoken_languages(fname, n):
    fhand = open(fname, 'r')
    data = fhand.read()
    countries = json.loads(data)
    count_dic = {}
    output = []
    for country in countries:
        languages = country["languages"]
        for language in languages:
            if language not in count_dic:
                count_dic[language] = 1
            else:
                count_dic[language] += 1
    for k, v in count_dic.items():
        tup = (v, k)
        output.append(tup)
    output.sort(key=lambda x: x[0], reverse=True)
    required_output = []
    count = 0
    for item in output:
        if count == n:
            break
        required_output.append(item)
        count += 1
    return required_output


print(most_spoken_languages('./data/countries_data.json', 10))
print(most_spoken_languages('./data/countries_data.json', 3))


def most_populated_countries(fname, n):
    fhand = open(fname, 'r')
    data = fhand.read()
    countries = json.loads(data)
    output = []
    for country in countries:
        new_dic = {}
        new_dic['country'] = country['name']
        new_dic['population'] = country['population']
        output.append(new_dic)
    output.sort(key=lambda x: x['population'], reverse=True)
    required_output = []
    count = 0
    for item in output:
        if count == n:
            break
        required_output.append(item)
        count += 1
    return required_output


print(most_populated_countries('./data/countries_data.json', 10))
print(most_populated_countries('./data/countries_data.json', 3))


fname = './data/email_exchanges_big.txt'
fhand = open(fname, 'r')
data = fhand.read()
lst = data.split('\n')
count = 0
for line in lst:
    if line.startswith('From'):
        count += 1
print(f"There are {count} incoming email addresses")


def find_most_common_words(fname, n):
    fhand = open(fname, 'r')
    data = fhand.read()
    lines = data.split('\n')
    word_dic = {}
    output = []
    for line in lines:
        words = line.split()
        for word in words:
            if word == ' ':
                continue
            if word in word_dic:
                word_dic[word] += 1
            else:
                word_dic[word] = 1
    for k, v in word_dic.items():
        tup = (v, k)
        output.append(tup)
    output.sort(key=lambda x: x[0], reverse=True)
    required_output = []
    count = 0
    for item in output:
        if count == n:
            break
        required_output.append(item)
        count += 1
    return required_output


print(
    f"10 most frequent words in obama_speech.txt are: \n{find_most_common_words('./data/obama_speech.txt', 10)} ")
print(
    f"10 most frequent words in michelle_obama_speech.txt are: \n{find_most_common_words('./data/michelle_obama_speech.txt', 10)} ")
print(
    f"10 most frequent words in donald_speech.txt are: \n{find_most_common_words('./data/donald_speech.txt', 10)} ")
print(
    f"10 most frequent words in melina_trump_speech.txt are: \n{find_most_common_words('./data/melina_trump_speech.txt', 10)} ")


stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up',
              'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]


def clean_text(fname):
    fhand = open(fname, 'r')
    data = fhand.read()
    lines = data.split('\n')
    word_lst = []
    for line in lines:
        words = line.split()
        for word in words:
            if word in stop_words or word in string.punctuation:
                continue
            else:
                word_lst.append(word)
    return word_lst


def check_text_similarity(lst1, lst2):
    output = []
    for word in lst1:
        if word in lst2:
            output.append(word)
    print(f"Total number of similar words are {len(output)}")
    print(f"Similar words are: \n{output}")


michelle_lst = clean_text('./data/michelle_obama_speech.txt')
melina_lst = clean_text('./data/melina_trump_speech.txt')
check_text_similarity(michelle_lst, melina_lst)


print(
    f"10 most frequent words in romeo_and_juliet.txt are: \n{find_most_common_words('./data/romeo_and_juliet.txt', 10)} ")


fname = './data/hacker_news.csv'
fhand = open(fname, 'r')
lines = csv.reader(fhand, delimiter=',')
python_count = 0
js_count = 0
java_count = 0
for line in lines:
    for item in line:
        words = item.split()
        if 'python' in words or 'Python' in words:
            python_count += 1
        if 'javascript' in words or 'Javascript' in words or 'JavaScript' in words:
            js_count += 1
        if 'java' in words or 'Java' in words:
            java_count += 1
print(f"Number of Lines having python are {python_count}")
print(f"Number of Lines having javascript are {js_count}")
print(f"Number of Lines having java are {java_count}")
