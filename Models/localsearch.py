from Models.solution import Solution,Route
from Models.graph import Graph,Graph_Node

def acept_permute(node1,node2,solution):
    pass
def local_search(solution:Solution,graph:Graph):
    best_solution = solution
    improvement_found = True

    while improvement_found:
        improvement_found = False
        for node_00 in solution.NODES:
            for node_10 in solution.NODES:
                if node_00==node_10 or node_00.next==node_10:
                    continue
                node_01=node_00.next
                node_11=node_10.next
            

    return best_solution
