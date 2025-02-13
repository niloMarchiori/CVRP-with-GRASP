from Models.solution import Solution
from Models.graph import Graph

def is_better(curr_cost:int,node_i:int,node_j:int,node_x:int,node_y:int,graph:Graph):
    economy_ij=graph.adj[node_i][node_j]
    economy_xy=graph.adj[node_x][node_y]

    cost_ix=graph.adj[node_i][node_x]
    cost_jy=graph.adj[node_j][node_y]

    new_cost=curr_cost-economy_ij-economy_xy+cost_ix+cost_jy

    if new_cost<curr_cost:
        return True
    return False

def move_two_opt(solution:Solution,route:list,i:int,x:int,graph:Graph):
    node_i=route[i]
    node_j=route[i+1]
    node_x=route[x]
    node_y=route[x+1]
    economy_ij=graph.adj[node_i][node_j]
    economy_xy=graph.adj[node_x][node_y]

    cost_ix=graph.adj[node_i][node_x]
    cost_jy=graph.adj[node_j][node_y]

    solution.cost=solution.cost-economy_ij-economy_xy+cost_ix+cost_jy
    
    route_xj=route[x:i:-1]
    
    route[i+1:x+1]=route_xj

    return solution

def two_opt(solution:Solution,graph:Graph):
    n=graph.size
    for route in solution.routes:
        for i in range(1,len(route)-3):
            node_i=route[i]
            node_j=route[i+1]
            
            for x in range(i+2,len(route)-1):
                node_x=route[x]
                node_y=route[x+1]
                curr_cost=solution.cost
                if not(is_better(curr_cost,node_i,node_j,node_x,node_y,graph)):continue
                solution=move_two_opt(solution,route,i,x,graph)
                return solution
    return solution
    

def local_search(solution:Solution,graph:Graph):
    improvement_found = True
    curr_cost=solution.cost
    i=0
    while improvement_found:
        improvement_found = False
        solution=two_opt(solution,graph)
        if curr_cost>solution.cost:
            improvement_found=True
            curr_cost=solution.cost
            
            
        i+=1
        
            
    return solution

