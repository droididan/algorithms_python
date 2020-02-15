import easy


def longestPelindromicSubstring(string):
    longest = ""
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i : j + 1]
            if len(substring) > len(longest) and easy.isPalindrome(substring):
                longest = substring
    return longest


# 1. define row and col
# 2. check if we run in the borders of the matrix
# 3. if the current number is bigger then the [target] then decrement column by 1
# 4. if the current nunber is smaller then the [target] then increament the row by 1
# 5. if none of these conditions are met so we are on the target number, return the coords

# O(n + m) time | O(1) space
def searchInSortedMatrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return [col, row]
    return [-1,-1]
