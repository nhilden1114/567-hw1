'''
Created on Aug 28, 2018

@author: Nicole Hilden
I pledge my honor that I have abided by the Stevens Honor System
'''

def classify_triangle(val_a, val_b, val_c):

    '''returns a string that specifies whether the triangle is not
    a triangle, scalene, isosceles, or equilateral and whether or
    not they are also right triangles as well. '''

    output = ''

    if (not isinstance(val_c, int) or not isinstance(val_b, int) or not isinstance(val_a, int)):
        return 'All values must be integers'

    if (val_a+val_b <= val_c) or (val_a+val_c <= val_b) or (val_c+val_b <= val_a):
        return 'Not a triangle'
    if val_a == val_b and val_b == val_c:
        output = 'equilateral'
    if (val_a == val_b and val_a != val_c) or (val_a == val_c and val_a != val_b):
        output = 'isosceles'
    if (val_b == val_c and val_b != val_a):
        output = 'isosceles'
    if val_a != val_b and val_b != val_c and val_c != val_a:
        output = 'scalene'
    if (val_a**2 + val_b**2) == val_c**2 or (val_c**2 + val_b**2) == val_a**2:
        return 'Your triangle is ' + output + ' and right'
    if (val_a**2 + val_c**2) == val_b**2:
        return 'Your triangle is ' + output + ' and right'
    return 'Your triangle is ' + output + ' and not right'
