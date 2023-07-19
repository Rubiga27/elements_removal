def minimum_cost_to_remove_elements(A):
    A.sort()
    cost = 0
    cumu= 0

    for i in range(len(A)):
        cumu += A[i]
        cost += cumu

    return cost
A = list(map(int,input().split()))
print(minimum_cost_to_remove_elements(A))

"""
Input 1:
A = [2, 1]
Input 2:
A = [5]


Output 1:
4
Output 2:
5
"""

