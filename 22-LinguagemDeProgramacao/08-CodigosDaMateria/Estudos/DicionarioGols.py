Jogadores = [
    {'nomes': 'Jogador1', 'partidas': 3, 'gols': [2, 4, 5]},
    {'nomes': 'Jogador2', 'partidas': 5, 'gols': [5, 8, 0]},
    {'nomes': 'Jogador3', 'partidas': 6, 'gols': [1, 2, 1]}
]

for jogador in Jogadores:
    nomes = jogador['nomes']
    partidas = jogador['partidas']
    gols = jogador['gols']

    saldo_gol = sum(gols)

    print(f'Jogador: {nomes}, jogou: {partidas}, marcou: {gols}, saldo de gols: {saldo_gol}')
