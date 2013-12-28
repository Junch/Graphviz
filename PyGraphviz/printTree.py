import unittest
import pygraphviz as pgv

class TestMath(unittest.TestCase):
	def testG1(self):
		A=pgv.AGraph(directed=True,strict=True)
		A.add_edge(1,2)
		A.add_edge(1,3)
		A.add_edge(2,4)
		A.add_edge(2,5)
		A.add_edge(5,6)
		A.add_edge(5,7)
		A.add_edge(3,8)
		A.add_edge(3,9)
		A.add_edge(8,10)
		A.add_edge(8,11)
		A.graph_attr['epsilon']='0.001'
		print A.string() # print dot file to standard output
		A.write('fooOld.dot')
		A.layout('dot') # layout with dot
		A.draw('fooOld.png') # write to file

if __name__ == '__main__':
	unittest.main()
