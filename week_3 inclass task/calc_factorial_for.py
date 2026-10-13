
sayi = int(input("Faktöriyeli alınacak sayıyı girin: "))
faktoriyel = 1

for i in range(1, sayi + 1):
    faktoriyel = faktoriyel * i  # ya da kısaca faktoriyel *= i

print("Sonuç:", faktoriyel)