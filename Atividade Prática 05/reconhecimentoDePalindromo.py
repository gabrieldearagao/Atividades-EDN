import unicodedata

def eh_palindromo(texto):
    texto_normalizado = ""

    for caractere in texto.lower():
        caractere = unicodedata.normalize('NFD', caractere)
        caractere = ''.join(c for c in caractere if unicodedata.category(c) != 'Mn')

        if caractere.isalnum():
            texto_normalizado += caractere

    if texto_normalizado == texto_normalizado[::-1]:
        return "Sim"
    else:
        return "Não"

print(eh_palindromo("Dracula"))  
print(eh_palindromo("Ame a ema")) 
print(eh_palindromo("Gabriel"))         
print(eh_palindromo("Socorram-me subi no ônibus em Marrocos")) 