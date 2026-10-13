sayi = int(input("Faktöriyeli alınacak sayıyı girin: "))
faktoriyel = 1
i = 1

while i <= sayi:
    faktoriyel = faktoriyel * i
    i = i + 1  # ya da kısaca i += 1

print("Sonuç:", faktoriyel)