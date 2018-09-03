'''
Created on Aug 28, 2018

@author: Nicole Hilden
I pledge my honor that I have abided by the Stevens Honor System
'''

def classify_triangle(a,b,c):

    '''returns a string that specifies whether the triangle is not
    a triangle, scalene, isosceles, or equilateral and whether or 
    not they are also right triangles as well. '''
    
    output = ''
    
    if (type(a)!= int or type(b)!= int or type(c)!= int): 
        return 'All values must be integers'
        
    if (a+b <= c) or (a+c <= b) or (c+b <= b):
        return 'Not a triangle'
    if a==b and b==c:
        output = 'equilateral'
    if (a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a):
        output = 'isosceles'
    if a!=b and b!=c and c!=a:
        output = 'scalene'
    if ((a**2 + b**2) == c**2) or ((c**2 + b**2) == a**2) or ((a**2 + c**2) == b**2):
        return 'Your triangle is ' + output + ' and right'
    return 'Your triangle is ' + output + ' and not right' 
    
if __name__ == '__main__':
    print(classify_triangle(5,4,5))