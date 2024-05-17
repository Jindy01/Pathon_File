import numpy as np 
from collections import deque

# matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])

# targ_ell = 1 
# incl = np.where(matrix == targ_ell)


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]




gg

# matrix_5x5 = [
#     [1,  2,  3,  4,  5],
#     [6,  7,  8,  9,  10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25]
# ]

# empty_matrix = []

# def find_max_ell(matrixf) -> int:
#     if len(matrixf) == 0:
#         return "Matrix - empty"
    
#     max_ell = matrixf[0][0]
#     for row in matrixf:
#         for element in row:
#             if element > max_ell:
#                 max_ell = element
#     return max_ell

# print(find_max_ell(matrixf=empty_matrix))

# def diagonal_and_secondary_sum(matrix: list):
#     if len(matrix) == 0:
#         return "Matrix - empty"
    
#     matrix_main_diagonal = 0
#     matrix_secondary_diagonal = 0
#     step_row = 0
#     step_element = 0

#     for row in matrix:
#         matrix_main_diagonal += matrix[step_row][step_element]
#         matrix_secondary_diagonal += matrix[step_row][-step_element - 1]
#         step_row += 1 
#         step_element += 1

#     return matrix_main_diagonal, matrix_secondary_diagonal

# print(diagonal_and_secondary_sum(matrix=matrix_5x5))




# def find_exsit(matrix: list):
#     if len(matrix) == 0:
#         return "Matrix - empry"
    
    
#     return 


# Графы 

# def bfs(graph, start):
#     visited = set()
#     queue = deque([start])

#     while queue:
#         current = queue.popleft()
#         visited.add(current)

#         for neighbor in graph[current]:
#             if neighbor not in visited:
#                 queue.append(neighbor)
    
#     print(visited)


# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F', 'G'],
#     'D': ['B'],
#     'E': ['B'],
#     'F': ['C'],
#     'G': ['C']
# }

# bfs(graph, 'A')


# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     print(start)
#     for neighbor in graph[start]:
#         if neighbor not in visited:
#             dfs(graph, neighbor, visited)


# graph = {
#     1: [2, 3],
#     2: [1, 4, 5],
#     3: [1, 6, 7],
#     4: [2],
#     5: [2],
#     6: [3],
#     7: [3]
# }

# dfs(graph, 7)

# Доделать своим способом
# def generateMatrix(n: int):
#         matrix = [[0 for _ in range(n)] for _ in range(n)]

#         coordinate_x = 0
#         coordinate_y = 0

#         int_for_matrix = 1
#         for i, row in enumerate(matrix):
#             for j, element in enumerate(row):
                
#                 if element == 0:
#                     matrix[coordinate_x][coordinate_y] = int_for_matrix
#                     int_for_matrix += 1
#                 if len(matrix) > i:
#                        coordinate_x += 1
#                 elif len(matrix) == i:
#                      continue
        
#         print(len(matrix))
#         print(len(matrix[0]))
#         print(matrix)

# generateMatrix(3)

# Данный пример с GPT
# def spiral_matrix(n):
#     matrix = [[0] * n for _ in range(n)]
#     top, bottom, left, right = 0, n - 1, 0, n - 1
#     num = 1

#     while num <= n * n:
#         # Вправо
#         for i in range(left, right + 1):
#             matrix[top][i] = num
#             num += 1
#         top += 1

#         # Вниз
#         for i in range(top, bottom + 1):
#             matrix[i][right] = num
#             num += 1
#         right -= 1

#         # Влево
#         for i in range(right, left - 1, -1):
#             matrix[bottom][i] = num
#             num += 1
#         bottom -= 1

#         # Вверх
#         for i in range(bottom, top - 1, -1):
#             matrix[i][left] = num
#             num += 1
#         left += 1

#     return matrix

# # Пример использования
# n = 5
# result = spiral_matrix(n)
# for row in result:
#     print(row)


# def speral_matrix(n):
#     matrix = [[0] * n for _ in range(n)]
#     top, bottom, left, right = 0, n - 1, 0, n - 1
#     num = 1 

#     while num <= n * n:
#         for i in range(left, right + 1):


# def factorial(n):
#     result = 1
#     for i in range(1, n +1):
#         result *= i
#     return result
    
# print(factorial(5))

