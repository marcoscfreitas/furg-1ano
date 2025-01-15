# torre de hanói 3 discos

def torreHanoi(numDiscos, origem, destino, auxiliar):
    if numDiscos == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
        return
    torreHanoi(numDiscos -1, origem, auxiliar, destino)
    print(f"Mova o disco {numDiscos } de {origem} para {destino}")
    torreHanoi(numDiscos -1, auxiliar, destino, origem)

numDiscos  = int(input("Digite o número de discos: "))

torreHanoi(numDiscos , "A", "C", "B")