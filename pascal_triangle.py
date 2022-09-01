"""
pascal_triangle.py: Inspired from 'The Discovery That Transformed Pi' by Veritasium
Generated with Codex as part of the PyCodex project
"""
def pascal_triangle(rows):
    triangle = []
    for i in range(rows):
        triangle.append([])
        triangle[i].append(1)
        for j in range(1, i):
            triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])
        if(rows != 0):
            triangle[i].append(1)
    return triangle
    
def print_triangle(triangle):
    for i in range(len(triangle)):
        print("   "*(len(triangle)-i), end=" ", sep=" ")
        for j in range(0, i+1):
            print('{0:6}'.format(triangle[i][j]), end=" ", sep=" ")
        print()
        
rows = int(input("Enter the number of rows: "))
triangle = pascal_triangle(rows)
print_triangle(triangle)
