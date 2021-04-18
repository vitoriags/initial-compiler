from funcoes import *

listareservadas = gerarLista('palavrasreservadas.cha', 'r')
listasimbolos = gerarLista('simbolos.cha', 'r')
listatipos = gerarLista('tipos.cha', 'r')

entrada = input()
listainput = list(entrada)
print("\n\n", listainput)
print("\n\n")


# ocorre(truta x=0;x<9;x++)

indice = 0
lista = listainput[0]
listavariaveis = []

while indice < len(entrada) - 1:
  if lista in listareservadas and lista not in listatipos:
    print(lista,'= palavra reservada')
    lista = listainput[indice+1]

  elif lista in listasimbolos:
    print(lista,'= símbolo')
    lista = listainput[indice+1]

  elif lista in listavariaveis:
    print(lista,'= variável')
    lista = listainput[indice+1]
  
  elif lista.isnumeric():
    print(listainput[indice], '= número')
    lista = listainput[indice+1]

  elif lista in listatipos:
    print(lista,'= palavra reservada e tipo')
    lista = listainput[indice+1]  # indice 11 + 1 = ' '

    if lista == " ":
      lista = listainput[indice+2] # indice 11 + 2 = x
      indice+=1   # indice 11 + 1 = 12 (' ')
    
    print(lista, '= variável')
    listavariaveis.append(lista)
    lista = listainput[indice+2]
    indice += 1

  elif lista == " ":
    lista = listainput[indice+1]

  else:
    lista = lista + listainput[indice+1]
    print(lista)

  indice+=1