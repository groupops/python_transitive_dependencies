__author__ = 'Mateusz_Gawel'


class Storage:
    def __init__(self):
        self.items = []

    def add_direct(self, item_name, dependencies):

        temp_item = Item(item_name, set())
        if temp_item in self.items:
            for item_from_list in self.items:
                if item_from_list == temp_item:
                    temp_item = self.__modify_existing_item(item_from_list, dependencies)
                    break
        else:
            temp_item = self.__create_new_item(item_name, dependencies)
        return temp_item

    def dependencies_for(self, item):
        dependencies = set()
        dependencies_str = set()
        for item_from_list in self.items:
            if item_from_list.item_name == item:
                dependencies = item_from_list.get_dependencies()
                break
        for dependency in dependencies:
            dependencies_str.update(dependency.item_name)
        return dependencies_str

    def __modify_existing_item(self, item, dependencies):
        for dependency in dependencies:
            new_dep = self.add_direct(dependency, set())
            item.add_dependency(new_dep)
        return item

    def __create_new_item(self, item_name, dependencies):
        item = Item(item_name, set())
        for dependency in dependencies:
            new_dep = self.add_direct(dependency, set())
            item.add_dependency(new_dep)
        self.items.append(item)
        return item


class Item:
    def __init__(self, item_name, dependencies):
        self.item_name = item_name
        self.dependencies = dependencies

    def __eq__(self, other):
        return self.item_name == other.item_name

    def __hash__(self):
        return hash(self.item_name)

    def add_dependency(self, dependency):
        self.dependencies = self.dependencies | set([dependency])

    def get_dependencies(self):
        recursive_dependencies = set()
        for dependency in self.dependencies:
            recursive_dependencies = recursive_dependencies | set([dependency]) | dependency.get_dependencies()
        return recursive_dependencies
