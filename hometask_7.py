from collections import Counter
import re
# file = open(r"C:\Users\Sofiia_Kalishchuk\hometasks_python_dqe\newsfeed.txt")
# data = file.read()
#
# counts = Counter(re.findall('\w+', data))
# list1 = list(counts.keys())
# list2 = list(counts.values())
# list3 = []
# for i in range(len(list1)):
#     list3.append(str(list1[i].lower()) + '-' + str(list2[i]))
# #print(list3)
# import csv
# # with open('text1.csv', 'w') as csvfile:
# #     writer = csv.writer(csvfile)
# #     writer.writerow(list3)
#
# with open('text2.csv', 'w') as csvfile:
#
#     headers = ['letter', 'cout_all', 'count_uppercase', 'percentage']
#     writer = csv.DictWriter(csvfile, fieldnames=headers)
#     writer.writeheader()
#     for i in range(len(list3)):
#         writer.writerow({'letter': list3[i], 'cout_all': list3[i], 'count_uppercase': list3[i], 'percentage': list3[i]})

text = 'aaAa abbB.bbccccc'
c = re.findall('\w+', text)
c1 = ''.join(c)
text1 = Counter(c1)
list3 = list(text1.keys())
list4 = list(text1.values())
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
for l in range(len(lower)):
    for r in range(len(upper)):
        low = upper[r]
        if low.lower() == lower[l]:
            print('we have a match')
            matchy_list.append(lower[l])
        else:
            print('no')

sum_for_matched =[]
for y in range(len(matchy_list)):
    summy = 0
    low1 = str(matchy_list[y])
    first = text1.get(low1)
    up = matchy_list[y]
    up1 = up.upper()
    second = text1.get(up1)
    summy = first + second
    sum_for_matched.append(summy)

print(text1)
print(sum_for_matched)
print(matchy_list)
print(list3)
print(upper)
print(lower)
print(sum1)