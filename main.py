import os
import vrplib
from Models.GRASP import *
from time import time


def main():
    instance = vrplib.read_instance(f'A-n32-k5.vrp')
    
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
    max_iter=1000
    alpha=0.5

    for i in range(100):
        inicio=time()
        solution=GRASP(graph,max_capacity, max_iter,alpha)
        fim=time()
        # print('Tempo: ', (fim-inicio))
        print(solution)
        print(solution.cost)
        # print(f"Erro:  {(solution.cost-bks)/bks*100.:0f} ")
    
    

if __name__=='__main__':
    # main('./Instances_A/',k_max=10)
    main()
    