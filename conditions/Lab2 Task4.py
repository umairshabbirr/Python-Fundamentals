chara=input("enter the single character")
if chara.lower() in "aeiou":
    print("The character is Vowel")
elif chara.isalpha():
    print("The Character is Consonant")
else:
 print("Enter the Alphabet Character")   