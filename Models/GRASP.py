import random as rd
from Models.graph import Graph,Graph_Node
from Models.solution import Solution
from Models.linkedlist import Linkedlist
import time


def update_costs(graph:Graph,solution:Solution, candidates:list):
    max_cost=0
    min_cost=float('inf')
    route=solution.routes[-1]
    last_node=route.tail

    free_capacity=route.free_capacity

    for next_node_ID in range(graph.size):
        demand=graph.NODES[next_node_ID].demand
        full= (free_capacity-demand)<=0
        if candidates[next_node_ID] and not full:
            if max_cost<graph.adj[last_node.node_ID][next_node_ID]:
                max_cost=graph.adj[last_node.node_ID][next_node_ID]

            if min_cost>graph.adj[last_node.node_ID][next_node_ID]:
                min_cost=graph.adj[last_node.node_ID][next_node_ID]

    include_costs={'min_cost':min_cost,'max_cost':max_cost}
    
    return include_costs
        
def creat_RCL(include_costs:dict,graph:Graph,solution:Solution,candidates:list,alpha:float):
    min_cost=include_costs['min_cost']
    max_cost=include_costs['max_cost']
    
    RCL=[]
    
    last_node=solution.routes[-1].tail

    for node in solution.NODES:
        if not candidates[node.node_ID]: continue
        if graph.adj[last_node.node_ID][node.node_ID]<=(min_cost+alpha*(max_cost-min_cost)):
            RCL.append(node)
    return RCL

def random_include(RCL:list,candidates:list,solution:Solution,graph:Graph):
    # InicioTESTE------------------------
    # seed = rd.randint(0,2**30)
    # seed=148046798
    # rd.seed(seed)
    # print(seed)
    # FIMTESTE------------------------

    i=rd.randint(0,len(RCL)-1)
    choosed_node=RCL[i]

    # choosed_node=RCL[i]
    # candidates[choosed_node.node_ID]=False
    # InicioTESTE------------------------

    global lista
    i=lista.pop(0)
    choosed_node=solution.NODES[i]
    candidates[i]=False
    # FIMTESTE---------------------------


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
        # ===================
        # print(solution)
        # ===================
        n+=1
        include_costs=update_costs(graph,solution,candidates)

    for route in solution.routes:
        solution.insert_node(Graph_Node(0,0),graph,route)

    return solution

def Local_Search(solution):
    return solution

lista=[]
def GRASP(graph,max_capacity, max_iter,alpha):

    best_solution=Solution(graph,max_capacity,cost=float('inf'))
    inicio=time.time()
    # while (time.time()-inicio)<=300:
    for _ in range(max_iter):
        # ==========================
        global lista
        lista=[21,31,19,17,13,7,26,12,1,16,30,27,24,29,18,8,9,22,15,10,25,5,20,14,28,11,4,23,3,2,6]
        # ==========================
        curr_solution=Greedy_Randomized_Construction(graph,max_capacity,alpha)
        curr_solution=Local_Search(curr_solution)
        # print(f'__________________ Iteração {_} __________________')
        # print(curr_solution)
        if curr_solution.cost<best_solution.cost:
            best_solution=curr_solution

    return best_solution