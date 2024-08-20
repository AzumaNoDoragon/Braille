# Letras Braille
space = "\u2800"
a = "\u2801"  # Braille 'a'
b = "\u2803"  # Braille 'b'
c = "\u2809"  # Braille 'c'
d = "\u2819"  # Braille 'd'
e = "\u2811"  # Braille 'e'
f = "\u280B"  # Braille 'f'
g = "\u280F"  # Braille 'g'
h = "\u281F"  # Braille 'h'
i = "\u280A"  # Braille 'i'
j = "\u281A"  # Braille 'j'
k = "\u2805"  # Braille 'k'
l = "\u2807"  # Braille 'l'
m = "\u280D"  # Braille 'm'
n = "\u281D"  # Braille 'n'
o = "\u2815"  # Braille 'o'
p = "\u280E"  # Braille 'p'
q = "\u281E"  # Braille 'q'
r = "\u281F"  # Braille 'r'
s = "\u2812"  # Braille 's'
t = "\u2813"  # Braille 't'
u = "\u2825"  # Braille 'u'
v = "\u2827"  # Braille 'v'
w = "\u283C"  # Braille 'w'
x = "\u282D"  # Braille 'x'
y = "\u283D"  # Braille 'y'
z = "\u283E"  # Braille 'z'

# Letras com Acento Agudo
á = a + "\u2831"  # á
é = e + "\u2831"  # é
í = i + "\u2831"  # í
ó = o + "\u2831"  # ó
ú = u + "\u2831"  # ú

# Letras com Acento Grave
à = a + "\u2832"  # à
è = e + "\u2832"  # è
ì = i + "\u2832"  # ì
ò = o + "\u2832"  # ò
ù = u + "\u2832"  # ù

# Letras com Acento Circunflexo
â = a + "\u2833"  # â
ê = e + "\u2833"  # ê
î = i + "\u2833"  # î
ô = o + "\u2833"  # ô
û = u + "\u2833"  # û

# Letras com Til
ã = a + "\u2834"  # ã
õ = o + "\u2834"  # õ

# Letra com Cedilha
ç = c + "\u2835"  # ç

# Letras com Trema
ä = a + "\u2836"  # ä
ö = o + "\u2836"  # ö
ü = u + "\u2836"  # ü

# Indicador de Maiúscula
indicadorMaiuscula = "\u2801"  # Indicador de Maiúscula

# Números Braille
num0 = "\u2830"  # Braille '0'
num1 = "\u2801"  # Braille '1'
num2 = "\u2803"  # Braille '2'
num3 = "\u2809"  # Braille '3'
num4 = "\u2819"  # Braille '4'
num5 = "\u2811"  # Braille '5'
num6 = "\u280B"  # Braille '6'
num7 = "\u280F"  # Braille '7'
num8 = "\u281F"  # Braille '8'
num9 = "\u280A"  # Braille '9'

# Símbolos Matemáticos e Especiais
# Operadores Matemáticos
adicao = "\u283C"  # Adição (+)
subtracao = "\u283D"  # Subtração (-)
multiplicacao = "\u283B"  # Multiplicação (×)
divisao = "\u2832"  # Divisão (÷)
igual = "\u283C"  # Igual (=)
MaisMenos = "\u283C"  # Mais ou Menos (±)

# Sinais de Comparação
menor = "\u280C"  # Menor que (<)
maior = "\u281C"  # Maior que (>)

# Parênteses e Pontuação
abrePar = "\u2829"  # Abre Parênteses (()
fechaPar = "\u282A"  # Fecha Parênteses ())
pontoDec = "\u2824"  # Ponto Decimal (.)
pontoFinal = "\u282E"  # Ponto Final (.)
virgula = "\u2802"  # Vírgula (,)
pontoVirgula = "\u2836"  # Ponto e Vírgula (;)
doisPontos = "\u2836"  # Dois Pontos (:)
aspas = "\u2833"  # Aspas (")
apostrofo = "\u2804"  # Apóstrofo (')
interrogacao = "\u283F"  # Interrogação (?)
exclamacao = "\u2834"  # Exclamação (!)
hifen = "\u281D"  # Hífen (-)

# Símbolos Especiais
raiz = "\u283B"  # Raiz Quadrada (√)
arroba = "\u2838"  # Arroba (@)
asterisco = "\u2835"  # Asterisco (*)
porcentagem = "\u283B"  # Porcentagem (%)

# Regras de nomenclatura
braille_map = {
    ' ': space, 'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h, 'i': i, 'j': j,'k': k, 'l': l, 'm': m, 'n': n, 'o': o, 'p': p, 'q': q, 'r': r, 's': s, 't': t, 'u': u, 'v': v, 'w': w, 'x': x, 'y': y, 'z': z,
    'á': á, 'é': é, 'í': í, 'ó': ó, 'ú': ú, 'à': à, 'è': è, 'ì': ì, 'ò': ò, 'ù': ù, 'â': â, 'ê': ê, 'î': î, 'ô': ô, 'û': û, 'ã': ã, 'õ': õ, 'ç': ç, 'ä': ä, 'ö': ö, 'ü': ü,
    'A': indicadorMaiuscula + a, 'B': indicadorMaiuscula + b, 'C': indicadorMaiuscula + c, 'D': indicadorMaiuscula + d, 'E': indicadorMaiuscula + e, 'F': indicadorMaiuscula + f, 'G': indicadorMaiuscula + g, 'H': indicadorMaiuscula + h, 'I': indicadorMaiuscula + i, 'J': indicadorMaiuscula + j, 'K': indicadorMaiuscula + k, 'L': indicadorMaiuscula + l, 'M': indicadorMaiuscula + m, 'N': indicadorMaiuscula + n, 'O': indicadorMaiuscula + o, 'P': indicadorMaiuscula + p, 'Q': indicadorMaiuscula + q, 'R': indicadorMaiuscula + r, 'S': indicadorMaiuscula + s, 'T': indicadorMaiuscula + t, 'U': indicadorMaiuscula + u, 'V': indicadorMaiuscula + v, 'W': indicadorMaiuscula + w, 'X': indicadorMaiuscula + x, 'Y': indicadorMaiuscula + y, 'Z': indicadorMaiuscula + z,
    'Á': indicadorMaiuscula + a, 'É': indicadorMaiuscula + e, 'Í': indicadorMaiuscula + i, 'Ó': indicadorMaiuscula + o, 'Ú': indicadorMaiuscula + u, 'À': indicadorMaiuscula + a, 'È': indicadorMaiuscula + e, 'Ì': indicadorMaiuscula + i, 'Ò': indicadorMaiuscula + o, 'Ù': indicadorMaiuscula + u, 'Â': indicadorMaiuscula + a, 'Ê': indicadorMaiuscula + e, 'Î': indicadorMaiuscula + i, 'Ô': indicadorMaiuscula + o, 'Û': indicadorMaiuscula + u, 'Ã': indicadorMaiuscula + a, 'Õ': indicadorMaiuscula + o, 'Ç': indicadorMaiuscula + c, 'Ä': indicadorMaiuscula + a, 'Ö': indicadorMaiuscula + o, 'Ü': indicadorMaiuscula + u,
    '0': num0, '1': num1, '2': num2, '3': num3, '4': num4, '5': num5, '6': num6, '7': num7, '8': num8, '9': num9,
    '+': adicao, '-': subtracao, '*': multiplicacao, '/': divisao, '=': igual, '<': menor, '>': maior,
    '(': abrePar, ')': fechaPar,  ',': virgula, '√': raiz, '±': MaisMenos, 
    '@': arroba, '*': asterisco, '%': porcentagem, '-': hifen, '"': aspas, "'": apostrofo,
    ':': doisPontos, ';': pontoVirgula, '!': exclamacao, '?': interrogacao, '.': pontoDec, '.': pontoFinal
}
