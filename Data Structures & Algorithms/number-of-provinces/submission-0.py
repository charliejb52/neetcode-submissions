class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        seen = set()
        ret = 0

        def explore(row_index, seen) -> set:
            if row_index not in seen:
                seen.add(row_index)
                row = isConnected[row_index]

                for j in range(len(row)):
                    if j!= row_index and row[j] == 1:
                        seen = explore(j, seen)
            
            return seen
            

        # fully explore and chart all cities connected to index 0
        for i in range(len(isConnected)):
            
            if i not in seen:
                seen = explore(i, seen)
                ret += 1

        return ret

        