def leiaDinheiro(msg):
    while True:
        entrada = input(msg).replace(',', '.').strip()
        if entrada == '' or entrada.isalpha():
            print(f'Erro! "{entrada}" é um preço invalido!')
        else:
            return float(entrada)
