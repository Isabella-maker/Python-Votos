total_votantes = int(input("Quantas pessoas vão votar? "))

votos1 = 0
votos2 = 0
votos3 = 0

for i in range(1, total_votantes + 1):
    while True:
        voto = int(input(f"Pessoa {i}, digite seu voto (1, 2 ou 3): "))
        
        if voto in [1, 2, 3]:
            break
        else:
            print("Voto inválido! Tente novamente.")

    if voto == 1:
        votos1 += 1
    elif voto == 2:
        votos2 += 1
    else:
        votos3 += 1

print("\nResultado da votação:")
print(f"Candidato 1: {votos1} votos")
print(f"Candidato 2: {votos2} votos")
print(f"Candidato 3: {votos3} votos")

# Verificando o vencedor
if votos1 > votos2 and votos1 > votos3:
    print("Vencedor: Candidato 1")
elif votos2 > votos1 and votos2 > votos3:
    print("Vencedor: Candidato 2")
elif votos3 > votos1 and votos3 > votos2:
    print("Vencedor: Candidato 3")
else:
    print("Houve empate!")