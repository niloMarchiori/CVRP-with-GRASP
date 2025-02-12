from Models.solution import Solution,Route
from Models.graph import Graph,Graph_Node

def is_better(curr_cost:int,node_i:Graph_Node,node_x:Graph_Node,graph:Graph):
    node_j=node_i.next
    node_y=node_x.next

    
    economy_ij=graph.adj[node_i.node_ID][node_j.node_ID]
    economy_xy=graph.adj[node_x.node_ID][node_y.node_ID]

    cost_ix=graph.adj[node_i.node_ID][node_x.node_ID]
    cost_jy=graph.adj[node_j.node_ID][node_y.node_ID]

    new_cost=curr_cost-economy_ij-economy_xy+cost_ix+cost_jy

    if new_cost<curr_cost:
        return True
    return False

def move_two_opt(solution:Solution,node_i:Graph_Node,node_x:Graph_Node,graph:Graph):
    node_j=node_i.next
    node_y=node_x.next

    economy_ij=graph.adj[node_i.node_ID][node_j.node_ID]
    economy_xy=graph.adj[node_x.node_ID][node_y.node_ID]

    cost_ix=graph.adj[node_i.node_ID][node_x.node_ID]
    cost_jy=graph.adj[node_j.node_ID][node_y.node_ID]

    node_i.next=node_x
    node_x.next=node_x
    node_x.reverse=True

    node_y.back=node_j
    node_j.back=node_y
    node_j.reverse=True


    solution.cost=solution.cost-economy_ij-economy_xy+cost_ix+cost_jy
    return solution

def two_opt(solution:Solution,graph:Graph):
    n=graph.size
    for i in range(n-3):
        node_i=solution.NODES[i]
        for x in range(i+2,n-1):
            node_x=solution.NODES[x]
            curr_cost=solution.cost
            if not (node_i.route is node_x.route): continue
            if not(is_better(curr_cost,node_i,node_x,graph)):continue
            solution=move_two_opt(solution,node_i,node_x,graph)
            return solution
    return solution
    

def local_search(solution:Solution,graph:Graph):
    improvement_found = True
    curr_cost=solution.cost
    while improvement_found:
        improvement_found = False
        solution=two_opt(solution,graph)
        if curr_cost>solution.cost:
            improvement_found=True
        
            
    return solution

