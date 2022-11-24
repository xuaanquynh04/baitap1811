# Cho n phương trình bậc 2 tính tổng của nghiệm khi có 1 nghiệm
tong_nghiem=0
def kiemtraPT():
     while True:
          a = int(input("nhap a: "))
          b = int(input("nhap b: "))
          c = int(input("nhap c: "))
          delta = 0
          x = 0
          tong_nghiem = 0
          if a == 0:
               if b != 0:
                    tong_nghiem = -c/b
                    print("Phương trình có một nghiệm: ",tong_nghiem)
                    break
               else:
                    print("mời nhập lại:")
          else:
               delta = b ** 2 - 4 * a * c
               if delta == 0:
                         x = - b / 2 * a
                         print("Phương trình có nghiệm kép: ", x)
                         tong_nghiem = x
                         break
               else:
                    print("Mời nhập lại:")
     return tong_nghiem
n = int(input("Hãy nhập số phương trình:"))
S = 0
for i in range (1,n+1):
  tong_nghiem = kiemtraPT()
  S += tong_nghiem
print("tong nghiệm của hai phương trình:",S)