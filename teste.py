import vrplib
from Models.GRASP import *
from time import time
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
        solution,curr_temp,n_iter=GRASP(graph,max_capacity, max_iter,alpha,neibors)
        avrg_temp+=curr_temp
        avrg_n_iter+=n_iter
        avrg_gap+=(solution.cost-bks)/bks
        avrg_cost+=solution.cost

        if solution.cost<dados['Best_cost']:
            dados['Best_cost']=solution.cost
            dados['Best_temp']=curr_temp
            dados['Best_gap']=(solution.cost-bks)/bks
            # print(instance['name'])
            # print(solution)
            # print("bTempo:", dados['Best_temp'],"bGap",dados['Best_gap'])
       
    

    dados['Avrg_cost']=round(avrg_cost/5,2)
    dados['n_iter']=round(avrg_n_iter/5,2)
    dados['Avrg_temp']=round(avrg_temp/5,2)
    dados['Avrg_gap']=round(avrg_gap/5,2)

    return dados


def main():
    for X in ['A','B','F']:
        instances_path=read_dir(f'Instances/{X}')
        rows=[]
        ##MUDAR DA MAIN CERTA===========
        df=pd.DataFrame(columns=['Instance_name','BKS','Best_cost','Avrg_cost','Best_temp','Avrg_temp','Best_gap','Avrg_gap','n_iter'])
        ##==============================
        for instance in instances_path:
            try:
                dados=run_instance(f'Instances/{X}/{instance}',alpha=0.1,max_iter=10000,neibors=[0,1])
                rows.append(dados)
                print(instance, 'OK')
            except:
                break
        df = pd.concat([df, pd.DataFrame(rows)], ignore_index=True)
        # print(df)
        df.to_csv(f"Output/Instance_{X}/out_{X}.csv", index=False)
if __name__=='__main__':
    main()
