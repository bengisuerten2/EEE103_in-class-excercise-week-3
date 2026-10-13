x = int(input("Bir sayı giriniz: "))
sum_loop = 0
for i in range (1, x + 1):
    sum_loop += i
print("Toplam:", sum_loop)

sum_gauss = x * (x + 1) // 2
print("Gauss Toplamı:", sum_gauss)
if sum_loop == sum_gauss:
    print("Toplamlar eşit, kod çalışıyor")
else :
    print("Toplamlar eşit değil, kod çalışmıyor")