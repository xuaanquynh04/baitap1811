flag=1
k=-1
ds = []
s=0
q=0
d=0
while flag==1:
    a=float(input("nhap a: "))
    b=float(input("nhap b: "))
    c=float(input("nhap c: "))
    if a==0:
        if b==0:
            if c==0:
                q=10
            else:
                q=0
        else:
            q=1
    else:
        d=b*b-4*a*c
        if d<0:
            q=0
        else:
            q=2
    k=k+1
    if q==10:
        print("phuong trinh co vo so nghiem. khong the tinh tong 2 nghiem cua phuong trinh nay.")
    else:
        if q==2:
            ds.insert(k,(-b/a))
        else:
            if q==1:
                print("phuong trinh co 1 nghiem. khong the tinh tong 2 nghiem cua phuong trinh nay.")
            else:
                print("phuong trinh vo nghiem. khong the tinh tong 2 nghiem co phuong trinh nay.")
    if k==1:
        flag=0
s=sum(ds)
print(s)




