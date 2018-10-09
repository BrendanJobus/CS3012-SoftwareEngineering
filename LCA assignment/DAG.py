import networkx as netx

def lcaForDAG(DAG, a, b):
	if( DAG.size() == 0 ):
		return None
	if( not netx.is_directed_acyclic_graph(DAG) ):
		return None
	nodes = DAG.nodes()
	if( a not in nodes or b not in nodes):
		return None

	
