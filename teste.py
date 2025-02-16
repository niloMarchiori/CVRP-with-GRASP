import vrplib
from Models.GRASP import *
from time import time
from Scripts.run_instance import run_instance
from Scripts.read_dir import read_dir
import pandas as pd

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
    
    dados={'Instance_name':instance['name'],'BKS':bks,
           'Best_cost':float('inf'),'Avrg_cost':0,
           'Best_temp':0,'Avrg_temp':0,
           'Best_gap':0,'Avrg_gap':0,
           'n_iter':0}
    avrg_temp=0
    avrg_cost=0
    avrg_n_iter=0
    avrg_gap=0
    for i in range(5):
        inicio=time()
        solution,curr_temp,n_iter=GRASP(graph,max_capacity, max_iter,alpha,neibors)
        fim=time()
        avrg_temp+=curr_temp
        avrg_cost+=solution.cost
        avrg_n_iter+=n_iter
        avrg_gap+=(solution.cost-bks)/bks

        if solution.cost<dados['Best_cost']:
            dados['Best_cost']=solution.cost
            dados['Best_temp']=fim-inicio
            dados['Best_gap']=(solution.cost-bks)/bks
       
    

    dados['Avrg_cost']=avrg_cost/5
    dados['n_iter']=avrg_n_iter/5
    dados['Avrg_temp']=avrg_temp/5
    dados['Avrg_gap']=avrg_gap/5

    return dados


def main():
    for X in ['A','B','F']:
        instances_path=read_dir(f'Instances/{X}')
        rows=[]
        ##MUDAR DA MAIN CERTA===========
        df=pd.DataFrame(columns=['Instance_name','BKS','Best_cost','Avrg_cost','Best_temp','Avrg_temp','Best_gap','Avrg_gap','n_iter'])
        ##==============================
        for instance in instances_path:
            dados=run_instance(f'Instances/{X}/{instance}',max_iter=10000)
            rows.append(dados)
        df = pd.concat([df, pd.DataFrame(rows)], ignore_index=True)
        # print(df)
        df.to_csv(f"Output/Instance_{X}/out_{X}.csv", index=False)
if __name__=='__main__':
    main()
