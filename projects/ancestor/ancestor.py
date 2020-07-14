# intital test: 
# 
# Ran 1 test in 0.000s

# FAILED (failures=1)

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    q = Queue()

    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        g.add_vertex(parent)
        g.add_vertex(child)
        g.add_edge(child, parent)

    q.enqueue([starting_node])

    longest_path_length = 1
    earliest_ancestor = -1

    while q.size() > 0:
        path = q.dequeue()
        current_node = path[-1]

        if len(path) >= longest_path_length and current_node < earliest_ancestor or len(path) > longest_path_length:
            longest_path_length = len(path)
            earliest_ancestor = current_node

        # if len(path) > longest_path_length:
        #     longest_path_length = len(path)
        #     earliest_ancestor = current_node

        neighbors = g.vertices[current_node]
        for ancestor in neighbors:
            path_copy = list(path)
            path_copy.append(ancestor)
            q.enqueue(path_copy)

    return earliest_ancestor