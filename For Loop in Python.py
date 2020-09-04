#list1 = [["chocolate", 1], ["icecream", 2],
# ["muffins",3], ["toffee",4]]

#for item in list1:
# print(item)

#for item, mango in list1:
# print(item, "and the mango is", mango)

#dict1 = dict(list1)
#print(dict1)

#for item, mango in dict1.items():
# print(item, "and the mango is", mango)

#for item in dict1:
# if item.endswith("e"):
# print(item)

#Quiz
abcd = [2,3,4,5,6,22,44,5,66,2,2,6654,75]

for item in abcd:
if str(item).isnumeric() and item>6:
print(item)
