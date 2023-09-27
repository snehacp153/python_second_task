# input list elements
result =[]
numbers = int(input("enter the limit:"))
roll_no = []
for i in range(0,numbers):
    elements = int(input("enter the values:"))
    roll_no.append(elements)
# input dict elements
dict_num = int(input("enter the limit:"))
d = {}
for i in range(0,dict_num):
    keys = input("enter the keys:")
    values = int(input("enter the values:"))
    d[keys] = values

for value in d.values():
    if value in roll_no:
       result.append(value)
    print(result)
    