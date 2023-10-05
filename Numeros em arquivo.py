def salvar_arq(numeros):
    arquivo_numeros = 'arquivo_num.txt'
    
    with open('arquivo_num.txt', 'a') as arquivo:
        for num in numeros:
            arquivo.write(str(num) + '\n')
    
    return arquivo_numeros

def media_num(arquivo_numeros):
    numeros = []
    
    with open(arquivo_numeros, 'r') as arquivo:
        for linha in arquivo:
            numero = int(linha.strip())
            numeros.append(numero)
    
    media = sum(numeros) / len(numeros)
    
    return media
    
def pedir_numeros(numeros):
    while True:
        numero = int(input("Digite um numeros inteiro (digite 0 para parar de adicionar): "))
        
        if numero == 0:
            break
        
        numeros.append(numero)
    
    return numeros
    
numeros = []    
numeros = pedir_numeros(numeros)
arquivo_numeros = salvar_arq(numeros)
media = media_num(arquivo_numeros)

print(f'Os numeros foram salvos em um arquivo {arquivo_numeros}!')
print(f'A média dos numeros dentro do arquivo é: {media}')
