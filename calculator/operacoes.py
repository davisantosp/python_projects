def soma(num_1, num_2):
    return num_1 + num_2

def subtracao(num_1, num_2):
    return num_1 - num_2

def multiplicacao(num_1, num_2):
    return num_1 * num_2

def divisao(num_1, num_2):
    return num_1 / num_2

def potencia(num_1, num_2):
    return num_1 ** num_2

def operacao_escolhida(operacao, num_1, num_2):
    match operacao:
        case "1":
            num_3 = soma(num_1, num_2)

        case "2":
            num_3 = subtracao(num_1, num_2)

        case "3":
            num_3 = multiplicacao(num_1, num_2)

        case "4":
            num_3 = divisao(num_1, num_2)

        case "5":
            num_3 = potencia(num_1, num_2)

        case "0":
            num_3 = "Fim do Programa"
            return
    
    return num_3