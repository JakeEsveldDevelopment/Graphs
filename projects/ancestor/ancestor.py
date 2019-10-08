
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

    ancestorsList = {}

    for node in ancestors:
        if node[1] not in ancestorsList:
            ancestorsList[node[1]] = set()
        ancestorsList[node[1]].add(node[0])

    if starting_node not in ancestorsList:
        return -1

    queue = Queue()
    visited = []
    queue.enqueue([starting_node])
    latest_ancestor = None
    biggest_gap = 0
    while queue.size() > 0:
        path = queue.dequeue()
        vert = path[-1]
        if vert not in ancestorsList:
            if len(path) > biggest_gap:
                biggest_gap = len(path)
                latest_ancestor = vert
            elif len(path) == biggest_gap and vert < latest_ancestor:
                    latest_ancestor = vert            
        if vert not in visited:
            visited.append(vert)
            if vert in ancestorsList:
                for ancestor in ancestorsList[vert]:
                    new_path = list(path)
                    new_path.append(ancestor)
                    queue.enqueue(new_path)

    return latest_ancestor