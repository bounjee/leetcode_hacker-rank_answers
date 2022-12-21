"""Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is:  (c++ int) or  (C++ long long int).

As we know, the result of  grows really fast with increasing .

Let's do some calculations on very large integers."""

"""https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem?isFullScreen=true"""


a = int(input())
b = int(input())
c = int(input())
d = int(input())

cevap = a ** b
cevap2 = c ** d
son = cevap + cevap2

print(son)