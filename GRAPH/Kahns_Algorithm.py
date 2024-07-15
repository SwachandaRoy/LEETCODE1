class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        adj=defaultdict(list)
        indegree=defaultdict(int)
        for preq in prerequisites:
            adj[preq[1]].append(preq[0])
            indegree[preq[0]]+=1
        queue=[]
        visited=0
        for i in range(numCourses):
            if indegree[i] == 0:
               queue.append(i)

        while queue:
            node=queue.pop(0)
            visited+=1
            for neighbor in adj[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
        return numCourses==visited

