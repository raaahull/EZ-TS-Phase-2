def kruskals(graph):
    pass

graph={
    'A':[(1,'B'),(3,'E')],
    'B':[(1,'A'),(2,'E'),(1,'D'),(4,'C')],
    'C':[(4,'B'),(1,'D')],
    'D':[(1,'B'),(1,'C'),(2,'E')],
    'E':[(3,'A'),(2,'B'),(2,'D')] 
    }


mst = kruskals(graph)
print(mst)