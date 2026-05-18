class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        egress_matrix = defaultdict(list)
        indegrees = [0]* numCourses

        for i in prerequisites:
            egress_matrix[i[1]].append(i[0])
            indegrees[i[0]] += 1

        queue, path = deque(), []

        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        seen = set()

        while len(queue) > 0:
            course = queue.popleft()

            if course in seen:
                break
            
            path.append(course)
            seen.add(course)

            for i in egress_matrix[course]:
                indegrees[i] -= 1

                if indegrees[i] == 0:
                    queue.append(i)


        if len(path) == numCourses:
            return path
        
        return []


            