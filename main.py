from time import sleep


def aquecimento():
    global TEMP_INT
    print("Aquecimento acionado devido a condições não favoráveis ao cozimento")
    sleep(2)
    print("Ligando aquecimento")
    sleep(3)
    print("Temperatura:")
    for AQUECIMENTO in range(TEMP_INT, 381, +1):
        print(AQUECIMENTO)
        sleep(0.02)
    TEMP_INT = 380
    sleep(2)
    print("A temperatura do forno agora é de 380 graus celsius")
    sleep(2)
    print("Aquecimento desligado")
    sleep(2)
    print("Forno pronto para cocção")
    BOTAO = input("Insira conteúdo para cocção, apos inserção pressione o botão pronto (1-pronto): ")
    while BOTAO != "1":
        print("Valor não reconhecido")
        BOTAO = input("Insira conteúdo para cocção, apos inserção pressione o botão pronto (1-pronto): ")
    if BOTAO == "1":
        print("O temperatura do forno se manterá em 380 graus celsius durante 3 horas")
        TIMER = 0
        sleep(2)
        print("O forno começará a contagem de tempo em minutos agora")
        sleep(3)
        print("Minutos:")
        for a in range(TIMER, 60, +1):
            print(a)
            sleep(0.1)
        TIMER = 60
        print("Já passou uma hora desde o ínicio, faltam mais duas horas para conclusão da cocção ")
        sleep(3)
        print("Minutos:")
        for b in range(TIMER, 120, +1):
            print(b)
            sleep(0.1)
        TIMER = 120
        print("Já passaram duas horas desde o ínicio, falta apenas uma hora para conclusão da cocção ")
        sleep(3)
        print("Minutos:")
        for c in range(TIMER, 180, +1):
            print(c)
            sleep(0.1)
        TIMER = 0
        sleep(2)
        print("Aquecimento desligado")
        sleep(2)
        print("Cocção concluída,conteúdo liberado para retirada, aproveite :)")


def exaustor_off():
    UMIDADE = 5
    sleep(2)
    print("A umidade interna do forno agora é de 5%")
    sleep(2)
    print("Exaustor desligado")
    sleep(2)
    print("Desumidificação concluída")
    sleep(3)


TEMP_INT = int(input("Insira a temperatura atual do forno (0 - 200): "))
if TEMP_INT >= 201:
    print("Temperatura não consta nos valores pedidos")
    exit()
TEMP_EXT = int(input("Insira a temperatura do ambiente: "))
UMIDADE = int(input("Insira a umidade do ar interna do forno (0 - 100): "))
if UMIDADE > 100:
    print("Quantidade não reconhecida da umidade")
    exit()
clima = input("Insira a estação do ano: 1-Inverno 2-Outono 3-Primavera 4-Verão: ")
if clima == "1":
    sleep(2)
    print(f"A umidade do ar no forno é de {UMIDADE}%")
    sleep(2)
    print(f"A temperatura interna do forno é de {TEMP_INT} graus celsius")
    print("O processo de desumidificação comecará agora")
    sleep(2)
    if 15 < TEMP_INT < 100 and UMIDADE >= 40:
        print("Exaustor acionado devido a necessidade de desumidificação devido clima")
        sleep(3)
        print("Ligando exaustor")
        sleep(3)
        print("Umidade:")
        for EXAUSTOR in range(UMIDADE, 4, -1):
            print(EXAUSTOR)
            sleep(0.1)
        exaustor_off()
        print("Iniciando procedimentos para cocção")
        sleep(2)
        print(f"A temperatura interna do forno é {TEMP_INT} em graus celsius")
        if TEMP_INT <= 200:
            aquecimento()
    elif TEMP_INT <= 15 and UMIDADE >= 40:
        print("Exaustor e aquecimento acionados devido a necessidade de desumidificação devido clima")
        sleep(3)
        print("Ligando exaustor")
        sleep(3)
        print("Umidade:")
        for EXAUSTOR in range(UMIDADE, 4, -1):
            print(EXAUSTOR)
            sleep(0.1)
        UMIDADE = 5
        sleep(2)
        print("A umidade interna do forno agora é 5%")
        sleep(2)
        print("Exaustor desligado")
        sleep(2)
        print("Desumidificação parcialmente concluída")
        sleep(2)
        print("Ligando aquecimento")
        sleep(3)
        print("Temperatura:")
        for AQUECIMENTO in range(TEMP_INT, 101, +1):
            print(AQUECIMENTO)
            sleep(0.1)
        TEMP_INT = 100
        sleep(2)
        print("A temperatura do forno agora é de 100 graus celsius")
        sleep(2)
        print("Aquecimento desligado")
        sleep(2)
        print("Desumidificação concluída")
        sleep(3)
        print("Iniciando procedimentos para cocção")
        sleep(2)
        print(f"A temperatura interna do forno é {TEMP_INT} em graus celsius")
        if TEMP_INT <= 200:
            aquecimento()
    elif TEMP_INT > 100 and UMIDADE <= 5:
        print("Resfriamento acionado devido a necessidade de desumidificação devido clima")
        sleep(3)
        print("Ligando resfriamento")
        sleep(3)
        print("Temperatura:")
        for RESFRIAMENTO in range(TEMP_INT, 99, -1):
            print(RESFRIAMENTO)
            sleep(0.1)
        TEMP_INT = 100
        sleep(2)
        print("A temperatura do forno agora é de 100 graus celsius")
        sleep(2)
        print("Resfriamento desligado")
        sleep(2)
        print("Resfriamento concluído")
        sleep(3)
        print("Iniciando procedimentos para cocção")
        sleep(2)
        print(f"A temperatura interna do forno é {TEMP_INT} em graus celsius")
        if TEMP_INT <= 200:
            aquecimento()
    elif UMIDADE > 5 and TEMP_INT > 100:
        print("Exaustor e resfriamento acionados devido a necessidade de desumidificação devido clima")
        sleep(3)
        print("Ligando resfriamento")
        sleep(3)
        print("Temperatura:")
        for RESFRIAMENTO in range(TEMP_INT, 99, -1):
            print(RESFRIAMENTO)
            sleep(0.1)
        TEMP_INT = 100
        sleep(2)
        print("A temperatura do forno agora é de 100 graus celsius")
        sleep(2)
        print("Resfriamento desligado")
        sleep(2)
        print("Resfriamento concluído")
        sleep(2)
        print("Ligando exaustor")
        sleep(3)
        print("Umidade:")
        for EXAUSTOR in range(UMIDADE, 4, -1):
            print(EXAUSTOR)
            sleep(0.1)
        exaustor_off()
        print("Iniciando procedimentos para cocção")
        sleep(2)
        print(f"A temperatura interna do forno é {TEMP_INT} em graus celsius")
        if TEMP_INT <= 200:
            aquecimento()
elif clima == 2 or 3 or 4:
    sleep(1)
    print("Iniciando procedimentos para cocção")
    sleep(1)
    print(f"A umidade interna do forno é {UMIDADE}%")
    if UMIDADE > 15:
        print("Exaustor acionado devido a condições não favoráveis ao cozimento")
        sleep(3)
        print("Ligando exaustor")
        sleep(3)
        print("Umidade:")
        for EXAUSTOR in range(UMIDADE, 4, -1):
            print(EXAUSTOR)
            sleep(0.1)
        UMIDADE = 5
        sleep(2)
        print("A umidade interna do forno agora é de 5%")
        sleep(2)
        print("Exaustor desligado")
    sleep(2)
    print(f"A temperatura interna do forno é {TEMP_INT} graus celsius")
    if TEMP_INT <= 200:
        aquecimento()
else:
    print("Código de clima não reconhecido")