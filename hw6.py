'''
Created on 10/13/18
@author:   Max Shi
Pledge:    I pledge my honor that I have abided by the Stevens Honor System
CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5
# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1
# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def increment(s):
    '''Precondition: s is a string of n bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if(s==''): return ''
    elif(s[-1]=='1'): return increment(s[:-1])+'0'
    else: return s[:-1]+'1'

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '': return 0
    else: return int(s[-1])+2*binaryToNum(s[:-1])

def compress(s):
    '''Returns a compressed version of string s with run length encoding with max length defined in file'''
    def compress_helper(encode, state, num):
        if encode == '': return num
        elif(num == "1"*COMPRESSED_BLOCK_SIZE): return num+compress_helper(encode,not state, "0"*COMPRESSED_BLOCK_SIZE)
        elif int(encode[0]) == int(state):
            return compress_helper(encode[1:],state,increment(num))
        else:
            return num+ compress_helper(encode,not state, "0"*COMPRESSED_BLOCK_SIZE)
    return compress_helper(s,False,"0"*COMPRESSED_BLOCK_SIZE)

def uncompress(s):
    '''Returns the uncompressed string compressed with the compress() function'''
    def uncompress_helper(decode, state):
        if decode == "": return ""
        else: return binaryToNum(decode[:COMPRESSED_BLOCK_SIZE])*str(int(state))+uncompress_helper(decode[COMPRESSED_BLOCK_SIZE:],not state)
    return uncompress_helper(s,False)

def compression(s):
    '''Returns the ratio of the length between compress and the original string'''
    def comp_length(comp):
        if comp == "": return 0
        else: return 1+comp_length(comp[1:])
    return comp_length(compress(s))/comp_length(s)
'''
    If every bit is different compared to the last one, starting with a 1, the compressed string would have length of 5*64+5 or 5*65.
'''