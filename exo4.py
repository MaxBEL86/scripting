#print ("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,Like a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")
import sys
texte=["Bonjour, je m'appelle Maxime"]


def MinMaj(texte):
    min = 0
    maj = 0
    for char in texte:
        if char.isupper():
            maj = maj+1
        elif char.islower():
            min = min+1
    return maj,min

