
class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        x = self.storage[0]
        self.storage[0] = self.storage[len(self.storage) - 1]
        del self.storage[len(self.storage) - 1]
        self._sift_down(0)
        return x

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        while index > 0:
            p = (index - 1) // 2
            if self.storage[index] > self.storage[p]:
                self.storage[index], self.storage[p] = self.storage[p], self.storage[index]
            index = p

    def _sift_down(self, index):
        while index * 2 + 1 <= len(self.storage) - 1:
            left = index * 2 + 1
            right = index * 2 + 2
            if right > len(self.storage) - 1 or self.storage[left] > self.storage[right]:
                big = left
            else:
                big = right
            if self.storage[index] < self.storage[big]:
                self.storage[index], self.storage[big] = self.storage[big], self.storage[index]
                index = big
            else:
                break
