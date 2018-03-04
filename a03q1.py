##==============================================================
## Cuiyin Chen (20708813)
## CS 116 Winter 2018
## Assignment 03, Problem 1
##==============================================================

import check
import math
# Q1

invalid_msg = "Invalid password"
end_msg = "Thank you!"
welcome_msg = "Enter a password:"

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digit = "1234567890"

## helper function to check upper-cased words
## check_upper(s) returns True if there is at least one upper-cased letter
##   in the string s; returns False otherwise
## check_upper: Str -> Bool
## Examples:
##   check_upper('') => False
##   check_upper('A') => True
##   check_upper('after') => False
##   check_upper('After') => True

def check_upper(s):
    if s == '':
        return False
    elif s[0] in upper:
        return True
    else:
        return check_upper(s[1:])

## Tests:
check.expect("t1", check_upper(''), False)
check.expect("t2", check_upper('A'), True)
check.expect('t3', check_upper('after'), False)
check.expect('t4', check_upper('Af ter'), True)
check.expect('t5', check_upper('CHEN'), True)


## helper function to check lower-cased words
## check_lower(s) returns True if there is at least one lower-cased letter
##   in the string s; returns False otherwise
## check_lower: Str -> Bool
## Examples:
##   check_lower('') => False
##   check_lower('A') => False
##   check_lower('a') => True
##   check_lower('AFTER') => False
##   check_lower('After') => True

def check_lower(s):
    if s == '':
        return False
    elif s[0] in lower:
        return True
    else:
        return check_lower(s[1:])    

## Tests:
check.expect('t6', check_lower(''), False)
check.expect('t7', check_lower('A'), False)
check.expect('t8', check_lower('a'), True)
check.expect('t9', check_lower('AFTER'), False)
check.expect('t10', check_lower('After'), True)
check.expect('t11', check_lower('ch en'), True)


## helper function to check if there are digits
## check_digit(s) returns True if there is at least one digit in the string
##   s; returns False otherwise
## check_digit: Str -> Bool
## check_digit('') -> False
## check_digit('aa3') -> True
## check_digit('4') -> True

def check_digit(s):
    if s == '':
        return False
    elif s[0] in digit:
        return True
    else:
        return check_digit(s[1:])    

## Tests:
check.expect('t12', check_digit(''), False)
check.expect('t13', check_digit('aa4'), True)
check.expect('t14', check_digit('55Aa'), True)
check.expect('t15', check_digit('2'), True)
check.expect('t16', check_digit('123456789'), True)
check.expect('t17', check_digit('CHECKif number'), False)


## main function
## pass_check() prints Thank you! if the person enter at least 1 lowercase 
##   leter, at least 1 uppercase letter, at least 1 number and no spaces; 
##   prints Invalid password otherwise
## Effects: prints either Invalid password to the users and let them to
##   enter again; or Thank you! if they enter the valid password
## pass_check: None -> Str
## Examples:
##   if the user inputs ['a', '3a', '3a A', '3aA'], pass_check() prints
##      Thanks you!
##   if the user inputs '22aaB!!DF44##$', pass_check() prints Thank you!

def pass_check():
    enter = input(welcome_msg)
    if not(' ' in enter) and check_upper(enter) and \
       check_lower(enter) and check_digit(enter):
        print(end_msg)
        return enter
    else:
        print(invalid_msg)
        return pass_check()


## Tests:
check.set_input(['a', '3a', '3a A', '3aA'])
check.set_screen("the user tried 3 times and succeeded in the last time")
check.expect('t18', pass_check(), '3aA')
check.set_input(['5344rffFEFA###22!!'])
check.set_screen("the user succeed in the first time")
check.expect('t19', pass_check(), '5344rffFEFA###22!!')
check.set_input(['aaAA', '2342A ERugfre 44 waterloo', '2342AERugfre44waterloo'])
check.set_screen("the user tried 2 times and succeed after removing the space")
check.expect('t20', pass_check(), '2342AERugfre44waterloo')
check.set_input(['chen', 'CHEN', 'Chen', 'Chen387'])
check.set_screen("the user succeeded in the last time")
check.expect('t21', pass_check(), 'Chen387')
check.set_input(['', ' ', 'C387Chen'])
check.set_screen("the user succeeded in the last time")
check.expect('t22', pass_check(), 'C387Chen')
check.set_input(['C333Chen Cuiyin', 'C333ChenCuiyin!!!'])
check.set_screen("the user succeeded in the second time")
check.expect('t23', pass_check(), 'C333ChenCuiyin!!!')