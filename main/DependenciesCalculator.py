__author__ = 'Oleksandr_Kohut'

class DependenciesCalculator():

    def __init__(self):
        self.dependencies = {}

    def add_direct(self, item, dependencies):
        self.dependencies.update({item: dependencies})

    def dependencies_for(self, item):
        return self.dependencies.get(item)