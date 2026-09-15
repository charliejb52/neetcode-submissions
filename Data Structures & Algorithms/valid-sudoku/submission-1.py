class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:

            seen = set()
            for num in row:
                if num != ".":
                    num = int(num)
                    if num < 0 or num > 9 or num in seen:
                        return False
                    seen.add(num)


        cols = list(zip(*board))

        for col in cols:

            seen = set()
            for num in col:
                if num != ".":
                    num = int(num)
                    if num < 0 or num > 9 or num in seen:
                        return False
                    seen.add(num)

        
        for r in range(3):
            for c in range(3):

                seen = set()
                
                for i in range(3):
                    for j in range(3):

                        num = board[r*3 + i][c*3 + j]

                        if num != ".":
                            num = int(num)
                            if num < 0 or num > 9 or num in seen:
                                return False
                            seen.add(num)

        return True

                

        