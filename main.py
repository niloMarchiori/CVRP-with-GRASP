from Models.GRASP import *
adj=[[0,51,32,15],
     [51,0,90,10],
     [32,90,0,18],
     [15,10,18,0]]

demand=[20,40,50,90]

k=1
max_capacity=120
max_iter=1
alpha=0.5

graph=Graph(len(demand))
graph.set_adj(adj)
graph.set_demand(demand)

solution_CVRP=GRASP(graph,max_capacity, max_iter,alpha)
print(solution_CVRP)