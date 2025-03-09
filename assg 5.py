#33. Find All Permutations of a String
def permute(string, answer):
    if len(string) == 0:
        print(answer)
        return
    
    for i in range(len(string)):
        ch = new_func(string, i)
        left_substring = string[:i]
        right_substring = string[i+1:]
        rest = left_substring + right_substring
        permute(rest, answer+ch)

def new_func(string, i):
    ch = string[i]
    return ch

string = "abc"
print("All permutations of the string are:")
permute(string, "")

#34. N-th Fibonacci Number (Dynamic Programming)
def fibonacci(n):
     if n == 0:
        return 0
     if n == 1:
        return 1
    
     dp = [0] * (n+1)
     dp[0], dp[1] = 0, 1
    
     for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
     return dp[n]

n = 10
print("The {}-th Fibonacci number is:".format(n))
print(fibonacci(n))

#35. Find Duplicates in a List
from collections import Counter

def find_duplicates(arr):
    freq = Counter(arr)
    duplicates = [item for item, count in freq.items() if count > 1]
    return duplicates

arr = [1, 2, 3, 4, 5, 2, 3, 6]
print("Duplicates in the list are:")
print(find_duplicates(arr))

#36. Longest Increasing Subsequence (LIS)
def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
             dp[i] = max(dp[i], dp[j] + 1)
             return max(dp)

arr = [10, 9, 2, 5, 3, 7, 101, 18]
print("Length of LIS is:", longest_increasing_subsequence(arr))

#37. Find K Largest Elements
def find_k_largest(arr, k):
    arr.sort(reverse=True)
    return arr[:k]

arr = [3, 2, 1, 5, 6, 4]
k = 2
print("The {} largest elements are:".format(k))
print(find_k_largest(arr, k))

#38. Rotate Matrix
def rotate_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
        return matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotated_matrix = rotate_matrix(matrix)
for row in rotated_matrix:
    print(row)

#39. Sudoku Validator
def is_valid_sudoku(board):

    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == ".":
                continue
            
            # Check Row
            if num in rows[i]:
                return False
            rows[i].add(num)
            
            # Check Column
            if num in cols[j]:
                return False
            cols[j].add(num)
            
            # Check Box (3x3 sub-boxes)
            box_index = (i // 3) * 3 + (j // 3)
            if num in boxes[box_index]:
                return False
            boxes[box_index].add(num)
    return True
sudoku_board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(is_valid_sudoku(sudoku_board))

