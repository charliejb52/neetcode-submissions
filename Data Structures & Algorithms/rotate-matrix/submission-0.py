class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        for i, column in enumerate(zip(*matrix)):
            matrix[i] = list(column)[::-1]
        