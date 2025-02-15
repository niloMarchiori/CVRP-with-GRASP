from Models.graph import *





class Solution():
    def __init__(self,graph:Graph ,max_capacity:int,cost=0):
        self.max_capacity=max_capacity
        self.routes = [[0]]
        self.free_capacity=[self.max_capacity]
        self.cost=cost
        self.candidates= [False for _ in range(graph.size)]
        self.candidates= [False for _ in range(graph.size)]

    
    def insert_node(self,node:int, graph:Graph,route=-1):
        '''Insere o nó 'node' à rota 'route' '''
      
        last_node=self.routes[route][-1]
        self.cost+=graph.adj[last_node][node]
        self.routes[route].append(node)
        self.free_capacity[route]-=graph.demand[node]
      
        last_node=self.routes[route][-1]
        self.cost+=graph.adj[last_node][node]
        self.routes[route].append(node)
        self.free_capacity[route]-=graph.demand[node]
    
    def new_route(self):
        self.routes.append([0])
        self.free_capacity.append(self.max_capacity)

        self.routes.append([0])
        self.free_capacity.append(self.max_capacity)

    def __str__(self):
        op=''
        for route in self.routes:
            for node in route:
                op+=str(node)+' '
        for route in self.routes:
            for node in route:
                op+=str(node)+' '
            op+='\n'
        op+=f'Custo total: {self.cost}\n'
        op+=f'Custo total: {self.cost}\n'
        return op


    
