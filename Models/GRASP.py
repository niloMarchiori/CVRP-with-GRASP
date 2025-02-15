import random as rd
from Models.graph import Graph
from Models.solution import Solution
from Models.localsearch import local_search
import time


def update_costs(graph:Graph,solution:Solution, candidates:list):
    max_cost=0
    min_cost=float('inf')
    route=solution.routes[-1]
    last_node=route[-1]

    free_capacity=solution.free_capacity[-1]

    for next_node in range(graph.size):
        demand=graph.demand[next_node]
        full= (free_capacity-demand)<0
        if candidates[next_node] and not full:
            if max_cost<graph.adj[last_node][next_node]:
                max_cost=graph.adj[last_node][next_node]

            if min_cost>graph.adj[last_node][next_node]:
                min_cost=graph.adj[last_node][next_node]

    include_costs={'min_cost':min_cost,'max_cost':max_cost}
    
    return include_costs
        
def creat_RCL(include_costs:dict,graph:Graph,solution:Solution,candidates:list,alpha:float):
    min_cost=include_costs['min_cost']
    max_cost=include_costs['max_cost']
    
    RCL=[]
    
    route=solution.routes[-1]
    last_node=route[-1]

    for next_node in range(graph.size):
        if not candidates[next_node]: continue
        if solution.free_capacity[-1]-graph.demand[next_node]<0: continue
        if graph.adj[last_node][next_node]<=(min_cost+alpha*(max_cost-min_cost)):
            RCL.append(next_node)
    return RCL

def random_include(RCL:list,candidates:list,solution:Solution,graph:Graph):
    i=rd.randint(0,len(RCL)-1)
    choosed_node=RCL[i]
    candidates[choosed_node]=False
    # INICO TESTE -----------------------
    # global lista
    # node_ID= lista.pop(0)
    # choosed_node=solution.NODES[node_ID]
    # candidates[choosed_node.node_ID]=False
    # FIM TESTE   -----------------------

    solution.insert_node(choosed_node,graph)
    


def Greedy_Randomized_Construction(graph:Graph,max_capacity:int,alpha:float):
    candidates=[True for _ in range(graph.size)]
    solution=Solution(graph,max_capacity)
    candidates[0]=False
    include_costs=update_costs(graph,solution,candidates)
    n=1
    while n<graph.size:
        if include_costs['max_cost']==0:
            solution.new_route()
            include_costs=update_costs(graph,solution,candidates)

        RCL=creat_RCL(include_costs,graph,solution,candidates, alpha)
        random_include(RCL,candidates,solution,graph)
        n+=1
        include_costs=update_costs(graph,solution,candidates)

    for route in range(len(solution.routes)):
        solution.insert_node(0,graph,route)

    return solution

# # INICO TESTE -----------------------
# lista=[14,6,2,4,22,18,28,3,23,8,29,27,1,21,31,17,13,19,20,15,11,9,25,10,5,24,26,16,30,12,7]
# FIM TESTE   -----------------------
def GRASP(graph,max_capacity, max_iter,alpha):

    best_solution=Solution(graph,max_capacity,cost=float('inf'))
    inicio=time.time()

    iter_count=0
    temp_best=0
    for _ in range(max_iter) or (time.time()-inicio)>300:
        
        curr_solution=Greedy_Randomized_Construction(graph,max_capacity,alpha)
        curr_solution=local_search(curr_solution,graph)
        if curr_solution.cost<best_solution.cost:
            best_solution=curr_solution
            temp_best=time.time()-inicio
        iter_count+=1

    return best_solution,temp_best,iter_count