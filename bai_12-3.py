import random,string
list1 = []
n = random.randrange(49,101)
for i in range(n) :
    y = random.randrange(1, 10)
    tuoi = random.randrange(0,100)
    def random_char(y):
        return ''.join(random.choice(string.ascii_letters) for x in range(y))
    dict1 = {'Name': random_char(y), 'Age': tuoi }
    list1.append(dict1)
print(list1)