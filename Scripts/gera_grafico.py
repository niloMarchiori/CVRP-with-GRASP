from Models.GRASP import update_costs,creat_RCL,random_include,Greedy_Randomized_Construction
from Models.solution import Solution
from Models.localsearch import local_search
from Models.graph import*
import vrplib
import matplotlib.pyplot as plt
import time

def GRASP_grafico(graph,max_capacity,alpha,neibors=[0,1]):

    best_solution=Solution(graph,max_capacity,cost=float('inf'))

    iter_count=0
    custos=[]
    b_bustos=[]
    inicio=time.time()
    while (time.time()-inicio)<=300:
        iter_count+=1
        curr_solution=Greedy_Randomized_Construction(graph,max_capacity,alpha)
        curr_solution=local_search(curr_solution,graph,neibors)
        custos.append(curr_solution.cost)
        if curr_solution.cost<best_solution.cost:
            best_solution=curr_solution
        b_bustos.append(best_solution.cost)
            

    return custos,b_bustos

def gera_grafico_An32k5():
    s=4
    instance = vrplib.read_instance('Instances/A/A-n32-k5.vrp')
    
    coment=instance['comment'].split()
    bks=int(coment[-1][:-1])

    for i in range(instance['dimension']):
        for j in range(i,instance['dimension']):
            instance['edge_weight'][i][j]=int(round(instance['edge_weight'][i][j]))
            instance['edge_weight'][j][i]=int(round(instance['edge_weight'][i][j]))
    
    graph=Graph(instance['dimension'])
    graph.set_adj(instance['edge_weight'])
    graph.set_demand(instance['demand'])
    max_capacity=instance['capacity']
    
    custos,b_custos=GRASP_grafico(graph,max_capacity,s)
    iteracoes=[x for x in range(len(custos))]

    fig, ax = plt.subplots()
    ax.scatter(iteracoes, custos, color='blue', linewidth=0.5,s=s)
    ax.scatter(iteracoes, b_custos, color='green', linewidth=0.8,s=s/2)

    ax.axhline(y=784, color='red', linestyle='--', linewidth=1, label='BKS*')

    ax.set_title('Evolução dos custos de cada soluão encontrada por iteração do GRASP', fontsize=14, fontname='Times New Roman')
    ax.set_xlabel('Iteração', fontsize=12, fontname='Times New Roman')
    ax.set_ylabel('Valor da função objetivo', fontsize=12, fontname='Times New Roman')
    ax.legend(fontsize=12, frameon=True)
    ax.grid(True, linestyle='--', linewidth=0.5)
    ax.tick_params(axis='both', labelsize=10)


    # Ajustando as fontes dos eixos
    plt.xticks(fontname='Times New Roman')
    plt.yticks(fontname='Times New Roman')

    plt.savefig("Output/Grafico/grafico.png", dpi=300)
    # Exibindo o gráfico
    plt.show()

    fig, ax = plt.subplots(figsize=(10, 5))

    # Criar hexbin plot (melhor para muitos pontos)
    hb = ax.hexbin(iteracoes,custos, gridsize=50, cmap='inferno', mincnt=1)

    # Adicionar barra de cores
    plt.colorbar(hb, label="Densidade de Pontos")
    ax.axhline(y=784, color='red', linestyle='--', linewidth=1, label='BKS*')

    ax.scatter(iteracoes, b_custos, color='green', linewidth=0.8,s=s/2)


    ax.set_title('Evolução dos custos de cada soluão encontrada por iteração do GRASP', fontsize=14, fontname='Times New Roman')
    ax.set_xlabel('Iteração', fontsize=12, fontname='Times New Roman')
    ax.set_ylabel('Valor da função objetivo', fontsize=12, fontname='Times New Roman')
    ax.legend(fontsize=12, frameon=True)
    ax.grid(True, linestyle='--', linewidth=0.5)
    ax.tick_params(axis='both', labelsize=10)


    # Ajustando as fontes dos eixos
    plt.xticks(fontname='Times New Roman')
    plt.yticks(fontname='Times New Roman')

    plt.savefig("Output/Grafico/grafico_heat.png", dpi=300)
    # Exibindo o gráfico
    plt.show()