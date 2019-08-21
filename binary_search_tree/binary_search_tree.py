class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        elif self.right is None:
            return False
        else:
            if self.left:
                if self.left.contains(target):
                    return True
            if self.right:
                if self.right.contains(target):
                    return True

    def get_max(self):
        while self.right is None:
            return self.value
        else:
            return self.right.get_max()

    def for_each(self, cb):
        if self.left:
            self.left.for_each(cb)
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
