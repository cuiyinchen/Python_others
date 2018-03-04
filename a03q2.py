##==============================================================
## Cuiyin Chen (20708813)
## CS 116 Winter 2018
## Assignment 03, Problem 2
##==============================================================

import check
import math

# Q2
## bin2nat(bistr) returns a natural number representing the decimal value
##   of the binary system's number bistr
## bin2nat: Str -> Nat
## Requires:
##   bistr is nonempty
##   bistr represents a positive binary number
## Examples:
##   bin2nat('1') -> 1
##   bin2nat('1101') -> 13
##   bin2nat('0') -> 0

def bin2nat(bistr):
    if bistr == '0':
        return 0
    if bistr == '1':
        return 1
    elif bistr[0] == '1':
        return 1 * (2 ** (len(bistr) - 1)) + bin2nat(bistr[1:])
    elif bistr[0] == '0':
        return 0 * (2 ** (len(bistr) - 1)) + bin2nat(bistr[1:])

## Tests:
check.expect('t1', bin2nat('1'), 1)
check.expect('t2', bin2nat('0'), 0)
check.expect('t3', bin2nat('1111'), 15)
check.expect('t4', bin2nat('00000'), 0)
check.expect('t5', bin2nat('101001'), 41)
check.expect('t6', bin2nat('001010'), 10)
check.expect('t7', bin2nat('010101'), 21)
check.expect('t8', bin2nat('101010'), 42)