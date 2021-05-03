#nsolve_S1R
import sys
from os.path import basename
from swatch import startwatch

def solve(v,n):#depth first recursive solver
     #internal function for solve
     def check(v, r, c, i):#chack related cells( row, column, block)
         return row(v, r, i) and column(v, c, i) and block(v, r,c, i)
     def row(v, r, i):
         return i not in v[r] #True if not used in row
     def column(v, c, i):
         return all(True if i != v[r][c] else False for r in range(9))
     def block(v, r, c, i): #17Sec faster than above
         c0 ,r0= (c // 3) * 3 , (r // 3) * 3
         return all(True if i not in v[r][c0:c0+ 3]
                  else False for r in range(r0, r0 + 3))

     #code of solve from here
     global rc
     rc+=1
     while n<81:
        r,c=n // 9,n % 9
        if v[r][c] == 0:break
        n+=1
     if n >=81: # finished?
        t=lap('5.3f')[0]  
        for i in range(9):print(v[i])  #print solution
        print('found:',t+'s','call count=',format(rc,',d'))
        return v#finished
     
     for i in range(1,10):  #try 1 - 9
        if check(v,r,c,i):
          solve(__newv(v,r,c,i),n + 1)
     return v
#works only list of int-list such as [[1,2,3,  ], .. ,[2,3,4,  ]]
def __newv(v,r,c,k):
   cpy=[ v[i][:]  for i in range(9)]
   cpy[r][c]=k
   return cpy


if __name__=='__main__' :

 #single solution
 v=[[5,0,0,0,0,0,0,0,0],[0,0,0,1,4,0,0,0,0],[0,1,0,0,0,0,8,0,2],
    [0,4,0,0,0,0,0,3,0],[0,0,3,0,1,0,9,0,0],[2,6,0,0,7,8,1,0,0],
    [0,9,0,0,0,0,0,2,0],[0,0,8,0,0,0,7,6,0],[0,0,7,5,0,6,0,0,0]]

 pth=sys.argv[0]
 pyname="Script="+pth
 fn=basename(pth)
 print(fn)
 rc=0
 lap=startwatch()
 vl=solve(v,0)
 for i in range(9):print(vl[i])
 print('solve end.',lap('5.3f')[0]+'s','call count=',format(rc,',d'))


