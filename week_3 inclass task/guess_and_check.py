given_number = int(input("Karekökü bulunacak sayıyı girin: "))


if given_number < 0:
    print("Square root of negative numbers is not a real number.")
else:
    guess_number = 1
    
   
    while guess_number**2 < given_number:
        guess_number += 1
        
    
    if guess_number**2 == given_number:
        print("Sayının karekökü:", guess_number)
    else:
        print("Girdiğiniz sayı bir tam kare (perfect square) değildir.")