from transliterate import translit
from num2words import num2words

text1 = "Ladies and gentlemen, I'm 78 "
text2 = "years old and I finally got 15 "
text3 = "minutes of fame once in a lifetime and I guess that this is mine. \nPeople have also told me to make these next few minutes escruciatingly embarrassing and to take vengeance of my enemies.\n \n Neither will happen. More than 3 "
text4 = "years ago I moved to Novo-Novsk, but worked on new Magnetic Storage for last 40 "
text5 = "When I was 8 " 
text6 = "..."
ru_text1 = translit(text1, 'ru')
ru_text2 = translit(text2, 'ru')
ru_text3 = translit(text3, 'ru')
ru_text4 = translit(text4, 'ru')
ru_text5 = translit(text5, 'ru')
ru_text6 = translit(text6, 'ru')
output = f"{ru_text1} {ru_text2} {ru_text3} {ru_text4} {ru_text5} {ru_text6}"
print(output)
print(" ")
print("78 -", num2words(78))
print("15-", num2words(15))
print("3 -", num2words(3))
print("40 -", num2words(40))
print("8 -", num2words(8))
