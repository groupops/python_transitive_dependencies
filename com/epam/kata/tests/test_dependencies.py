from unittest import TestCase
from com.epam.kata import Dependencies

__author__ = 'Mateusz_Gawel'


class TestDependencies(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestDependencies, self).__init__(*args, **kwargs)
        self.dep = Dependencies.Storage()

    def test_add_direct(self):
        self.dep.add_direct('A', ['B', 'C'])
        self.dep.add_direct('B', ['C', 'E'])
        self.dep.add_direct('C', ['G'])
        self.dep.add_direct('D', ['A', 'F'])
        self.dep.add_direct('E', ['F'])
        self.dep.add_direct('F', ['H'])

        self.assertEquals(set(['B', 'C', 'E', 'F', 'G', 'H']), self.dep.dependencies_for('A'))
        self.assertEquals(set(['C', 'E', 'F', 'G', 'H']), self.dep.dependencies_for('B'))
        self.assertEquals(set(['G']), self.dep.dependencies_for('C'))
        self.assertEquals(set(['A', 'B', 'C', 'E', 'F', 'G', 'H']), self.dep.dependencies_for('D'))
        self.assertEquals(set(['F', 'H']), self.dep.dependencies_for('E'))
        self.assertEquals(set(['H']), self.dep.dependencies_for('F'))

    def test_cycle_dependencies(self):
        self.dep.add_direct('A', ['B'])
        self.dep.add_direct('B', ['C'])
        self.dep.add_direct('C', ['A'])

        self.assertEquals(set(['B']), self.dep.dependencies_for('A'))
        self.assertEquals(set(['C']), self.dep.dependencies_for('B'))
        self.assertEquals(set(['A']), self.dep.dependencies_for('C'))
