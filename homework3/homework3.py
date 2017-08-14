## COMP1730/6730 S2 2017 - Homework 3

## The assignment can be done together in pairs, but not in a group of
## more than two students.
##
## If you work in a pair, both students must submit solution files, and
## both students must attend the following lab and answer the tutors
## questions. In this file, you must write a comment to say who you
## worked together with, like this:
##
## I worked together with NNNNNN (ANU id: NNNNNN).
##
## Both of you must be able to explain every part of your submitted
## solution. The tutor will choose who to address each question to, and
## only the student addressed may answer. It is not acceptable to divide
## the assignment up so that one student does half and the other student
## the other half.

## Modify the following function definition so that it computes and
## returns the correct answer to the homework problem. (The statement
## "return 1" is just a placeholder: you should of course modify it.)
def total_days(start_year, end_year):
    sum_day = 0

    for year in range(start_year, end_year ):
        isLeapYear = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        if isLeapYear:
            sum_day += 366
        else:
            sum_day += 365

    return sum_day

## REMEMBER THAT THIS FILE (WHEN YOU SUBMIT IT) MUST NOT CONTAIN ANYTHING
## OTHER THAN YOUR FUNCTION DEFINITION AND COMMENTS. You can (and should)
## use docstrings to document your functions, but a docstring should only
## be used inside a function definition, an then only at the very beginning
## of the function suite. Everywhere else you should use comments.
