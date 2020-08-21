lst = []

lst = [1, 2, 3, 4, 5, 6, 7]
print(lst)

print(len(lst))

fitem = lst[0]
litem = lst[len(lst)-1]
mitem = lst[(len(lst)//2)+1]
print(fitem, mitem, litem)

mixed_data_types = ["sumanth", 12, 185, "single", "LA,USA"]
print(mixed_data_types)

it_companies = ["Facebook", "Goolge", "Microsoft",
                "Apple", "IBM", "Oracle", "Amazon"]

print(it_companies)

print(f"No of companies: {len(it_companies)}")

fitem = it_companies[0]
litem = it_companies[len(it_companies)-1]
mitem = it_companies[(len(it_companies)//2)+1]
print(fitem, mitem, litem)

it_companies[0] = "Cisco"
print(it_companies)

it_companies.append("Palo Alto")
print(it_companies)

it_companies.insert((len(it_companies)//2)+1, "Juniper")
print(it_companies)

it_companies[0] = it_companies[0].upper()
print(it_companies)

print("#; ".join(it_companies))

if "Facebook" in it_companies:
    print("Facebook is present")
else:
    print("Facebook is not present")

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[:3])

print(it_companies[-3:])

print(it_companies[(len(it_companies)//2)+1])

it_companies.remove(it_companies[-1])
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
web_technologies = front_end + back_end
print(web_technologies)

full_stack = web_technologies.copy()
full_stack.extend(["Python", "SQL", "Redux"])
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(f"Min is {ages[0]} and Max is {ages[-1]}")

ages.extend([ages[0], ages[-1]])
print(ages)

if len(ages) % 2 == 0:
    item1 = ages[len(ages)//2]
    item2 = ages[(len(ages)//2)-1]
    median = (item1+item2) / 2
else:
    median = ages[(len(ages)//2)+1]
print(median)

result = sum(ages)
average = result/len(ages)
print(average)

minn = ages[0]
maxx = ages[-1]
print(maxx - minn)

if abs(minn-average) > abs(maxx-average):
    print("1")
else:
    print("2")

countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Cape Verde',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombi',
    'Comoros',
    'Congo (Brazzaville)',
    'Congo',
    'Costa Rica',
    "Cote d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor (Timor Timur)',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia, The',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia and Montenegro',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syria',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe',
]
print(f"middle element of countries is {countries[(len(countries)//2)+1]}")

if len(countries) % 2 == 0:
    countries1 = countries[0:len(countries)/2]
    countries2 = countries[len(countries)/2:]
else:
    countries1 = countries[0:(len(countries)//2)+1]
    countries2 = countries[(len(countries)//2)+1:]
print(countries1)
print(countries2)

first, second, third, *scandic = ['China', 'Russia',
                                  'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(first, second, third)
print(scandic)
