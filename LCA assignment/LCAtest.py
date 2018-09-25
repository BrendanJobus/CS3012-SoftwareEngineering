import unittest
from Tree import BinaryTree


class LCATestClass(unittest.TestCase):
	def testEmptyGraph(self):
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

if __name__ == "__main__":
	unittest.main()
