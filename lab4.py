"""
    Max Shi
    9/26/18
    I pledge my honor that I have abided by the Stevens Honor System
"""

def knapsack(cap, items):
<<<<<<< HEAD
    '''Returns the maximum value and the list of items that can be created out of the subset of the items given with the given capacity'''
=======
    '''Returns a tuple of the maximum value of items and the items that can be taken with the given capacity from the given list of items'''
>>>>>>> 86e6f2c6e3d0a3dec7ea1095dd8cead396724a74
    if items == []: return [0,[]]
    elif items[0][0]>cap: return knapsack(cap, items[1:])
    else:
        use = knapsack(cap-items[0][0],items[1:])
        useList = [items[0][1]+use[0],[items[0]]+use[1]]
        lose = knapsack(cap,items[1:])
        return useList if useList[0]>lose[0] else lose
