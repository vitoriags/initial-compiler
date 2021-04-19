from funcoes import *

listareservadas = gerarLista('palavrasreservadas.cha', 'r')
listasimbolos = gerarLista('simbolos.cha', 'r')
listatipos = gerarLista('tipos.cha', 'r')

entrada = input()
listainput = list(entrada)
print("\n\n", listainput)
print("\n\n")


# ocorre(truta x=0;x<9;x++)
# ocorre(truta 8=0;x<9;x++)

indice = 0
lista = listainput[0]
listavariaveis = []

while indice < len(entrada) - 1:
  if lista in listareservadas and lista not in listatipos:
    print(f'Símbolo [frag={lista}, tipo=palavra reservada],')
    lista = listainput[indice+1]

  elif lista in listasimbolos:
    print(f'Símbolo [frag={lista}, tipo=símbolo],')
    lista = listainput[indice+1]

  elif lista in listavariaveis:
    print(f'Símbolo [frag={lista}, tipo=variável],')
    lista = listainput[indice+1]
  
  elif lista.isnumeric():
    print(f'Símbolo [frag={lista}, tipo=numérico],')
    lista = listainput[indice+1]

  elif lista in listatipos:
    print(f'Símbolo [frag={lista}, tipo=tipo],')
    lista = listainput[indice+1]

    if lista.isspace():
      lista = listainput[indice+2]
      indice+=1
    
    if lista.isnumeric():
      print(f'Símbolo [frag={lista}, tipo=numérico],')
      lista = listainput[indice+2]
      indice += 1
    
    else:
      print(f'Símbolo [frag={lista}, tipo=variável],')
      listavariaveis.append(lista)
      lista = listainput[indice+2]
      indice += 1

  elif listainput[indice+1] in listasimbolos:
    if listainput[indice].isspace():
      print(f'Símbolo [frag={listainput[indice-1]}, tipo=variável],')
      listavariaveis.append(listainput[indice-1])
      lista = listainput[indice+1]
    else:
      print(f'Símbolo [frag={listainput[indice]}, tipo=variável],')
      listavariaveis.append(listainput[indice])
      indice+=1
      print(f'Símbolo [frag={listainput[indice]}, tipo=símbolo],')
      indice+=1
      lista = listainput[indice+1]


  elif lista.isspace():
    lista = listainput[indice+1]

  else:
    lista = lista + listainput[indice+1]
    print(lista)

  indice+=1