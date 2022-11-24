flag=1
pt=1
k=-1
d=0
q=0
ds=[]
sn=[]
s=0
s1=0
while flag==1:
    a=float(input("nhap a cua phuong trinh thu " + str(pt)+": "))
    b=float(input("nhap b cua phuong trinh thu " + str(pt) + ": "))
    c=float(input("nhap c cua phuong trinh thu " + str(pt) + ": "))
    if a==0:
        if b==0:
            if c==0:
                q=10
            else:
                q=0
        else:
            q=1
            s1=-c/b
    else:
        d=b*b-4*a*c
        if d<0:
            q=0
        else:
            if d>0:
                q=2
            else:
                q=1
                s1=-b/a
    k=k+1
    sn.insert(k,q)
    if q==1:
        ds.insert(k,s1)
        print("nghiem cua phuong trinh nay se duoc tinh vao tong.")
    else:
        print("nghiem cua phuong trinh nay se khong tinh vao tong.")
    flag=int(input("neu muon tiep tuc nhap phuong trinh thi nhan 1. neu muon xuat tong thi nhan 0: "))
    pt=pt+1
s=sum(ds)
print(s)


