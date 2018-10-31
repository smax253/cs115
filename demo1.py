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

def primeWack(N):
    return list(filter(lambda x:(N%x==0 and sum(map(lambda w: x%w==0, range(2,x)))),range(2,N)))



