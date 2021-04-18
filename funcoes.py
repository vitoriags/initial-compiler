def manipularArquivo (arquivo, tipo):
  abrirarquivo = (open(arquivo, tipo))
  lerarquivo = abrirarquivo.read()
  abrirarquivo.close()
  return lerarquivo

def gerarLista(arquivo, tipo):
  lista = manipularArquivo(arquivo, tipo)
  listaseparada = lista.split(" ")
  print (listaseparada, '\n\n')
  return listaseparada