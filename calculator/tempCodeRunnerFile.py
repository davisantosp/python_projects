import operacoes as op


while(True):
    num_1 = int(input("Valor 1: "))
    num_2 = int(input("Valor 2: "))

    operacao = str(input("Operacoes:\n" \
                        "1.Soma\n" \
                        "2.Subtracao\n" \
                        "3.Multiplicacao\n" \
                        "4.Divisao\n" \
                        "5.Potencia\n" \
                        "0.Sair\n"))
    resultado = op.operacao_escolhida(operacao, num_1, num_2)

    print(resultado)
    if resultado == "Fim do Programa": break