from Models.solution import Solution
from Models.graph import Graph
from Models.solution import Solution
from Models.graph import Graph


def is_better(curr_cost:int,node_i:int,node_j:int,node_x:int,node_y:int,graph:Graph):
    economy_ij=graph.adj[node_i][node_j]
    economy_xy=graph.adj[node_x][node_y]

    cost_ix=graph.adj[node_i][node_x]
    cost_jy=graph.adj[node_j][node_y]
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
    cost_ix=graph.adj[node_i][node_x]
    cost_jy=graph.adj[node_j][node_y]

    solution.cost=solution.cost-economy_ij-economy_xy+cost_ix+cost_jy
    
    route_xj=route[x:i:-1]
    
    route[i+1:x+1]=route_xj

    
    route_xj=route[x:i:-1]
    
    route[i+1:x+1]=route_xj

    return solution

def two_opt(solution:Solution,graph:Graph):
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

def swap_move(solution:Solution,route_i_idx:int,node_i_idx:int,route_j_idx:int,node_j_idx:int,graph:Graph):
    route_i=solution.routes[route_i_idx]
    route_j=solution.routes[route_j_idx]

    node_j=route_j[node_j_idx]
    node_i=route_i[node_i_idx]


    free_cap_i=solution.free_capacity[route_i_idx]
    free_cap_j=solution.free_capacity[route_j_idx]
    demand_i=graph.demand[node_i]
    demand_j=graph.demand[node_j]
    
    if free_cap_i+demand_i-demand_j<0:
        return solution
    if free_cap_j+demand_j-demand_i<0:
        return solution


    node_bi=route_i[node_i_idx-1]
    node_ni=route_i[node_i_idx+1]

    node_bj=route_j[node_j_idx-1]
    node_nj=route_j[node_j_idx+1]

    economy_i=graph.adj[node_i][node_ni]+graph.adj[node_bi][node_i]
    economy_j=graph.adj[node_j][node_nj]+graph.adj[node_bj][node_j]

    cost_j=graph.adj[node_j][node_ni]+graph.adj[node_bi][node_j]
    cost_i=graph.adj[node_i][node_nj]+graph.adj[node_bj][node_i]
    if economy_i+economy_j<cost_i+cost_j:
        return solution
    solution.cost=solution.cost-economy_i-economy_j+cost_i+cost_j
    solution.free_capacity[route_i_idx]=free_cap_i+demand_i-demand_j
    solution.free_capacity[route_j_idx]=free_cap_j+demand_j-demand_i
    route_i[node_i_idx],route_j[node_j_idx]=node_j,node_i
    return solution
    
    
def swap(solution:Solution,graph:Graph):
    curr_cost=solution.cost
    for route_i in range(len(solution.routes)-1):
        for no_i in range(1,len(solution.routes[route_i])-1):
            for route_j in range(route_i+1,len(solution.routes)):
                for no_j in range(1,len(solution.routes[route_j])-1):
                    solution=swap_move(solution,route_i,no_i,route_j,no_j,graph)
                    if solution.cost<curr_cost:
                        return solution
    return solution

                    




def local_search(solution:Solution,graph:Graph):
    improvement_found = True
    curr_cost=solution.cost
    i=0
    neibor=[two_opt,swap]
    while improvement_found:
        solution=neibor[i](solution,graph)
        if curr_cost>solution.cost:
            improvement_found=True
            curr_cost=solution.cost
            i=0
        else:
            i+=1
            
        if i==len(neibor):
            improvement_found = False
       
        
            
    return solution

