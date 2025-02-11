from Models.linkedlist import *

class Graph():
    def __init__(self,n_nodes):
        self.size=n_nodes
        self.NODES=[None for _ in range(n_nodes)]
        self.adj=[[0]*n_nodes for _ in range(n_nodes)]
        self.creat_nodes()

    def set_adj(self,matrix):
        self.adj=matrix
    
    def add_demand(self,demand,costumer):
        self.NODES[costumer].demand=demand
    
    def set_demand(self,demand_list):
        for costumer in range(len(demand_list)):
            self.add_demand(demand_list[costumer],costumer)

    def creat_nodes(self):
        for n in range(self.size):
            self.NODES[n]=Graph_Node(n)
    
class Graph_Node(Node):
    def __init__(self,node_ID=0,demand=0):
        super().__init__(node_ID)
        self.demand=demand
        self.route=None
        
    def copy_node(self):
        node_ID=self.node_ID
        demand=self.demand
        return Graph_Node(node_ID,demand)

   