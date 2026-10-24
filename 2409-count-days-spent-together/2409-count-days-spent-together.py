class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        to_day = lambda d: sum(days[:int(d[:2])]) + int(d[3:])
        return max(0, to_day(min(leaveAlice, leaveBob)) - to_day(max(arriveAlice, arriveBob)) + 1)