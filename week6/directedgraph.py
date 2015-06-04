class DirectedGraph:

    def __init__(self):
        self.network = {}

    def __iter__(self):
        return iter(self.network)

    def __getitem__(self, user):
        return self.network[user]

    def has_node(self, node):
        return node in self.network

    def add_edge(self, node_a, node_b):

        if not self.has_node(node_a):
            self.network[node_a] = []

        if not self.has_node(node_b):
            self.network[node_b] = []

        if node_b not in self.network[node_a]:
            self.network[node_a].append(node_b)

    def add_node(self, node_a):
        if not self.has_node(node_a):
            self.network[node_a] = []

    def get_neighbors_for(self, node):
        if not self.has_node(node):
            raise KeyError("No such node in DirectedGraph")
        return self.network[node]

    def path_between(self, start, end, path=[]):

        if not self.has_node(start) or not self.has_node(end):
            return False

        path.append(start)
        if start == end:
            return True

        for node in self.network[start]:
            if node not in path:
                newpath = self.path_between(node, end, path)
                if newpath:
                    return True
        return False

    def get_path_between(self, start, end, path=[]):

        if not self.has_node(start) or not self.has_node(end):
            return None

        path.append(start)
        if start == end:
            return path

        for node in self.network[start]:
            if node not in path:
                newpath = self.get_path_between(node, end, path)
                if newpath:
                    return newpath
        return None


    def pprint(self):
        for node in self.network:
            print (node, self.network[node])
