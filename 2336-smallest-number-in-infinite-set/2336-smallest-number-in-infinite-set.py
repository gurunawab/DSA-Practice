class SmallestInfiniteSet:

    def __init__(self):
        self.cur, self.s = 1, set()

    def popSmallest(self) -> int:
        res = min(self.s) if self.s else self.cur
        if self.s: self.s.remove(res)
        else: self.cur += 1
        return res

    def addBack(self, num: int) -> None:
        if num < self.cur:
            self.s.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)