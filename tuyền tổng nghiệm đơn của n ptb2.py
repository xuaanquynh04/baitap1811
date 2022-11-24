n = int(input("bạn cần nhập bao nhiêu phương trình"))
tong = 0
for i in range(1, n+1):
    print("phương trình thứ ", i ," bạn nhập là")
    a = float(input('Nhap a = '))
    b = float(input('Nhap b = '))
    c = float(input('Nhap c = '))
    if a == 0 and b == 0 and c == 0:
        print("Phuong trinh vo so nghiem")
    if a == 0 and b == 0 and c != 0:
        print("Phuong trinh vo nghiem")
    if a == 0 and b != 0:
        x = -c / b
        print("Phương trình có 1 nghiệm là ", x)
        tong += x
        print('tổng là', tong)
    if a != 0:
        delta = b ** 2 - 4 * a * c
        if delta == 0:
            x = -b / (2 * a)
            print("Phương trình có nghiệm kép là ", x)
            tong += x
            print('tổng là', tong)
        if delta < 0:
            print(" Phuong trinh vo nghiem")
        if delta > 0:
            print(" Phuong trinh co 2 nghiem")
print('KQ là', tong)
