class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        matrix = defaultdict(list)

        for i in edges:
            matrix[i[0]].append(i[1])
            matrix[i[1]].append(i[0])

        queue = deque()

        seen = set()

        queue.append((0,-1))

        while len(queue) > 0:
            node, parent = queue.popleft()

            if node in seen:
                return False

            for j in matrix[node]:
                if j != parent:
                    queue.append((j, node))

            seen.add(node)

        return len(seen) == n


       

        
