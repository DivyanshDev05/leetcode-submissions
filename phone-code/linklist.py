class Node:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Node({self.data})"


if __name__ == '__main__':
    n = Node("hello")
    print(n)
