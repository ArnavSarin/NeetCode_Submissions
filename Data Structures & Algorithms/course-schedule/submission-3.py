class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #CREATE ADJACENCY MATRICES 
        matrix = defaultdict(list)

        for i in prerequisites:
            matrix[i[0]].append(i[1])
           
        print(matrix)
        stack = []
        seen = set()

        for course in range(numCourses):
            stack.append((course,[course]))
            print(course)
            while len(stack)>0:
                course_num, course_path = stack.pop()

                if course_num in seen:
                    break

                for i in matrix[course_num]:
                    if i in course_path:
                        return False
                    else:
                        stack.append((i,course_path+[i]))

                seen.add(course_num)

        return True
                                
            










        return True