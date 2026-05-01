def menu():
    print("1-Criptografar uma mensagem")
    print("2-Descriptografar uma mensagem")
    print("3-Sair")




def conversao_lista(seq1):
    # lê a chave dada e retorna uma lista com a posição alfabética de cada letra, em ordem
    # (A=1,B=2,etc.)
    seq2 = []
    for caractere in seq1:
        c_ordem = int(ord(caractere.upper())) - 64
        seq2.append(c_ordem)
    return seq2




def codifica(m_original, seq, offset):
    contador = 0
    m_modificado = ""
    for caractere in m_original:
        m_modificado += desloca_letra(caractere, offset * seq[contador])
        contador += 1
        if contador >= len(seq):  # reinicia o contador conforme o tamanho da chave dada
            contador = 0
    return m_modificado




def desloca_letra(letra, offset):
    num = ord(letra)
    if 65 <= num <= 90:  # caso da letra ser minúscula
        num = num + offset
        if num < 65:
            num += 26
        elif num > 90:
            num -= 26
    elif 97 <= num <= 122:  # caso da letra ser maiúscula
        num = num + offset
        if num < 97:
            num += 26
        elif num > 122:
            num -= 26
    return chr(num)




print("Demonstração da cifra de Vigenère")
while True:
    menu()
    escolha = input("Digite um número: ")
    if escolha == "1" or escolha == "2":
        entrada = input("Entre com a frase de entrada: ")
        chave = input("Entre com a chave (somente letras, sem espaço): ")
        sequencia = conversao_lista(chave)
        if escolha == "1":
            print(codifica(entrada, sequencia, 1))
        else:
            print(codifica(entrada, sequencia, -1))
    elif escolha == "3":
        break
    else:
        print("Entrada inválida.")
    print("")
