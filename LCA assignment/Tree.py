class Node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.value = val

class BinaryTree:
	def __init__(self):
		self.root = None

	def add(self, val):
		if self.root == None:
			self.root = Node(val)
		else:
			self._add(val, self.root)

	def _add(self, val, node):
		if val < node.value:
			if node.left != None:
				self._add(val, node.left)
			else:
				node.left = Node(val)
		elif val > node.value:
			if node.right != None:
				self._add(val, node.right)
			else:
				node.right = Node(val)

	def find(self, val):
		if self.root != None:
			return self._find(val, self.root)
		else:
			return None

	def _find(self, val, node):
		if val == node.value:
			return node
		elif val < node.value:
			if node.left != None:
				self._find(val, node.left)
			else:
				return None
		elif val > node.value:
			if node.right != None:
				self._find(val, node.right)
			else:
				return None

	def toString(self):
		if self.root != None:
			return(self._printTree(self.root))

	def _printTree(self, node):
		treestring = ''
		if node != None:
			treestring += self._printTree(node.left)
			treestring += str(node.value) + ' '
			treestring += self._printTree(node.right)
		return treestring


	def lca(self, nodes):
		if len(nodes) == 0:
			return None
		for node in nodes:
			if tree.find(node) == None:
				return None
		return -1
