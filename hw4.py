"""
    Max Shi
    9/26/18
    I pledge my honor that I have abided by the Stevens Honor System
"""

def adjSum(L):
    if L[0] == 1: L=L+[0]
    if L[1] == 0: return [1]
    else: return [L[0]+L[1]]+adjSum(L[1:])
def pascal_row(N):
    if N == 0: return [1]
    else: return [1]+adjSum(pascal_row(N-1))
def pascal_triangle(N):
    if(N==0): return [[1]]
    else: return pascal_triangle(N-1)+[[1]+adjSum(pascal_row(N-1))]
