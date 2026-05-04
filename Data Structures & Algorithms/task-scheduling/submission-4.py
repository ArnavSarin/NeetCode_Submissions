class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hm = Counter(tasks)
        task_frequency = [(-i[1],i[0]) for i in hm.items()]
        heapq.heapify(task_frequency)

        queue = deque()
        time = 0

        while task_frequency or queue:

            while queue and queue[0][0] <= time:
                _, frequency, task = queue.popleft()
                heapq.heappush(task_frequency, (frequency, task))

            if task_frequency:
                frequency, task = heapq.heappop(task_frequency)

                if -frequency > 1:
                    queue.append((time+n+1,frequency+1,task))

            time += 1

        return time
