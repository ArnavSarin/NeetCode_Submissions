class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        matrix = defaultdict(list)

        for i in edges:
            matrix[i[0]].append(i[1])
            matrix[i[1]].append(i[0])

        seen = set()
        queue = deque()
        count = 0
        for i in range(n):
            queue.append((i,-1))
            if queue[0][0] not in seen:
                count += 1

            while len(queue)>0:
                node, parent = queue.popleft()

                for j in matrix[node]:
                    if j not in seen and j != parent:
                        queue.append((j,node))

                seen.add(node)

        return count
