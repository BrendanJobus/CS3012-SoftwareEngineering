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
			return False

	def _find(self, val, node):
		if val == node.value:
			return True
		elif val < node.value:
			if node.left != None:
				self._find(val, node.left)
			else:
				return False
		elif val > node.value:
			if node.right != None:
				self._find(val, node.right)
			else:
				return False

	def toString(self):
		if self.root != None:
			return(self._toString(self.root))

	def _toString(self, node):
		treestring = ''
		if node != None:
			treestring += self._toString(node.left)
			treestring += str(node.value) + ' '
			treestring += self._toString(node.right)
		return treestring


	def lca(self, nodeValues):
		if len(nodeValues) == 0 or self.root == None:
			return None
		moveleft = False
		moveright = False
		for value in nodeValues:
			if self.find(value) == False:
				return None
			if value < self.root.value:
				moveleft = True
			elif value > self.root.value:
				moveright = True

		if moveleft == moveright:
			return self.root.value
		if moveleft == True:
			return self._lca(self.root.left, nodeValues)
		if moveright == True:
			return self._lca(self.root.right, nodeValues)

	def _lca(self, root, nodeValues):
		moveleft = False
		moveright = False
		for value in nodeValues:
			if value < root.value:
				moveleft = True
			elif value > root.value:
				moveright = True

		if moveleft == moveright:
			return root.value
		if moveleft == True:
			return self._lca(root.left, nodeValues)
		if moveright == True:
			return self._lca(root.right, nodeValues)
