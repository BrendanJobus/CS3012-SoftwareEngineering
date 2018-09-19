import unittest

import LCA
from LCA import lcaFunction

class LCATestClass(unittest.TestCase):
	def testtest(self):
		self.assertEqual(lcaFunction(0), 0)

if __name__ == "__main__":
	unittest.main()
