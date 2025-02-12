from Models.graph import *
from Models.linkedlist import *

class Route(Linkedlist):
    def __init__(self,max_capacity,head=None,tail=None):
        '''Cria uma rota, inicia ela depósito sendo o primeiro node'''
        super().__init__(head,tail)
        self.max_capacity=max_capacity
        self.free_capacity=max_capacity
        node0=Graph_Node(0,0)
        self.add_node(node0)

    def new_costumer(self,node:Graph_Node):
        self.add_node(node)
        node.route=self
        self.free_capacity-=node.demand
        pass

class Solution():
    def __init__(self,graph:Graph ,max_capacity:int,cost=0):
        self.max_capacity=max_capacity
        self.routes = [Route(self.max_capacity)]
        self.cost=cost
        self.NODES= Solution.creat_nodes(graph)

    def insert_node(self,node:Graph_Node, graph:Graph,route=None):
        '''Insere o nó 'node' à rota 'route' '''
        # route=self.routes[k]

        if not route:
            route=self.routes[-1]
        route.new_costumer(node)
        last_node=route.tail
        self.cost+=graph.adj[last_node.back.node_ID][last_node.node_ID]
    
    def new_route(self):
        self.routes.append(Route(self.max_capacity))

    
    def __str__(self):
        op=''
        for route in range(len(self.routes)):
            # op+=f'rota {route}:'
            op+=str(self.routes[route])
            op+='\n'
        # op+=f'Custo total: {self.cost}\n'
        return op
    
    @staticmethod
    def creat_nodes(graph:Graph):
        NODES=[ node.copy_node() for node in graph.NODES]
        return NODES



    
