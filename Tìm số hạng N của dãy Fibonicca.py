n=int(input("Nhap so "))
if (n<=0):
    print("nhap so nguyen duong")
    if (n==1):
       print(0)
    elif n==2:
       print(1)
else:
    sothunhat=0
    sothuhai=1
    sohang=0
    for i in range(0,n-2):
        sohang=sothunhat+sothuhai
        sothunhat=sothuhai
        sothuhai=sohang
    print(sothuhai)



