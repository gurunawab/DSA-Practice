class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited, stack = {0}, [0]
        while stack:
            visited.update(k for k in rooms[stack.pop()] if k not in visited and not stack.append(k))
        return len(visited) == len(rooms)