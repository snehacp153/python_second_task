n1 = int(input("enter the limit:"))
n2 = int(input("enter the limit:"))
list_1 = []
list_2 = []
for i in range(0,n1):
    values_list1 = input("enter the elements in list1:") 
    list_1.append(values_list1)
for i in range(0,n2):   
    values_list2 = int(input("enter the elements in list2:"))
    list_2.append(values_list2)

print(list(list_1))
print(list(list_2))
map_two_list = zip(list_1,list_2)
print(dict(map_two_list))



