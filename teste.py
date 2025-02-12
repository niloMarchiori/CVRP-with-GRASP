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

    adj=instance['edge_weight']
    lista=[0,21,31,19,17,13,7,26,0,0,12,1,16,30,0,0,27,24,0,0,29,18,8,9,22,15,10,25,5,20,0,0,14,28,11,4,23,3,2,6,0]
    sum=0
    for i in range(len(lista)-1):
        a=lista[i]
        b=lista[i+1]
        if b ==0 and a==0:
            print(sum)
        sum+=adj[a][b]
    print(sum)
    
    

if __name__=='__main__':
    # main('./Instances_A/',k_max=10)
    main()
    