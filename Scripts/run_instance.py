import vrplib
from Models.GRASP import *
from time import time


def run_instance(instancia:str,alpha=0.35,max_iter=50000,neibors=[0,1]):

    instance = vrplib.read_instance(instancia)
    
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
    
    dados={'Instance_name':instance['name'],'BKS':bks, 'Custo':0,'Tempo':0,'Best_temp':0,'n_iter':0,'Erro':0}
    avrg_temp=0
    avrg_custo=0
    avrg_best_temp=0
    avrg_n_iter=0
    avrg_err=0
    for i in range(5):
        inicio=time()
        solution,best_temp,n_iter=GRASP(graph,max_capacity, max_iter,alpha,neibors)
        # print(solution)
        fim=time()
        avrg_temp+=fim-inicio
        avrg_custo+=solution.cost
        avrg_best_temp+=best_temp
        avrg_n_iter+=n_iter
        avrg_err+=(solution.cost-bks)/bks
        # print(f"Erro:  {(solution.cost-bks)/bks*100:.0f} ")
        print(instance['name'],'OK')
    

    dados['Bes_tempo']=avrg_best_temp/5
    dados['Custo']=avrg_custo/5
    dados['n_iter']=avrg_n_iter/5
    dados['Tempo']=avrg_temp/5
    dados['Erro']=avrg_err/5

    return dados


        # print('alpha:',alpha)
        # print('Tempo: ', (fim-inicio))
        # print(solution)
        # print(solution.cost)
    
    

if __name__=='__main__':
    print(run_instance('A-n32-k5.vrp'))