import sys
from os.path import basename
from swatch import startwatch

def solve(v,n):#depth first recursive solver
    """
    first sodoku solver.
    algorithm :depth-first recursion.
    gives all solutions.
    fill the cell sequentially from top-left.
    for each cell, try not violated number from 1 to 9
    backtrack if no number without violation.
    """
    global rc
    rc+=1
    while True:
       if n >=81: # finished?
          t=lap('5.3f')[0]
          for i in range(9):print(v[i])  #print solution
          print('found: '+t+'s',' rc=',format(rc,',d'))
          return #finished
       r,c=n // 9,n % 9 #convert to 2 dimentional index
       if v[r][c] == 0: #empty cell?
          for i in range(1,10):  #try 1 - 9
             if check(v,r,c,i):   #possible to place?
                v[r][c] = i     #place it
                solve(v,n + 1) #call myself to go next cell          
          v[r][c] = 0  #nothing to place here,cancel current placement
          return     #return to previous cell. (backtrack)
       else :
          n+=1 #skip pre-placed cell
def check(v, r, c, i):#chack related cells( row, column, block)
    def row(v, r, i):
         return i not in v[r] #True if not used in row
    def column(v, c, i):
         return all(True if i != v[r][c] else False for r in range(9))
    def block(v, r, c, i): #17Sec faster than above
         c0 ,r0= (c // 3) * 3 , (r // 3) * 3
         return all(True if i not in v[r][c0:c0+ 3] else False for r in range(r0, r0 + 3)  )
    return row(v, r, i) and column(v, c, i) and block(v, r,c, i) 


if __name__=='__main__' :
 v=[ [5,0,0,0,0,0,0,0,0],[0,0,0,1,4,0,0,0,0],[0,1,0,0,0,0,8,0,2],
 [0,4,0,0,0,0,0,3,0],[0,0,3,0,1,0,9,0,0],[2,6,0,0,7,8,1,0,0],
 [0,9,0,0,0,0,0,2,0],[0,0,8,0,0,0,7,6,0],[0,0,7,5,0,6,0,0,0]]
## v=[[0, 2, 0, 0, 0, 6, 0, 0, 9], [4, 0, 6, 7, 0, 0, 1, 2, 0], [0, 0, 0, 1, 0, 3, 0, 5, 0],
##    [0, 1, 0, 0, 0, 5, 0, 7, 0], [5, 0, 7, 0, 9, 0, 2, 0, 0], [3, 4, 0, 0, 0, 0, 0, 1, 0],
##    [0, 3, 0, 0, 6, 0, 0, 0, 1], [6, 0, 0, 2, 0, 0, 3, 0, 0], [0, 7, 0, 0, 3, 0, 0, 6, 0]]
## v=[[0, 2, 0, 0, 0, 6, 0, 0, 0], [4, 0, 6, 7, 0, 0, 1, 2, 0], [0, 0, 0, 1, 0, 3, 0, 5, 0],
##    [0, 1, 0, 0, 0, 5, 0, 7, 0], [5, 0, 7, 0, 9, 0, 2, 0, 0], [3, 4, 0, 0, 0, 0, 0, 1, 0],
##    [0, 3, 0, 0, 6, 0, 0, 0, 1], [6, 0, 0, 2, 0, 0, 3, 0, 0], [0, 7, 0, 0, 3, 0, 0, 6, 0]]
 pth=sys.argv[0]
 pyname="Script="+pth
 fn=basename(pth)
 print(fn)
 rc=0
 lap=startwatch()
 solve(v,0)
 t=lap('5.3f')[0]
 for i in range(9):print(v[i])
 print('solve end. '+t+'s ','RC=',format(rc,',d'))
 
##first solution 2.048s  to return 3.960s

