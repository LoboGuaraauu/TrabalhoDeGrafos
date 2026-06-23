def gerar_campeonato(equipes):

    n = len(equipes)

    # Se for ímpar, adiciona equipe fantasma
    if n % 2 == 1:
        equipes.append("Folga")
        n += 1

    times = equipes[:]
    rodadas = []

    for rodada in range(n - 1):

        jogos = []

        for i in range(n // 2):
            time1 = times[i]
            time2 = times[n - 1 - i]

            if time1 != "Folga" and time2 != "Folga":
                jogos.append((time1, time2))

        rodadas.append(jogos)

        # Método do círculo
        fixo = times[0]
        resto = times[1:]

        resto = [resto[-1]] + resto[:-1]

        times = [fixo] + resto

    return rodadas


def exibir_rodadas(rodadas):

    print("=== Calendario Gerado ===\n")

    for i, rodada in enumerate(rodadas, start=1):

        print(f"Cor c{i}  -> Rodada {i}")

        for jogo in rodada:
            print(f"   {jogo[0]} x {jogo[1]}")

        print()


# Exemplo do artigo (K6)

equipes = ["A", "B", "C", "D", "E", "F"]

rodadas = gerar_campeonato(equipes)

exibir_rodadas(rodadas)

n = len(equipes)

print("Numero de equipes:", n)
print("Numero de rodadas:", len(rodadas))
print("Indice cromatico X'(K_n):", n - 1)

