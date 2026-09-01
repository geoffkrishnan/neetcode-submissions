"""
input:
    tasks - int array
        tasks[i] - [A, Z]
        length - [1, 1000]
    
    n - int
        range [0, 100]
    

output:
    min # of CPU cycles to complete all tasks


constraints:
    identical tasks must be seperated by AT LEAST n( >= n) CPU cycles
    can idle for 1 CPU cycle
    can be completed in any order
    each task costs 1 CPU cycle


example:
    [X, X, Y, Y] n = 2

    [X Y idle X Y]

can make a freq map

X - 2
Y - 2

decrement 1 from both and you get 2 cycles

how do we figure out the distance between a task and how many cycles it's been


ok we process X. costs 1 cycle

next we see X again. so we idle 2 then x so that's 3 so that'll be 4

then y idle 2 then y again that'll be 8 total cycles. but that's not the minimum.

ok. 

so freq map X and Y

we do X and costs 1 and we remove 1 then we go to Y costs 1 and remove.


idk man im confused how does a heap help here?

knowing the max/min doesn't help us know the distance between dupes?? does it? im confused

To minimize CPU cycles, we always start with distinct tasks first

what if we have

[A, A, A, B, B, C] n = 2

A-B-C-A-B-idle-A

so gotta do most frequent first

then how do we track the actual CPU cycles

so what do we want,

we do the distincts.

then we want to wait until n cycles have passed before continuing to add more tasks

so we want to know at which cycle a task was actually used on.

the next most close cycle that task can be perfomed again at will be the cycle at which task was performed + n

so we want to like go by most frequent first

so start with freq map

then order based on freq. can use a max heap i guess.

"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = []
        queue = deque()
        cpu_cycle = 0

        for task, freq in Counter(tasks).items():
            max_heap.append((freq, task))
        
        heapq.heapify_max(max_heap)

        while max_heap or queue:
            if max_heap:
                freq, task = heapq.heappop_max(max_heap)
                freq -= 1
                task_tuple = freq, task
                if freq > 0:
                    queue.append((task_tuple, cpu_cycle))

            cpu_cycle += 1

            if queue and cpu_cycle >= queue[0][1] + n + 1:
                task_tuple, _ = queue.popleft()
                heapq.heappush_max(max_heap, task_tuple)
            
        return cpu_cycle