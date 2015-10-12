__author__ = 'Oleksandr_Kohut'

class DependenciesCalculator():

    def __init__(self):
        self.dependencies = []

    def add_direct(self, item, dependencies):
            for item in dependencies:
                self.dependencies[item, dependencies]

    def dependencies_for(self, item):
        for item in self.dependencies:
            return item[1]