class MyCalendarTwo:
    def __init__(self):
        self.bookings = []
        self.overlaps = []

    def book(self, startTime: int, endTime: int) -> bool:
        # Check if the new interval overlaps with existing double bookings
        for s, e in self.overlaps:
            if max(s, startTime) < min(e, endTime):
                return False

        # Record new overlaps with existing single bookings
        for s, e in self.bookings:
            if max(s, startTime) < min(e, endTime):
                self.overlaps.append((max(s, startTime), min(e, endTime)))

        self.bookings.append((startTime, endTime))
        return True  


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)