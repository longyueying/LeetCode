class Solution(object):
    res = []
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.res = []
        def solver( node, path):
            if node == len(graph)-1:
                path.append(node)
                self.res.append(path)
                return
            if len(graph[node])== 0:
                return
            path.append(node)
            for i in graph[node]:
                solver(i, path[:])

        solver(0, [])
        return self.res

if __name__=="__main__":
    solu = Solution()
    print(solu.allPathsSourceTarget([[1,2], [3], [3], []]))