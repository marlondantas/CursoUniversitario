#Importa o organizador de matriz e importa o gerador de disciplinas
from ler_semestre import *

#Importa a solução inicial
from solucao_inicial import * 

print("-"*50)
print("|"+" "*15+"Programa Iniciado"+" "*16+"|")
print("-"*50)

def Teste_inicial(ciclo):
    #Primeiro teste!

    disciplinas_usadas_top = ler_semestre("Entrada\entrada"+str(ciclo)+".txt")

    saida_inicial = CalcularBlocosSeparados(SepararBlocos(disciplinas_usadas_top),pontos)

    novo = AnaliseSemestre(saida_inicial)

    return novo
    # return EscreverRelatorio(saida_inicial,"Primeiro TESTE","solucao_inicial_"+str(ciclo))

def subida_Inicial(sol_inicial,ciclo):
    atual = sol_inicial
    entrada_atual = "Entrada\entrada"+str(ciclo)+".txt"

    flag = True
    count_melhora = 0
    
    while(flag):
        count_melhora = count_melhora + 1 

        #subida de encosta ou algo assim.
        disciplinas_subida = shuffleSemestres(ler_semestre("Entrada\entrada"+str(ciclo)+".txt")) 
        saida_subida = CalcularBlocosSeparados(SepararBlocos(disciplinas_subida),pontos)
        novo = AnaliseSemestre(saida_subida)
        if(novo["total_semestre"] >= atual["total_semestre"]):
            print("|"+" "*10+"Não foi possivel melhorar! +"+" "*10+"|")
            print("-"*50)
            flag = False
        else:
            novo = AnaliseSemestre(saida_subida)
            atual = novo
            entrada_atual = "Entrada\Subida\subida_encosta_ciclo"+str(ciclo)+"_"+str(count_melhora)+".txt"
            print("|"+" "*6+"Foi realizado um total de "+str(count_melhora)+" subidas!"+" "*6+"|")
    return (atual)

def subida_alternativa(sol_inicial,ciclo,max=5):
    atual = sol_inicial
    entrada_atual = "Entrada\entrada"+str(ciclo)+".txt"
    flag = True
    count_melhora = 0
    max_tentativa = max
    tentiva = 0
    while(flag):
        count_melhora = count_melhora + 1
        #subida de encosta ou algo assim.
        disciplinas_subida = shuffleSemestres(ler_semestre("Entrada\entrada"+str(ciclo)+".txt")) 
        saida_subida = CalcularBlocosSeparados(SepararBlocos(disciplinas_subida),pontos)
        novo = AnaliseSemestre(saida_subida)
        if(novo["total_semestre"] >= atual["total_semestre"]):
            print("|"+" "*10+"Não foi possivel melhorar!("+str(tentiva+1)+"/"+str(max_tentativa)+")"+" "*7+"|")
            tentiva = tentiva + 1
            if(tentiva == max_tentativa):
                flag = False
        else:
            novo = AnaliseSemestre(saida_subida)
            atual = novo
            tentiva = 0
            entrada_atual = "Entrada\Subida\subida_alternativa_ciclo"+str(ciclo)+str(count_melhora)+".txt"
            print("|"+" "*6+"Foi realizado um total de "+str(count_melhora)+" subidas!"+" "*6+"|")
    return (atual)

from math import exp as exp

def tempera_simulada(sol_inicial,ciclo,t_init,t_fim):
    print("Têmpera Simulada:",end='')
    criarLOADING()
    atual = sol_inicial
    entrada_atual = "Entrada\entrada"+str(ciclo)+".txt"
    temp = t_init
    fr = 0.9    
    count_melhora = 0
    while(temp > t_fim):
        if(count_melhora%10 == 0):
            addBarra()
        count_melhora = count_melhora + 1 
        disciplinas_subida = shuffleSemestres(ler_semestre(entrada_atual))
        saida_subida = CalcularBlocosSeparados(SepararBlocos(disciplinas_subida),pontos)
        novo = AnaliseSemestre(saida_subida)
        de = novo["total_semestre"] - atual["total_semestre"] 
        if(de < 0):
            atual = novo
        else:
            ale = random.uniform(0,1)
            valor = temp + 0
            aux = exp(de/valor)
            if(ale<aux):
                novo = AnaliseSemestre(saida_subida)
                atual = novo
            temp = temp * fr
    fecharBarra()
    return (atual)


from algoritmoGenetico import *
#variaveis globais:
pontos = 6

saidas={
    'teste_inicial':[],
    'subida_inicial':[],
    'Subida_alternativa':[],
    'tempera_simulada1':[],
    'tempera_simulada2':[],
    'tempera_simulada3':[],
    'algoritmo_g1':[],
    'algoritmo_g2':[],
    'algoritmo_g3':[],
    'dados_gerais':{
        'pontos':pontos,
        'quantidade_disciplinas':100,
        'Subida_alternativa':5,
        'tempera_simulada1':{
            'temp_init':9000,
            'temp_fim':1,
            'fr': 0.9,
        },
        'tempera_simulada2':{
            'temp_init':18000,
            'temp_fim':25,
            'fr': 0.9,
        },
        'tempera_simulada3':{
            'temp_init':36000,
            'temp_fim':50,
            'fr': 0.9,
        },
        'algoritmo_g1':{
            'tp':10,
            'tc':0.7,
            'tm':0.3,
            'ig':0.1,
            'ng':50,
        },
        'algoritmo_g2':{
            'tp':20,
            'tc':0.7,
            'tm':0.3,
            'ig':0.1,
            'ng':100,
        },
        'algoritmo_g3':{
            'tp':30,
            'tc':0.7,
            'tm':0.3,
            'ig':0.1,
            'ng':150,
        }
    },
}

# Desmarcar>
for x in range(10):

    print("Entrada: ",x)
    
    saidas['teste_inicial'].append(Teste_inicial(x)['total_semestre'])

    saidas['subida_inicial'].append(subida_Inicial(Teste_inicial(x),x)['total_semestre'])
    
    mx_t = saidas['dados_gerais']['Subida_alternativa']
    saidas['Subida_alternativa'].append(subida_alternativa(Teste_inicial(x),x,mx_t)['total_semestre'])

    for yy in range(3):
        # Têmpera simulada
        tempI = saidas['dados_gerais']['tempera_simulada'+str(yy+1)]['temp_init']
        tempf = saidas['dados_gerais']['tempera_simulada'+str(yy+1)]['temp_fim']
        total_semestre_tem_final = tempera_simulada(Teste_inicial(x),x,tempI,tempf)['total_semestre']
        saidas['tempera_simulada'+str(yy+1)].append(total_semestre_tem_final)

        #Algoritmo Génetico
        tp = saidas['dados_gerais']['algoritmo_g'+str(yy+1)]['tp']
        tc = saidas['dados_gerais']['algoritmo_g'+str(yy+1)]['tc']
        tm = saidas['dados_gerais']['algoritmo_g'+str(yy+1)]['tm']
        ig = saidas['dados_gerais']['algoritmo_g'+str(yy+1)]['ig']
        ng = saidas['dados_gerais']['algoritmo_g'+str(yy+1)]['ng']
        
        saidas['algoritmo_g'+str(yy+1)].append(algoritmo_genetico(tp,tc,tm,ig,ng,x,saidas['dados_gerais']['pontos'])[1])
        print("-"*50)
    # print(saidas)

EscreverRelatorioHTML(saidas)

# Finalizacao do programa

print("-"*50)
print("|"+" "*23+"FIM"+" "*22+"|")
print("-"*50)