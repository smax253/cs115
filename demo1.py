from cs115 import *

def add(x,y):
    return x+y

def f(L):
    '''assume L is a list of numbers'''
    return reduce(add,L)

def mult(x,y): return x*y

def fact(N):
    return reduce(mult,range(1,N+1))

def span(L):
    '''return difference between max and min of list L'''
    return reduce(max,L)-reduce(min,L);

def square(N):
    '''returns square of N'''
    return N*N;

def gauss(N):
    '''returns sum of numbers from 1 to N'''
    return reduce(add,range(1,N+1))

def sumOfSquares(N):
    '''returns sum of squares from 1 to N'''
    return reduce(add,map(square,range(1,N+1)))

def reverse2(L):
    def rev(acc,L):
        if L==[]: return acc
        else: return rev([L[0]]+acc, L[1:])
    return rev([],L)

def factorial(N):
    ans = 1
    for x in range(1,N+1):
        ans*=x
    return ans

def mapSqr(L):
    ans = []
    for x in range(len(L)):
        ans += [L[x]**2]
    return ans



def fib(N):
    first = 0
    second = 1
    if N==0: return first
    elif N==1: return second
    while N>1:
        third = second+first
        first = second
        second = third
        N-=1
    return second
        


