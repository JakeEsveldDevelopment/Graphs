f = open('words.txt', 'r')
words = f.read().split("\n")

word_set = set()
for word in words:
    word_set.add(word.lower())

def get_neighbors(word):
    neighbors = []
    string_word = list(word)
    for i in range(len(string_word)):
        for letter in list("abcdefghijklmnopqrstuvwxyz"):
            temp_word = list(string_word)
            temp_word[i] = letter
            w = "".join(temp_word)
            if w != word and w in word_set:
                neighbors.append(w)
    return neighbors

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


def find_word_ladder(beginWord, endWord):
    queue = Queue()
    visited = set()
    queue.enqueue([beginWord])

    while queue.size() > 0:
        path = queue.dequeue()
        vertex = path[-1]
        if vertex not in visited:
            if vertex == endWord:
                return path
            visited.add(vertex)
            for new_vert in get_neighbors(vertex):
                new_path = list(path)
                new_path.append(new_vert)
                queue.enqueue(new_path)

print(find_word_ladder("sail", "boat"))