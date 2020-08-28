import requests

url = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(url)
data = response.text
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
    if count == 10:
        break
    required_output.append(item)
    count += 1
print(required_output)


url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
cats_data = response.json()
weights = []
for cat in cats_data:
    weights.append(cat['weight']['metric'])
sum_start = 0
sum_end = 0
for weight in weights:
    w = weight.split()
    start = int(w[0])
    end = int(w[2])
    sum_start += start
    sum_end += end
avg_start = round(sum_start/len(weights))
avg_end = round(sum_end/len(weights))
print(
    f"The average weight of a cat in metric units is in between {avg_start} and {avg_end}")


url = 'https://restcountries.eu/rest/v2/all'
response = requests.get(url)
countries = response.json()
country_lst = []
for country in countries:
    try:
        name, area = country['name'], int(country['area'])
    except:
        continue
    country_lst.append((name, area))
country_lst.sort(key=lambda x: x[1], reverse=True)
print(country_lst[:10])
