list1=[]
list2=[]
size=int(input("Enter the size"))
print("Enter the elements")
for i in range(0,size):
    element=int(input())
    list1.append(element)
    if(list1[i]%2 ==0):
        list2.append(list1[i])
print("input list",list1)
print("even list",list2)
