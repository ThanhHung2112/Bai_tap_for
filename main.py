import random
list1 = []
list2 = []
list3 = []
n = random.randrange(49,1001)
print("list1 có",n,"phần tử")
for i in range(n) :
     list1.append(input("nhập phần tử "))
     list2.append(random.randrange(-1001,1001))
     list3.append((random.uniform(-1001,1001)))
print("phần tử list1 :",list1)
print("phần tử list2 :",list2)
print("phần tử list3 :",list3)
