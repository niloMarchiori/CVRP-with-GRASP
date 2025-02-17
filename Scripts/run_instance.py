import vrplib
from Models.GRASP import *


def run_instance(instancia:str,alpha=0.35,max_iter=50000,neibors=[0,1],n_iter=5,draw=False):

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
    
    dados={'Instance_name':instance['name'],'BKS':bks,
           'Best_cost':float('inf'),'Avrg_cost':0,
           'Best_temp':0,'Avrg_temp':0,
           'Best_gap':0,'Avrg_gap':0}
    avrg_temp=0
    avrg_cost=0
    avrg_gap=0

    best_solution=Solution(graph,max_capacity,cost=float('inf'))

    for i in range(n_iter):
        solution,curr_temp=GRASP(graph,max_capacity, max_iter,alpha,neibors,draw)
        avrg_temp+=curr_temp
        avrg_gap+=(solution.cost-bks)/bks
        avrg_cost+=solution.cost

        if solution.cost<dados['Best_cost']:
            dados['Best_cost']=solution.cost
            dados['Best_temp']=curr_temp
            dados['Best_gap']=(solution.cost-bks)/bks
            best_solution=solution

    dados['Avrg_cost']=round(avrg_cost/n_iter,4)
    dados['Avrg_temp']=round(avrg_temp/n_iter,4)
    dados['Avrg_gap']=round(avrg_gap/n_iter,4)
    
    if draw:
        print('------------------ Solução final -------------------')
        print(f'''Instância: {instance['name']}''')
        print(best_solution)
        print('----------------------------------------------------')

    return dados
    
    

if __name__=='__main__':
    print(run_instance('A-n32-k5.vrp'))