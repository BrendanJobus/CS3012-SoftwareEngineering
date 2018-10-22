import unittest
from Tree import BinaryTree

import networkx as netx
from DAG import lcaForDAG as lca


class DAGTestClass(unittest.TestCase):
	def testEmptyDAG(self):
		g = netx.DiGraph()
		self.assertEqual(lca(g, 1, 2), None)

	def testNodesNotPresent(self):
		g = netx.DiGraph()
		g.add_nodes_from([1,2,3,4])
		self.assertEqual(lca(g, 7, 8), None)

	def testNotAcyclic(self):
		g = netx.DiGraph()
		g.add_nodes_from([1,2,3])
		g.add_edges_from([(1,2), (2,3), (3,1)])
		self.assertEqual(lca(g, 1, 2), None)

	def testRegularDAG(self):
		g = netx.DiGraph()
		g.add_nodes_from([1,2,3,4,5,6,7])
		g.add_edges_from([(1,2), (1,4), (2,3), (3,6), (4,5), (5,6), (6,7)])
		self.assertEqual(lca(g, 3, 4), 1)

	def testNoCommonAncestor(self):
		g = netx.DiGraph()
		g.add_nodes_from([1,2,3,4])
		g.add_edges_from([(1,2), (3,4)])
		self.assertEqual(lca(g, 2, 3), None)

	def testLCAisNode(self):
		g = netx.DiGraph()
		g.add_nodes_from([1,2,3,4])
		g.add_edges_from([(1,2), (2,3), (3,4)])
		self.assertEqual(lca(g, 2, 3), 2)


class LCATestClass(unittest.TestCase):
	def testEmptyTree(self):
		g = BinaryTree()
		self.assertEqual(g.lca([1]), None)

	def testEmptyNodeList(self):
		g = BinaryTree()
		g.add(5)
		g.add(2)
		g.add(4)
		self.assertEqual(g.lca([]), None)

	def testRegular(self):
		g = BinaryTree()
		g.add(5)
		g.add(2)
		g.add(4)
		g.add(8)
		g.add(7)
		g.add(0)
		#			 5
		#		  /	    \
		#		2		 8
		#	  /	  \	   /
		#	0	   4 7
		self.assertEqual(g.lca([0, 4]), 2)
		self.assertEqual(g.lca([0, 4, 7]), 5)

	def testSingleNode(self):
		g = BinaryTree()
		g.add(5)
		g.add(2)
		g.add(4)
		g.add(8)
		g.add(7)
		g.add(0)
		self.assertEqual(g.lca([5, 2]), 5)
		self.assertEqual(g.lca([7, 8]), 8)

if __name__ == "__main__":
	unittest.main()
