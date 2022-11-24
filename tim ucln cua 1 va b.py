#Tìm ước số chung lớn nhất của 2 số A B
a = int(input("nhập số hạng A: "))
b = int(input("nhập số hạng B: "))
c = 0
d = 0
lista=[]
listb=[]
n=0
m=0
ucln=0
print("Các ước của A là: ")
for i in range(1,a+1):
    c += 1
    if a % c == 0:
       lista.insert(n,c)
       n=n+1
print("Các ước của B là: ")
for i in range(1,b+1):
    d += 1
    if b % d == 0:
       listb.insert(m,d)
       m=m+1
print(lista)
print(listb)
giao_nghiem = set(lista)&set(listb)
for i in giao_nghiem:
    if i > ucln:
        ucln = i
print("Ước chung lớn nhất: ",ucln)




