# Cifrado Cesar doble

abecedario = {
    'A': 'E', 'B': 'F', 'C': 'G', 'D': 'H', 'E': 'I',
    'F': 'J', 'G': 'K', 'H': 'L', 'I': 'M', 'J': 'N',
    'K': 'O', 'L': 'P', 'M': 'Q', 'N': 'R', 'O': 'S',
    'P': 'T', 'Q': 'U', 'R': 'V', 'S': 'W', 'T': 'X',
    'U': 'Y', 'V': 'Z', 'W': 'A', 'X': 'B', 'Y': 'C',
    'Z': 'D'
}


def Encriptar(Frase):
    Frase = Frase.upper()
    FraseEnc = ''
    for letra in Frase:
        encontrado = False
        for x, y in abecedario.items():
            if letra == x:
                FraseEnc += y
                encontrado = True
        if not encontrado:
            FraseEnc += letra
    return Encriptar2(FraseEnc)


def Encriptar2(Frase):
    Frase = Frase.upper()
    FraseEnc = ''
    for letra in Frase:
        encontrado = False
        for x, y in abecedario.items():
            if letra == x:
                FraseEnc += y
                encontrado = True
        if not encontrado:
            FraseEnc += letra
    return FraseEnc
