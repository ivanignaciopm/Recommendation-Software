class Tree:
    def __init__(self, value) -> None:
        self.value = value
        self.children = []

    def add_child(self, child):
        if isinstance(child, Tree):
            self.children.append(child)
        else:
            print('Must be an instance')

    def remove_child(self, child):
        if child in self.children:
            self.children.remove(child)
        else:
            print("child not found")
            
    def __repr__(self) -> str:
        return f"{self.value}, {self.children}"