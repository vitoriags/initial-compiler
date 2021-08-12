# compilador
# main

from funcoes import *

listareservadas = gerarLista('palavrasreservadas.cha', 'r')
listasimbolos = gerarLista('simbolos.cha', 'r')
listatipos = gerarLista('tipos.cha', 'r')

entrada = input().replace(" ", "")
lista = entrada[0]

# ocorre(mano x=0; x<=9; x++)

flag = False
indice = 0
estado = 0
listavariaveis = []
listalexico = []
listasintatico = []
listacomparacao = []

while indice < len(entrada):
    #print(f'{lista}, indice: {indice}')
    flag = False
    if lista in listareservadas and lista not in listatipos:
        listalexico.append(f'Símbolo [frag = {lista}, tipo = palavra reservada]')
        if lista == "ocorre":
            listacomparacao.append("for")

        if estado == 0:
            listasintatico.append(f'Estado {estado}: {lista} = Válido')
        else:
            listasintatico.append(f'Estado {estado}: {lista} = Inválido')
        estado += 1
        flag = True

    elif lista in listasimbolos:
        listalexico.append(f'Símbolo [frag = {lista}, tipo = símbolo]')
        listacomparacao.append(lista)

        if not estado == 0 or estado == 3 or estado == 5 or estado == 7 or estado == 10 or estado == 15 or estado == 16:
            listasintatico.append(f'Estado {estado}: {lista} = Válido')
            if estado == 2:
                estado += 4
            elif estado == 12:
                estado += 2
            else:
                estado += 1
        else:
            listasintatico.append(f'Estado {estado}: {lista} = Inválido')
            estado += 1
        flag = True

    elif lista in listavariaveis:
        listalexico.append(f'Símbolo [frag = {lista}, tipo = variável]')
        listacomparacao.append(lista)

        if estado == 2 or estado == 3 or estado == 5 or estado == 7 or estado == 9 or estado == 10 or estado == 12 or estado == 14 or estado == 15:
            if estado == 14:
                if entrada[12] in listasimbolos:
                    listasintatico.append(f'Estado {estado}: {lista} = Válido')
                    estado += 1
                else:
                    listasintatico.append(f'Estado {estado}: {lista} = Inválido')
                    estado += 1
            elif estado == 2 or estado == 9:
                estado += 2
            else:
                listasintatico.append(f'Estado {estado}: {lista} = Válido')
                estado += 1
        else:
            listasintatico.append(f'Estado {estado}: {lista} = Inválido')
            estado += 1
        flag = True

    elif lista.isnumeric():
        listalexico.append(f'Símbolo [frag = {lista}, tipo = numérico]')
        listacomparacao.append(lista)

        if estado == 5 or estado == 9 or estado == 10 or estado == 15:
            listasintatico.append(f'Estado {estado}: {lista} = Válido')
            estado += 1
        else:
            listasintatico.append(f'Estado {estado}: {lista} = Inválido')
            estado += 1
        flag = True

    elif lista in listatipos:
        listalexico.append(f'Símbolo [frag = {lista}, tipo = tipo]')
        if lista == "mano":
            listacomparacao.append("int ")

        if estado == 2:
            listasintatico.append(f'Estado {estado}: {lista} = Válido')
        else:
            listasintatico.append(f'Estado {estado}: {lista} = Inválido')
        estado += 1
        lista = entrada[indice + 1]

        if lista.isnumeric():
            listalexico.append(f'Símbolo [frag = {lista}, tipo = numérico]')
            listacomparacao.append(lista)

            if estado == 5 or estado == 9 or estado == 10 or estado == 15:
                listasintatico.append(f'Estado {estado}: {lista} = Válido')
                estado += 1
            else:
                listasintatico.append(f'Estado {estado}: {lista} = Inválido')
                estado += 1
        else:
            if estado == 2 or estado == 3 or estado == 5 or estado == 7 or estado == 9 or estado == 10 or estado == 12 or estado == 14:
                if estado == 14:
                    if entrada[12] in listasimbolos:
                        listasintatico.append(f'Estado {estado}: {lista} = Válido')
                        estado += 1
                    else:
                        listasintatico.append(f'Estado {estado}: {lista} = Inválido')
                        estado += 1
                elif estado == 2 or estado == 9:
                    estado += 2
                else:
                    listasintatico.append(f'Estado {estado}: {lista} = Válido')
                    estado += 1
            else:
                listasintatico.append(f'Estado {estado}: {lista} = Inválido')
                estado += 1
            listalexico.append(f'Símbolo [frag = {lista}, tipo = variável]')
            listavariaveis.append(lista)
            listacomparacao.append(lista)
        indice += 1
        flag = True

    else:
        if indice < len(entrada):
            lista = lista + entrada[indice + 1]
    if flag == True:
        if indice < len(entrada) - 1:
            #print(f'passou {lista}, {indice}, {len(entrada)}')
            lista = entrada[indice + 1]
        else:
            #print("pass")
            pass
    indice += 1

print()
stringlexico = ', '.join(map(str, listalexico))
print(f'Léxico: {stringlexico}')
print()
stringsintatico = '\n'.join(map(str, listasintatico))
print(f'Sintático:\n{stringsintatico}')
print()
stringcomparacao = ''.join(map(str, listacomparacao))
print(f'Em C: {stringcomparacao}')
