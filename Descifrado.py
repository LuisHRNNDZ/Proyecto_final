def Desencriptar(Frase):
    FraseDes = ''
    for letra in Frase:
        encontrado = False
        for x,y in abecedario.items():
            if letra == y:
                FraseDes += x
                encontrado = True
        if not encontrado: 
            FraseDes += letra
    return FraseDes
abecedario = {
    'A':'E', 'B':'F', 'C':'G', 'D':'H', 'E':'I',
    'F':'J', 'G':'K', 'H':'L', 'I':'M', 'J':'N',
    'K':'O', 'L':'P', 'M':'Q', 'N':'R', 'O':'S',
    'P':'T', 'Q':'U', 'R':'V', 'S':'W', 'T':'X',
    'U':'Y', 'V':'Z', 'W':'A', 'X':'B', 'Y':'C',
    'Z':'D'
}
print("Menú\n1) Desencriptar\n2) Salir")
x = int(input("Opción: "))
while x != 2:
    if x == 1:
        frase = input('Frase encriptada: ')
        frase = frase.upper()
        fraseEnc = Desencriptar(frase)
        print(fraseEnc)
    else:
        print("Error! Opción no válida")
    print("Menú\n1) Desencriptar\n2) Salir")
    x = int(input("Opción: "))
    
