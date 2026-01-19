def right_triangle(rows):
    for i in  range(1, rows+1):
        line = ''
        for j in range (i):
            line += str("*")
        print(line)

 

def right_triangles(rows):
    print("\n".join("*" * i for i in range(1, rows+1)))
 #for line in ["*" * i for i in range(1, rows+1)]:
    #print(line)


def square(row):
    for i in range(row):
     line = "*" * row  
     print(line)

   

def inverted_triangle(row):
    for line in ['*'* i for i in range(row+1,0,-1) ]:
        print(line)

 

def pyramid(height):
    for row_number in range(1, height+1):
        spaces = ' ' * (height - row_number)
        stars = '*' * (2 * row_number -1)
        print(spaces+stars)

       

def diamond(height):
    if height%2 == 0:
        print ('invalid entry')
    else:    
        for row_number in range(1,(height//2)+2):
            #if row_number <= (height//2) + 1:
            space= ' ' *(((height//2)+1) -row_number)
            star='*' *(2*row_number -1)
            print(space+star)
        for row_number in range ((height//2),0,-1):
            spaces= ' ' * ((height//2+1)- row_number)
            stars ='*' * (2*row_number-1)
            print(spaces+stars)
                
   
diamond(5)                 
#
       