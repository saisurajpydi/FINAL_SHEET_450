"""
Given a string S. The task is to print all permutations of a given string.

Input:
2
ABC
ABSG

Output:
ABC ACB BAC BCA CAB CBA 
ABGS ABSG AGBS AGSB ASBG ASGB BAGS BASG BGAS BGSA BSAG BSGA GABS GASB GBAS GBSA GSAB GSBA SABG SAGB SBAG SBGA SGAB SGBA
"""
from itertools import permutations
    
def permu(s):
    per = permutations(s)
    for i in list(per):
        print(''.join(i), end = ' ')
    print()
t = int(input())
for i in range(t):
    st = input()
    stt = sorted(st)
    st = "".join(stt)
    permu(st)