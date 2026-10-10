"""
input:
    2D int array - grid
        grid[i] - 0(empty)
                  1(fresh  fruit)
                  2(rotten fruit)

output:
    int - min num of minutes until 0 fresh fruits returning
    if impossible, -1

if 1 horizontal/vertically adj to 2, then 1 becomes 2 every minute.

so from every rotten fruit, BFS
    each level out would be minute elapsing

Hmm. 

When would that be impossible?

1 0 1
0 2 0
1 0 1

oh I see if rotten has no adj fresh, then rotten won't infect any

so should return -1

this case will only ever happen if for every rotten fruit node, there are no adjacent fruits.

so just check after the first loop in bfs after seeding. if no neighbors added, return -1

else start counting minutes?

no.. because you could have rotten adj to fresh but if there exists a fresh that is isolated then always its -1

So.

So first check if there exists any fresh fruit that has no connections at all. 
    if that's true then return -1

so while doing that, 
    find the rotten fruit
    can also just check if the rotten fruit has no connections

if every rotten fruit has no connections
    return -1

actually. can just track fresh fruit count at start
decrement count as they turn rotten

if fruit count != 0 after msbfs return -1
else min_minutes




"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        min_minutes = 0
        q = deque()
        visited = set()

        fresh_fruit = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):

                if val == 2:
                    q.append((r, c))
                    visited.add((r, c))
                
                if  val == 1:
                    fresh_fruit += 1
        
        
        while q and fresh_fruit > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    if 0 <= r + dr < rows and 0 <= c + dc < cols and grid[r + dr][c + dc] == 1:
                        grid[r + dr][c + dc] = 2
                        fresh_fruit -= 1
                        visited.add((r, c))
                        q.append((r + dr, c + dc))
            
            min_minutes += 1

        return min_minutes if fresh_fruit == 0 else -1



