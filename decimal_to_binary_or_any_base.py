##==============================================================
## Cuiyin Chen (20708813)
## CS 116 Winter 2018
##==============================================================

import check
import math

# helper function for (a) and (b)

## quotient_lst(n,x) returns a list of number that are the quotient of n
##   when n is divided by some number x
## quotient_lst: Nat Nat -> (listof Nat)
## Examples:
##   quotient_lst(5,2) => [5,2,1]
##   quotient_lst(0,2) => [0]

def quotient_lst(n,x):
    lst = []
    if n == 0:
        lst.append(0)
    while n > 0:
        lst.append(n)
        n = n//x
    return lst     


# Part a
## nat2bin(n) returns a list of number 0 or 1 by converting the binary number 
##   n into the binary system's number
## nat2bin: Nat -> (listof (anyof 0 1))
## Requires: the function do not return []
## Examples:
##   nat2bin(0) -> [0]
##   nat2bin(15) -> [1,1,1,1]

def nat2bin(n):
    lst = []
    for num in quotient_lst(n,2):
        num = num % 2
        lst.insert(0,num)
    return lst

## Tests:
check.expect('a1', nat2bin(0), [0])
check.expect('a2', nat2bin(1), [1])
check.expect('a3', nat2bin(15), [1,1,1,1])
check.expect('a4', nat2bin(33), [1,0,0,0,0,1])
check.expect('a5', nat2bin(20), [1,0,1,0,0])
check.expect('a6', nat2bin(16), [1,0,0,0,0])
check.expect('a7', nat2bin(2), [1,0])


# Part b
## nat2base(n,base) returns a new list of number with the system of 
##   number base to represent the binary number n
## nat2base: Nat Nat -> (listof Nat)
## Requires:
##   base >= 2
## Examples:
##   nat2base(0,2) => [0]
##   nat2base(36,36) => [1,0]

def nat2base(n, base):
    lst = []
    for num in quotient_lst(n,base):
        num = num % base
        lst.insert(0,num)
    return lst    

## Tests:
check.expect('b1', nat2base(0,2), [0])
check.expect('b2', nat2base(0,30), [0])
check.expect('b3', nat2base(13,5), [2,3])
check.expect('b4', nat2base(15,18), [15])
check.expect('b5', nat2base(4,5), [4])
check.expect('b6', nat2base(121,10), [1,2,1])
check.expect('b7', nat2base(198,240), [198])
check.expect('b8', nat2base(361,3), [1,1,1,1,0,1])
check.expect('b9', nat2base(9,245), [9])
