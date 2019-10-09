import random

class User:
    def __init__(self, name):
        self.name = name

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

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()
        

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        for n in range(numUsers):
            self.addUser(n)
        
        for n in range(1, numUsers):
            rand = random.randint(1, avgFriendships * 2)
            for i in range(rand):
                randUser = random.randint(1, numUsers)
                if n == i:
                    continue
                if self.friendships[randUser] != None and n in self.friendships[randUser]:
                    continue
               
                self.addFriendship(n, randUser)

        # Add users

        # Create friendships

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        doneList = list()
        queue = Queue()
        queue.enqueue([userID])
        while queue.size() > 0:
            path = queue.dequeue()
            vert = path[-1]
            if len(path) - 1 not in visited:
                visited[len(path) - 1] = set()
            if vert not in doneList:               
                visited[len(path) - 1].add(vert)
                doneList.append(vert)
                for next in self.friendships[vert]:
                    next_path = list(path)
                    next_path.append(next)
                    queue.enqueue(next_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print("CONNECTIONS FOR 1")
    print(connections)
    connections = sg.getAllSocialPaths(2)
    print("CONNECTIONS FOR 2")
    print(connections)
    connections = sg.getAllSocialPaths(3)
    print("CONNECTIONS FOR 3")
    print(connections)
