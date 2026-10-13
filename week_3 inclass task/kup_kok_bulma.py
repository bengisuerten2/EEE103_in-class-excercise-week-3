given_number = int(input("Küp kökü bulunacak sayıyı girin: "))


is_negative = False
if given_number < 0:
    is_negative = True
    given_number = abs(given_number)  
guess_number = 1


while guess_number**3 < given_number:
    guess_number += 1

if guess_number**3 == given_number:
    
    if is_negative:
        print("Sayının küp kökü:", -guess_number)
    else:
        print("Sayının küp kökü:", guess_number)
else:
    print("Girdiğiniz sayı tam bir küp değildir.")