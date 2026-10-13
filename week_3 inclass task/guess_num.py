



from secret_number import secretNum
sayac = 0

while True:

    x = float(input("Gizli sayıyı tahmin etmeye çalışın: "))

    if x > secretNum:
        print("Daha küçük bir sayı düşünmelisin")
    elif x < secretNum:
        print("Daha büyük bir sayı düşünmelisin")
        
    else:
        print("Tebrikler, gizli sayıyı buldun")
    sayac += 1
    if sayac > 5:
        print ("deneme hakkın bitti")
        break