# Tính tổng nghiệm  của 2 phương trình bậc 2 nhập vào khi có 2 nghiệm
import math
tong_nghiem=0
def kiemtraPT():
     while True:
          a = int(input("nhap a: "))
          b = int(input("nhap b: "))
          c = int(input("nhap c: "))
          delta = 0
          tong_nghiem = 0
          if a != 0:
               delta = b ** 2 - 4 * a * c
               if delta > 0:
                    x2 = (- b - math.sqrt(delta)) / 2 * a
                    x1 = (- b + math.sqrt(delta)) / 2 * a
                    print("x1 = ", x1, "x2 = ", x2)
                    tong_nghiem = x1 + x2 + tong_nghiem
                    break
               else:
                    print("Mời nhập lại:")
          else:
               print("Mời nhập lại:")
     return tong_nghiem
tong_nghiem1 = kiemtraPT()
tong_nghiem2 = kiemtraPT()
S = tong_nghiem1 + tong_nghiem2
print("tong nghiệm của hai phương trình:",S)