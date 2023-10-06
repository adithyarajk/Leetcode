class RandomizedSet:

    def __init__(self):
        self.items = set()
        self.item_list = []

    def insert(self, val: int) -> bool:
        if val in self.items:
            return False
        else:
            self.items.add(val)
            self.item_list.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.items:
            self.items.remove(val)
            self.item_list.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.item_list)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()