class Graph():
    def __init__(self,n_nodes):
        self.size=n_nodes
        self.adj=[[0]*n_nodes for _ in range(n_nodes)]
        self.add_demand=[0 for _ in range(n_nodes)]

    def set_adj(self,matrix):
        self.adj=matrix
    
    def set_demand(self,demand):
        self.demand=demand
    
   