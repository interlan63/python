from transliterate import translit
from num2words import num2words

text1 = "Ladies and gentlemen, I'm"
text2 = "years old and I finally got"
text3 = "minutes of fame once in a lifetime and I guess that this is mine. \nPeople have also told me to make these next few minutes escruciatingly embarrassing and to take vengeance of my enemies.\n \n Neither will happen. More than"
text4 = "years ago I moved to Novo-Novsk, but worked on new Magnetic Storage for last"
text5 = "When I was" 
text6 = "..."
ru_text1 = translit(text1, 'ru')
ru_text2 = translit(text2, 'ru')
ru_text3 = translit(text3, 'ru')
ru_text4 = translit(text4, 'ru')
ru_text5 = translit(text5, 'ru')
ru_text6 = translit(text6, 'ru')
output = f"{ru_text1} {num2words(78)} {ru_text2} {num2words(15)} {ru_text3} {num2words(3)} {ru_text4} {num2words(40)} {ru_text5} {num2words(8)} {ru_text6}"
print(output)
