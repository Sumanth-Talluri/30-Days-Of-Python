import pandas as pd

fname = './data/hacker_news.csv'
df = pd.read_csv(fname)

print("\nFirst 5 Rows")
print(df.head())

print("\nLast 5 Rows")
print(df.tail())

titles = df['title']
print("\nTitle Column as Series")
print(titles)

py_count = 0
js_count = 0
for title in titles:
    lower_title = title.lower()
    if 'python' in lower_title:
        py_count += 1
    if 'javascript' in lower_title:
        js_count += 1

print(f"python count is {py_count}")
print(f"javascript count is {js_count}")
