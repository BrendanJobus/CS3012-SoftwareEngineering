def lcaFunction(tree, nodes):
	if len(nodes) == 0:
		return None
	for node in nodes:
		#print(node)
		if tree.find(node) == None:
			return None
	return -1
