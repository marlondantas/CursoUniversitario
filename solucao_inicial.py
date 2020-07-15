#                                 ¯\_(ヅ)_/¯ 
import random

def shuffleSemestres(index_disciplinas):
  # print('index_disciplinas ',index_disciplinas)
  total_materias = len(index_disciplinas)

  nUM = random.randint(0,total_materias-1)
  nDOIS = random.randint(0,total_materias-1)

  while (nUM == nDOIS):
    nDOIS = random.randint(0,total_materias-1)

  saida=[]
  
  saida.append(index_disciplinas[nUM])
  saida.append(index_disciplinas[nDOIS])

  for x in range(total_materias):
    if(nUM == x or nDOIS == x):
      continue
    else:  
      saida.append(index_disciplinas[x])

  return saida

def SepararBlocos(index_disciplinas):
  blocos = index_disciplinas
  n_materias = int(len(blocos))
  conjuntos={}

  if(n_materias < 6):
    
    conjuntos['conjuntoespecial'] = []

    blocos = sorted(blocos,reverse=True)
    for x in range(n_materias):
      conjuntos['conjuntoespecial'].append(blocos[x])
    return conjuntos

  conjuntos['conjunto0'] = []
  conjuntos['conjunto1'] = []
  conjuntos['conjunto2'] = []

  count = 0


  for x in range(n_materias):
    if(count == 0):
      conjuntos['conjunto0'].append(blocos[x])
      count = 1
    elif (count == 1):
      conjuntos['conjunto1'].append(blocos[x])
      count = 2
    elif (count == 2):
      conjuntos['conjunto2'].append(blocos[x])
      count = 0

  return conjuntos

def CalcularBlocosSeparados(conjuntos, pontos):

  saida = {}
  extra = []

  for x in conjuntos.keys():
    extra.extend(conjuntos[x])
  
  flag = True
  counti = 0

  novos_blocos = {}
  while flag:

    if(len(extra) > 0 ):
        novos_blocos = SepararBlocos(extra)
      
        extra.clear()

        for x in novos_blocos.keys():

            counti = counti + 1
            total_saida = 0
        
            esse_semestre = []
            proximo_semestre = []

            for y in list(novos_blocos[x]):
                total_saida = total_saida + int(y[0])
                if(total_saida > pontos):
                  proximo_semestre.append(y)
                else:
                  esse_semestre.append(y)
                #Aqui ele já separa os semestres e boa
                    
            # if(total_saida <= pontos):
            #     saida[x+"e"+str(counti)] = list(novos_blocos[x])
            # else:
            #     extra.extend(novos_blocos[x])
            
            saida[x+"e"+str(counti)] = list(esse_semestre)
            extra.extend(proximo_semestre)

            # Aqui o saida vai adicionar o "esse_semestre" e o extra vai adcionar o proximo_semestre e apagar ambos.
    else:
        flag = False
  
  return saida

def AnaliseSemestre(curso):
  if(curso == {}):
    return {'dados':"Sem sucesso!!!"}
  saida = {}

  count = 0
  count_materia = 0

  n_total = 0
  p_total = 0
  m_total = 0
  for wddd in curso.keys():

    if(curso[wddd] == []):
      continue
    else:

    #n = número total de materías no semestre / p número de peso total do semestre 
      p_pacial = 0
      n_parcial = len(curso[wddd])

      for x in curso[wddd]:
        p_pacial = p_pacial + int(x[0])
        count_materia = count_materia + 1

      saida[count] = [n_parcial,p_pacial,int(p_pacial/n_parcial)]

      n_total = n_total + n_parcial
      p_total = p_total + p_pacial

      m_total = m_total + int(p_pacial/n_parcial)
      count = count + 1

  saida["media"] = [int(n_total/count),int(p_total/count),int(m_total)]
  saida["total_semestre"] = count
  saida["total_materia"] = count_materia

  return saida
