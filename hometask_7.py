from collections import Counter
import re
import csv
import os



# first part of the hometask
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'newsfeed.txt')
with open(filename) as file:
    data = file.read()

counts = Counter(re.findall('\w+', data))
list1 = list(counts.keys())
list2 = list(counts.values())
list3 = []
for i in range(len(list1)):
    list3.append(str(list1[i].lower()) + '-' + str(list2[i]))

with open('text1.csv', 'w') as csvfile:
     writer = csv.writer(csvfile)
     writer.writerow(list3)

# second part of the hometask
c = re.findall('\w+', data)
c1 = ''.join(c)
text = str()
for j in c1:
    if j.isalpha():
        text = text + j

text1 = Counter(text)
list3 = list(text1.keys())
sum1 = sum(text1.values())

upper =[]
lower = []
for j in range(len(list3)):
    u = list3[j].isupper()
    if u == True:
        upper.append(list3[j])
    else:
        lower.append(list3[j])

matchy_list = []
not_matchy_list = []
for l in range(len(lower)):
    for r in range(len(upper)):
        low = upper[r]
        if low.lower() == lower[l]:
            print('we have a match')
            matchy_list.append(lower[l])

seen = set() # set for all letters from all dictionaries without duplication
dupes = set()# with this cycle we make the list of duplicates and elements that are not duplicated
for i in lower:
    if i in matchy_list:
        dupes.add(i)
    else:
        seen.add(i)

not_matchy_list = list(seen)
not_matchy_list_values =[]

for y in range(len(not_matchy_list)):
    not_matchy_list_values.append(text1.get(not_matchy_list[y]))

sum_for_matched =[]
upper_values = []
for y in range(len(matchy_list)):
    summy = 0
    low1 = str(matchy_list[y])
    first = text1.get(low1)
    up = matchy_list[y]
    up1 = up.upper()
    second = text1.get(up1)
    upper_values.append(text1.get(up1))
    summy = first + second
    sum_for_matched.append(summy)

# print(text1)
# print(lower)
# print(sum_for_matched)
# print(matchy_list)
# print(not_matchy_list)
# print(upper_values)

with open('text2.csv', 'w') as csvfile:
    headers = ['letter', 'cout_all', 'count_uppercase', 'percentage']
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    for i in range(len(matchy_list)):
        writer.writerow({'letter': matchy_list[i], 'cout_all': sum_for_matched[i], 'count_uppercase': upper_values[i], 'percentage': ((sum_for_matched[i])/sum1)*100})
    for i in range(len(not_matchy_list)):
        writer.writerow({'letter': not_matchy_list[i], 'cout_all': not_matchy_list_values[i], 'count_uppercase': 0, 'percentage': ((not_matchy_list_values[i])/sum1)*100})