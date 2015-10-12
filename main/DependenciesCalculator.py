__author__ = 'Oleksandr_Kohut'

class DependenciesCalculator():

    def __init__(self):
        self.dependencies = {}

    def add_direct(self, item, dependencies):
        self.dependencies.update({item: dependencies})
        for dependency in self.dependencies.keys():
            dependentValues = self.dependencies.get(dependency)
            for dependentValue in dependentValues:
                if dependentValue == item:
                    dependentValues.extend(dependencies)
                    dependentValues = sorted(set(dependentValues))
                    self.dependencies.update({dependency: dependentValues})
        print ("===")
        print (self.dependencies)

    def dependencies_for(self, item):
        return self.dependencies.get(item)