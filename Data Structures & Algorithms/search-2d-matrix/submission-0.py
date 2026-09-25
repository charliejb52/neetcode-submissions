class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def bs(row, target):

            left = 0
            right = len(row) - 1
            mid = left + ((right-left) // 2)

            while (left <= right):

                # if number is found return true
                if row[left] == target or row[right] == target or row[mid] == target:
                    return True
                
                elif row[mid] > target:
                    right = mid-1
                    mid = left + ((right-left) // 2)

                elif row[mid] < target:
                    left = mid+1
                    mid = left + ((right-left) // 2)

            #if we get through the full list without finding target return False
            return False

            




        for row in matrix:

            if target >= row[0] and target <= row[-1]:
                return bs(row, target)

        return False

        