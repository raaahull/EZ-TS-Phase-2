class Graph:
    def _init_(self,num_of_nodes,directed=True):
        self.m_num_of_nodes=num_of_nodes
        self.m_nodes=range(slf.m_num_of_nodes)
        self.m_directed=directed
        self.m_adj_list=(node, set() for node in self.m_nodes)

    def add_edge(self,node1,node2,node3,weight=1):
        self.m_adj_list[node1]
        add((node2,weight))
        if not self.m_directed:
            self.m_adj_list[node2]
            add((node1,weight))
    def print_adj_list(self):
        for key in self.m_adj_list.keys():
            print("node",key, ":",self.m_adj_list(key))

graph=Graph(5)
graph.add=edge(0,0,25)
graph.add=edge(0,1,5)
graph.add=edge(0,2,3)
graph.add=edge(1,3,1)
graph.add=edge(1,4,15)
graph.add=edge(4,2,7)
graph.add=edge(4,3,11)

graph.print_adj_list()