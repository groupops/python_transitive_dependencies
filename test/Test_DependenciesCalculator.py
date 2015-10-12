__author__ = 'Oleksandr_Kohut'

import unittest
from main.DependenciesCalculator import DependenciesCalculator

class TestCase(unittest.TestCase):
    if __name__ == '__main__':
        unittest.main()

    def test_basic(self):
      dep = DependenciesCalculator()
      dep.add_direct('A', ['B', 'C'])
      dep.add_direct('B', ['C', 'E'])
      dep.add_direct('C', ['G'])
      dep.add_direct('D', ['F'])
      dep.add_direct('E', ['F'])
      dep.add_direct('F', ['H'])

      self.assertEqual(['B', 'C', 'E', 'F', 'G', 'H'],      dep.dependencies_for('A'))
      self.assertEqual(['C', 'E', 'F', 'G', 'H'],           dep.dependencies_for('B'))
      self.assertEqual(['G'],                               dep.dependencies_for('C'))
      self.assertEqual(['F', 'H'],                          dep.dependencies_for('D'))
      self.assertEqual(['F', 'H'],                          dep.dependencies_for('E'))
      self.assertEqual(['H'],                               dep.dependencies_for('F'))
