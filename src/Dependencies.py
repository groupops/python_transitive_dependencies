class Dependencies:
    def __init__(self):
        self.dependencies_set = set();

    def add_direct(self, item, item_dependencies):
        list = item_dependencies.split(" ")
        for itemm in list:
            self.dependencies_set.add(itemm);

    def dependencies_for(self, item, item_dependencies):
        for item in self.dependencies_set:
            item.add_direct(item, item_dependencies)
