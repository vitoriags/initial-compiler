from funcoes import *

listareservadas = gerarLista('palavrasreservadas.cha', 'r')
listasimbolos = gerarLista('simbolos.cha', 'r')
listatipos = gerarLista('tipos.cha', 'r')

entrada = input()
listainput = entrada.split(" ")
print("\n\n", listainput, "\n\n")

flag = False
listavariaveis = []
indice = 0

while indice < len(listainput):
  for reservada in listareservadas:
    if listainput[indice] == reservada and listainput[indice] not in listatipos:
      print(listainput[indice],' = palavra reservada')
      flag = True
      
  for simbolo in listasimbolos:
    if listainput[indice] == simbolo:
      print(listainput[indice],' = símbolo')
      flag = True
  
  if listainput[indice] in listavariaveis:
    print(listainput[indice],' = variável')
    flag = True

  #if indice < len(listainput) - 1 and listainput[indice+1] == "=": # menos 2 casinhas pq pode ser variável apenas se ela tiver mais duas casinhas na frente. (x = 1)
  #  print(listainput[indice],' = variável')
  #  listavariaveis.append(listainput[indice])
  #  flag = True

  if listainput[indice] in listareservadas and listainput[indice] in listatipos:
    print(listainput[indice],' = palavra reservada e tipo')
    indice = indice + 1
    print(listainput[indice],' = variável')
    listavariaveis.append(listainput[indice])
    flag = True

  elif listainput[indice].isnumeric():
    print(listainput[indice], ' = número')

  elif not flag:
    print(listainput[indice],' = texto')

  flag = False
  indice = indice + 1