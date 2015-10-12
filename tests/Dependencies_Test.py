import unittest
from Dependencies import Dependencies

class Dependencies_Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Dependencies_Test, self).__init__(*args, **kwargs)
        self.depend = Dependencies()

    def runTest(self):
        self.depend.add_direct('A', 'B')
        self.depend.add_direct('B', 'C')
        self.depend.add_direct('C', 'A')
        print self.depend.dependencies_set
        self.assertTrue('B' in self.depend.dependencies_set)
        self.assertTrue('C' in self.depend.dependencies_set)
        self.assertTrue('A' in self.depend.dependencies_set)
