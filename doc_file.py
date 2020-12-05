import os
for (a,b,c) in os.walk('C:\\'):
# a= dirpath chỉ ra những thư mục con tại ổ C
	print(a)
# b= dirnames xem tên tất cả thư mục con
	print(b)
# c= name file xem tên tất cả file con
	print(c)