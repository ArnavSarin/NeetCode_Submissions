class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hm = Counter(tasks)
        task_frequency = [(-i[1],i[0])for i in hm.items()]
        print(hm)
        print(task_frequency)
        heapq.heapify(task_frequency)

        queue = []

        time = 0
        while len(task_frequency) > 0 or len(queue) > 0:
            print("GOT HERE 0")
            print(task_frequency)
            print(queue)

            while queue and queue[0][0]<= time:
                    deadline, frequency, task_name = queue.pop(0)
                    heapq.heappush(task_frequency,(frequency,task_name))

            if len(task_frequency) > 0:
                frequency, task_name = heapq.heappop(task_frequency)

                if (-frequency) > 1:
                    queue.append((time+n+1,frequency+1,task_name))

            time += 1
        return time
