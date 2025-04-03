class Solution:

    # Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        # code here
        visited = [False] * len(adj)
        stack = []
        result = []
        stack.append(0)
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                result.append(node)
                for i in range(len(adj[node]) - 1, -1, -1):
                    if not visited[adj[node][i]]:
                        stack.append(adj[node][i])
        return result


    # code here


if __name__ == "__main__":
    s = Solution()
    adj = [[1, 2, 4], [0], [0, 3], [2, 4], [0, 3]]
    print(s.dfs(adj))
