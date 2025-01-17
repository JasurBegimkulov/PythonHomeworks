list1 = [1, 1, 2]
list2 = [2, 3, 4]

uncommon_elements = []

for i in list1:
    if i not in list2:
        uncommon_elements.append(i)
for i in list2:
    if i not in list1:
        uncommon_elements.append(i)
print(uncommon_elements)



list1 = [1, 2, 3]
list2 = [4, 5, 6]

uncommon_elements = []

for i in list1:
    if i not in list2:
        uncommon_elements.append(i)
for i in list2:
    if i not in list1:
        uncommon_elements.append(i)
print(uncommon_elements)


list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

uncommon_elements = []

for i in list1:
    if i not in list2:
        uncommon_elements.append(i)
for i in list2:
    if i not in list1:
        uncommon_elements.append(i)
print(uncommon_elements)