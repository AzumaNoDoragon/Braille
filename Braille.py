from Unicode import *

def text_to_braille(text):
    return ''.join(braille_map.get(char, char) for char in text)

with open('transcricao.txt', 'r', encoding='utf-8') as file:
    text = file.readline()
    braille_text = text_to_braille(text)

with open('transcrito.txt', 'w', encoding='utf-8')as file:
    file.write(braille_text)

print("Texto Original:")
print(text)
print("\nTexto em Braille:")
print(braille_text)