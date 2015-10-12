class Dependencies(object):
    directDependencies = {}

    def __init__(self):
        pass

    @classmethod
    def sorted_transitive_dependencies_for(cls, top):
        list_of_dependencies = set()
        while top in cls.directDependencies:
            current_elements = set(cls.directDependencies[top])
            list_of_dependencies |= set(current_elements)
            for i, val in enumerate(current_elements):
                top = val
                list_of_dependencies |= set(cls.sorted_transitive_dependencies_for(val))
        return sorted(list(list_of_dependencies))

    @classmethod
    def add_direct(cls, top, dependencies):
        cls.directDependencies[top] = dependencies
