class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        trustGraph = [[] for i in range(n+1)]
        trustedGraph = [[] for i in range(n+1)]
        for a, b in trust:
            trustGraph[a].append(b)
            trustedGraph[b].append(a)

        for person in range(n+1):
            if len(trustGraph[person]) == 0 and len(trustedGraph[person]) == n-1:
                return person
        return -1