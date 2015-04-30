class Histogram:

    def __init__(self):
        self.histogram = {}


    def add(self, server):
        if server not in self.histogram:
            self.histogram[server] = 1
        else:
            self.histogram[server] += 1

    def count(self, server):
        if server not in self.histogram:
            return 0
        return self.histogram[server]


    def get_dict(self):
        return self.histogram
