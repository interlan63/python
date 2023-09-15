from transliterate import translit
ru_text = "Ladies and gentlemen, I'm 78 years old and I finally got 15 minutes of fame once in a lifetime and I guess that this is mine. \nPeople have also told me to make these next few minutes escruciatingly embarrassing and to take vengeance of my enemies. Neither will happen.\n \nMore than 3 years ago I moved to Novo-Novsk, but worked on new Magnetic Storage for last 40. When I was 8..."
text = translit(ru_text, language_code='ru', reversed=True)
print(text)