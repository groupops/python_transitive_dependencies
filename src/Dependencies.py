class Dependencies(object):
    directDependencies = {}

    def __init__(self):
        pass

    @classmethod
    def add_direct(item, top, dependencies):
        item.directDependencies[top] = dependencies

    @classmethod
    def dependencies_for(item, top):
        list_of_dependencies = set()
        while top in item.directDependencies:
            current_elements = set(item.directDependencies[top])
            list_of_dependencies |= set(current_elements)
            for i, val in enumerate(current_elements):
                top = val
                list_of_dependencies |= set(item.dependencies_for(val))
        return sorted(list(list_of_dependencies))