a=int(input("nhap so a: "))
b=int(input("nhap so b: "))
i=1
ucln=0
if (b>a):
    for i in range (1,b+1):
        if (a%i==0) and (b%i==0):
            if i>ucln:
                ucln=i
else:
    for i in range(1, a + 1):
        if (a % i == 0) and (b % i == 0):
            if i > ucln:
                ucln = i
print(ucln)