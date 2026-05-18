class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        egress_matrix = defaultdict(list)
        indegrees = [0] * numCourses

        for course in prerequisites:
            egress_matrix[course[1]].append(course[0])
            indegrees[course[0]] += 1
            
        path, queue = [], deque()
        for course in range(numCourses):
            if indegrees[course] == 0:
                queue.append(course)

        seen = set()
        while len(queue)> 0:
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
            