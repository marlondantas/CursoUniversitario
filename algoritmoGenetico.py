from math import ceil
import random

#Importa o organizador de matriz e importa o gerador de disciplinas
from ler_semestre import *

#Importa a solução inicial
from solucao_inicial import * 

def pop_inicial(tp,ciclo,pontos):
    """
    Criar a população inicial do algoritmo!

    tp = Tamanho da população;
    ciclo = Número da entrada do sistema;
    potnos = Maximo de pontos por semestre.
    """
    pop = []

    for x in range(tp):
        entrada_atual = "Entrada\entrada"+str(ciclo)+".txt"
        disciplinas = shuffleSemestres(ler_semestre(entrada_atual))
        saida = CalcularBlocosSeparados(SepararBlocos(disciplinas),pontos)
        pop.append(saida)
    
    return pop

def checkAutenticidade(curso, max_pon):
    """
    Calcula os semestre que estão completou ou não.

    curso = Lista ou dicionario do semestre a ser analisado;
    max_pon = O total de pontos por semestre;
    """
    # Verificar os semestres repetidos.
    if(type(curso) == dict):
        if(curso == {}):
            return {'dados':"Sem sucesso!!!"}

        lista_negra = []
        semestresvalidos = []
        cursos_cadastrados = []
        for x in curso.keys():
            if(curso[x] == []):
                continue

            total_pontos = 0
            cont = 0

            for y in curso[x]:
                if(total_pontos > max_pon or total_pontos + int(y[0]) > max_pon or y in cursos_cadastrados):
                    lista_negra.append(y)
                    continue
                else:
                    cursos_cadastrados.append(y)
                    total_pontos = total_pontos + int(y[0])
                cont = cont + 1
                
            if(cont == len(curso[x])):
                if(total_pontos == max_pon):
                    semestresvalidos.append(curso[x])
                elif(total_pontos < max_pon):
                    lista_negra.extend(curso[x])
            
        return semestresvalidos, lista_negra
    else:
        tranforme = {}
        cont = 0

        for x in curso:
            tranforme['AQUI0e'+str(cont)] = x
            cont = cont + 1

        return checkAutenticidade(tranforme,max_pon)

def apidao(pop,tp):
    """
    CAlcula a relevancia de cada populacao.

    pop = A lista de população;
    tp = Tamanho da população.
    """
    f = []
    soma = 0

    for i in range(tp):
        verdadeiroT = 0 
        if(type(pop[i]) == dict):
            for x in pop[i].keys():
                if(pop[i][x]):
                    verdadeiroT = verdadeiroT + 1
        elif(type(pop[i]) == list):
            for x in pop[i]:
                if(x):
                    verdadeiroT = verdadeiroT + 1
        f.append(1/verdadeiroT)
        soma += f[i]
    
    for i in range(tp):
        f[i] = f[i]/soma
    
    return f

def CRUZARmentoEspecial(pop,pop1,pontos = 6):
    '''
    Cruza duas populações.

    pop = População pai;
    pop1 = População Filho;
    pontos = maximo de pontos por semestre.
    '''

    sn  = checkAutenticidade(pop,pontos)
    sn1 = checkAutenticidade(pop1,pontos)
    
    ids, idsfilhos, todas_materiasP = [], [], []
    
    for x in sn[0]:
        todas_materiasP.append(x)
        for z in range(len(x)):
            ids.append(x[z][1])
    
    ids.sort()        

    for x in sn1[0]:
        todas_materiasP.append(x)
        for z in range(len(x)):
            idsfilhos.append(x[z][1])

    todas_materiasP = sorted(todas_materiasP, key=len)
    idsfilhos.sort()        

    repetidosIDS = []

    for x in ids:
        for y in idsfilhos:
            if(x == y):
                repetidosIDS.append(x)

    saidas,materiasavulsa = [],[]

    if(len(repetidosIDS) == 0):
        materiasNPerfeitas = []
        materiasNPerfeitas.extend(sn[1])
        materiasNPerfeitas.extend(sn1[1])

        saidas.extend(sn[0])
        saidas.extend(sn1[0])

        materiasSalva = []

        for semestre in saidas:
            for materia in semestre:
                materiasSalva.append(materia)

        listaFinal = [xy for xy in materiasSalva if x not in materiasNPerfeitas]

        semestresRestantes = CalcularBlocosSeparados(SepararBlocos(listaFinal),6)

        for semestre in semestresRestantes.keys():
            if(semestresRestantes[semestre] == []):
                continue
            shuffle(shuffleSemestres[semestre])
            saidas.append(semestresRestantes[semestre])
    else:
        for semestre in todas_materiasP:
            temRepetido = False
            
            for materia in semestre:
                if(materia[1] in repetidosIDS):
                    temRepetido = True

            if(temRepetido == False):
                saidas.append(semestre)
               
        listaFinal = [xy for xy in todas_materiasP if xy not in saidas]

        for x in repetidosIDS:
            referenetaoX = []

            for semestre in listaFinal:
                semestreconfere = False
                for materia in semestre:
                    if(materia[1] == x):
                        semestreconfere = True
                if(semestreconfere == True):
                    referenetaoX.append(semestre)
            
            if(len(referenetaoX) > 0):
                saidas.append(referenetaoX[0])
    materiasavulsa.extend(sn[1])
    materiasavulsa.extend(sn1[1])

    t = []
    [ t.append(item) for item in materiasavulsa if not t.count(item) ]
    materiasavulsa = t

    materiasSalva = []

    for semestre in saidas:
        for materia in semestre:
            materiasSalva.append(materia)

    materiasavulsa = [xy for xy in materiasavulsa if xy not in materiasSalva]
    
    novossemestrekeys =  CalcularBlocosSeparados(SepararBlocos(materiasavulsa),pontos)
    novossemestre = []

    for keys in novossemestrekeys.keys():
        if(novossemestrekeys[keys] == []):
            continue
        novossemestre.append(novossemestrekeys[keys])

    saidas.extend(novossemestre)
    return saidas

def cruzamento(pop,fit,tc,tp,pontos = 6):
    """
    Organiza o cruzamento do individos.

    pop = Lista da população;
    fit = Influencia de cada menbro da população;
    tc = Taxa de cruzamento;
    tp = Tamanho da população;
    pontos = Pontos máximo por semestre.
    """
    qc= ceil(tp*tc)

    desc = []
    for x in range(qc):
        soma = 0
        j=0

        ale = random.uniform(0,1)
        while soma < ale:
            soma = soma + fit[j]
            j = j + 1
        
        p1 = j-1

        ale = random.uniform(0,1)
        while soma < ale:
            soma = soma + fit[j]
            j = j + 1
            
        p2 = j-1

        #descendente 1 :
        desc.append(CRUZARmentoEspecial(pop[p1],pop[p2]))

        #descendente 2:
        desc.append(CRUZARmentoEspecial(pop[p2],pop[p1]))
    return desc

def mutacao(pop,tm,tp,pontos):
    # TODO Ainda tem que ser feito!
    # Quantidade de mutacao
    qm = ceil(tp*tm)
    
    qd = len(pop)

    # Executa a mutacao
    saida = []
    for i in range(qm):
        
        #Descente
        ind = random.randrange(0,qd)

        sn = checkAutenticidade(pop[ind],pontos)

        curso = []
        curso = sn[0]

        novossemestrekeys =  CalcularBlocosSeparados(SepararBlocos(sn[1]),pontos)
        novossemestre = []

        for keys in novossemestrekeys.keys():
            if(novossemestrekeys[keys] == []):
                continue
            novossemestre.append(novossemestrekeys[keys])

        curso.extend(novossemestre)

        saida.append(curso)

    return saida
# ROTINA NOVA POPULAÇÃO
def nova_pop(pop,desc,ig):
    """
    Calcula os melhores membros para uma nova população

    pop = Lista de população;
    desc = Lista de descendentes;
    ig = Intervalo de geração.
    """
    superPop = []
    superPop.extend(desc)
    superPop.extend(pop)

    superPopT = []

    for xyx in superPop:
        tamanho = 0
        if(type(xyx) == dict):
            for x in xyx.keys():
                if(xyx[x]):
                    tamanho = tamanho + 1
        elif(type(xyx) == list):
            for x in xyx:
                if(x):
                    tamanho = tamanho + 1

        superPopT.append([tamanho,xyx])

    superPop = sorted(superPopT, key=lambda x: x[0])

    saida = []

    for x in range(len(pop)):
        saida.append(superPop[x][1])

    return saida

import sys


def algoritmo_genetico(tp,tc,tm,ig,ng,clico,pontos):
    '''
    tp = tamanaho da população
    tc = taxa de cruzamento
    tm = taxa de mutação
    ig = intervalo de geração
    ng = número de gerações
    '''
    print("Algoritmo Genetico: ",end='')
    criarLOADING()
    pop = []
    fit = []
    desc = []
    fit_d = []
    # Gera a população inicial.
    pop = pop_inicial(tp,clico,6)
    for t in range(ng):
        if(((t*100)/ng)%10 == 0):
            addBarra()
        fit = apidao(pop,tp)
        # Inicia o cruzamento gerando descendentes
        desc = cruzamento(pop,fit,tc,tp,pontos)
        # Inicia a mutacao
        desc.append(mutacao(pop,tm,tp,pontos))
        fit_d = apidao(desc,10)
        pop_list = []
        for x in range(len(pop)):
            pop_list.append([fit[x],pop[x]])
        sorted_zippedlist = sorted(pop_list, key=lambda x: x[0]) 
        pop_list = [element for _, element in sorted_zippedlist]
        zipped_list = zip(fit_d,desc)
        sorted_zippedlist = sorted(zipped_list) 
        desc = [element for _, element in sorted_zippedlist]
        pop = nova_pop(pop,desc,ig)
        Leitura = checkAutenticidade(pop[0],6)
    tamanho = 0
    if(type(pop[0]) == dict):
        for xyx in pop[0]:
            if(pop[0][xyx]):
                tamanho = tamanho + 1
    elif(type(pop[0]) == list):
        for x in pop[0]:
            if(x):
                tamanho = tamanho + 1
    fecharBarra()
    return pop[0], tamanho

# result = algoritmo_genetico(11,0.7,0.3,0.1,10,9,6)
# print("Total de Semestres:",result[1])
