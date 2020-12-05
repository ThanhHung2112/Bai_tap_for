import os
name = input('nhập tên thư mục cần tạo :')
os.mkdir(name)
os.listdir()
link=os.getcwd()
name_file = input('nhập tên file :')
m= open(name_file,'w')
print(link)
#n = input('nhập dữ liệu file')
#m.write(n)
#data = open(name_file).read()
#print('dữ liệu trong tập tin là :', data)
m.close()


