def ler_semestre(local_arquivo):
  f = open(local_arquivo,'r')

  dados = f.readlines()

  saida = []

  for x in dados:
    ina = []
    if(x == " "):
      continue
    if('#' in x):
      continue
    if (x.count(" ") > 2):
      
      for espaco in range(0,x.count(" ")+1,2):
        dados_espaco = x.split(" ")

        if(dados_espaco[espaco] != ''):
          x1 = int(dados_espaco[0 + espaco])
          x2 = int(dados_espaco[1 + espaco])

          ina.append(x1,x2)

      saida.append(ina)
      
    else:
      x1 = int(x.split(" ")[0])
      x2 = int(x.split(" ")[1])
      ina = [x1,x2]
      saida.append(ina)

  return(saida)

#importando a funcao random para as mudanças na entrada.
from random import randint, shuffle
import random

def pm_random(count,entrada,nome_arq_saida='subida_encosta'):
  entrada = ler_semestre(entrada)
  saida = []


  saida = entrada
  random.shuffle(saida)

  # Escrever saida:
  f = open("Entrada\Subida\\"+nome_arq_saida+".txt","w+",encoding='utf-8')

  for x in saida:
    f.write(str(x[0])+" "+str(x[1])+"\n")
  
  f.close
  return saida

import os
import sys
import shutil

shutil.rmtree("Entrada\Subida", ignore_errors=False, onerror=None)
os.mkdir("Entrada\Subida")

# for x in range(10):
#   shutil.rmtree("Entrada\Subida"+str(x)+".txt", ignore_errors=False, onerror=None)
  # os.mkdir("Entrada\Subida"+str(x)+".txt")

shutil.rmtree("Saidas\\", ignore_errors=False, onerror=None)
os.mkdir("Saidas\\")
# print(pm_random(88,"Entrada\entrada.txt"))

#importando de analisar semestre.
from solucao_inicial import AnaliseSemestre

#importador de tempo, não é realmente necessario no algoritmo.
import datetime

x=datetime.datetime.now()
def EscreverRelatorioHTML(dic_saida):
  saida = []

  arq = open("Entrada/relatorio/relatorioIN.html","r+",encoding='utf-8')
  
  modelo = arq.read()
  # print(dic_saida)

  for x in range(len(dic_saida['teste_inicial'])):
    modelo = modelo.replace('%%sl'+str(x+1)+'%%',str(dic_saida['teste_inicial'][x]))
    modelo = modelo.replace('%%ss'+str(x+1)+'%%',str(dic_saida['subida_inicial'][x]))
    modelo = modelo.replace('%%sa'+str(x+1)+'%%',str(dic_saida['Subida_alternativa'][x]))

    modelo = modelo.replace('%%ts1'+str(x+1)+'%%',str(dic_saida['tempera_simulada1'][x]))
    modelo = modelo.replace('%%ts2'+str(x+1)+'%%',str(dic_saida['tempera_simulada2'][x]))
    modelo = modelo.replace('%%ts3'+str(x+1)+'%%',str(dic_saida['tempera_simulada3'][x]))
    
    modelo = modelo.replace('%%ag1'+str(x+1)+'%%',str(dic_saida['algoritmo_g1'][x]))
    modelo = modelo.replace('%%ag2'+str(x+1)+'%%',str(dic_saida['algoritmo_g2'][x]))
    modelo = modelo.replace('%%ag3'+str(x+1)+'%%',str(dic_saida['algoritmo_g3'][x]))
  
  #Solucao inicial 
  modelo = modelo.replace('%%quant_disc%%',str(dic_saida['dados_gerais']['quantidade_disciplinas']))
  
  # Subida de encosta
  modelo = modelo.replace('%%max_tentativa%%',str(dic_saida['dados_gerais']['Subida_alternativa']))
  
  # Tempera Simulada1
  modelo = modelo.replace('%%temp_init1%%',str(dic_saida['dados_gerais']['tempera_simulada1']['temp_init']))
  modelo = modelo.replace('%%temp_fim1%%',str(dic_saida['dados_gerais']['tempera_simulada1']['temp_fim']))
  modelo = modelo.replace('%%fr1%%',str(dic_saida['dados_gerais']['tempera_simulada1']['fr']))
 
   # Tempera Simulada2
  modelo = modelo.replace('%%temp_init2%%',str(dic_saida['dados_gerais']['tempera_simulada2']['temp_init']))
  modelo = modelo.replace('%%temp_fim2%%',str(dic_saida['dados_gerais']['tempera_simulada2']['temp_fim']))
  modelo = modelo.replace('%%fr2%%',str(dic_saida['dados_gerais']['tempera_simulada2']['fr']))
 
   # Tempera Simulada3
  modelo = modelo.replace('%%temp_init3%%',str(dic_saida['dados_gerais']['tempera_simulada3']['temp_init']))
  modelo = modelo.replace('%%temp_fim3%%',str(dic_saida['dados_gerais']['tempera_simulada3']['temp_fim']))
  modelo = modelo.replace('%%fr3%%',str(dic_saida['dados_gerais']['tempera_simulada3']['fr']))
 
  #Algoritmo Genitico 1
  modelo = modelo.replace('%%tp1%%',str(dic_saida['dados_gerais']['algoritmo_g1']['tp']))
  modelo = modelo.replace('%%tc1%%',str(dic_saida['dados_gerais']['algoritmo_g1']['tc']))
  modelo = modelo.replace('%%tm1%%',str(dic_saida['dados_gerais']['algoritmo_g1']['tm']))
  modelo = modelo.replace('%%ig1%%',str(dic_saida['dados_gerais']['algoritmo_g1']['ig']))
  modelo = modelo.replace('%%ng1%%',str(dic_saida['dados_gerais']['algoritmo_g1']['ng']))
   
  #Algoritmo Genitico 2
  modelo = modelo.replace('%%tp2%%',str(dic_saida['dados_gerais']['algoritmo_g2']['tp']))
  modelo = modelo.replace('%%tc2%%',str(dic_saida['dados_gerais']['algoritmo_g2']['tc']))
  modelo = modelo.replace('%%tm2%%',str(dic_saida['dados_gerais']['algoritmo_g2']['tm']))
  modelo = modelo.replace('%%ig2%%',str(dic_saida['dados_gerais']['algoritmo_g2']['ig']))
  modelo = modelo.replace('%%ng2%%',str(dic_saida['dados_gerais']['algoritmo_g2']['ng']))
   
  #Algoritmo Genitico 3
  modelo = modelo.replace('%%tp3%%',str(dic_saida['dados_gerais']['algoritmo_g3']['tp']))
  modelo = modelo.replace('%%tc3%%',str(dic_saida['dados_gerais']['algoritmo_g3']['tc']))
  modelo = modelo.replace('%%tm3%%',str(dic_saida['dados_gerais']['algoritmo_g3']['tm']))
  modelo = modelo.replace('%%ig3%%',str(dic_saida['dados_gerais']['algoritmo_g3']['ig']))
  modelo = modelo.replace('%%ng3%%',str(dic_saida['dados_gerais']['algoritmo_g3']['ng']))
   
  # print(modelo)

  # for y in modelo:
  #   saida.append(y)

  aqr_saida = open('saida_final.html',"w+",encoding='utf-8')

  aqr_saida.write(modelo)

  aqr_saida.close()

  os.system("start saida_final.html")

def EscreverRelatorio(solucao,titulo,nome_arquivo):
  #Salvando saida
  f = open("Saidas\\"+nome_arquivo+".txt","w+",encoding='utf-8')
  # f.write("#Solucao inicial, primeira saida ()\n")

  f.write("-"*50+"\n")
  f.write("|"+" "*17+titulo+" "*17+"|\n")
  f.write("-"*50+"\n")

  s_a = AnaliseSemestre(solucao)

  # count = 0
  total_semestre=0

  for zsss in solucao.keys():
      if(solucao[zsss] == []):
          continue
      else:
          f.write("| N:"+str(s_a[total_semestre][0])+" P:"+str(s_a[total_semestre][1])+" M:"+str(s_a[total_semestre][2])+" | >"+str(solucao[zsss])+" <| \n")
          total_semestre = total_semestre + 1
          # count = count + len(saida_inicial[zsss])
          # print(str(saida_inicial[zsss]))

  f.write("-"*50+"\n")
  f.write("|"+"-"*2+"Total de semestres: "+str(s_a['total_semestre'])+"; Total de Materias: "+str(s_a['total_materia'])+"-"*2+"|\n")
  f.write("-"*50+"\n")

  #Analise do curso

  f.write("| Média_N(S): "+str(s_a['media'][0])+" Média_P(S): "+str(s_a['media'][1])+" Média geral: "+str(s_a['media'][2])+" "*3+"|\n")

  f.write("-"*50+"\n")
  f.write("|"+" "*23+"FIM"+" "*22+"|\n")
  f.write("-"*50+"\n")

  f.write("Time:"+str(x))

  f.close

  return s_a

def criarLOADING():
    sys.stdout.write("[%s]" % (" " * 10))
    sys.stdout.flush()
    sys.stdout.write("\b" * (10+1)) # return to start of line, after '['

def addBarra():
    sys.stdout.write("-")
    sys.stdout.flush()

def fecharBarra():
    sys.stdout.write("]\n") # this ends the progress bar