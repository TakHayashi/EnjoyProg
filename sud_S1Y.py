#sud_S1Y
import sys
from os.path import basename

from swatch import startwatch
from sudq_common import v

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
     global rc
     rc+=1
     while n<81:
        r,c=n // 9,n % 9
        if v[r][c] == 0:break
        n+=1
     if n >=81: # finished?
        yield 
        return #return for recursion
     for i in range(1,10):  #try 1 - 9
        if check(v,r,c,i):  
           v[r][c]=i

           yield from solve(v,n + 1)
     v[r][c]=0

if __name__=='__main__' :
 
 pth=sys.argv[0]
 pyname="Script="+pth
 fn=basename(pth)
 print(fn)
 rc=0 
 lap=startwatch() 

 for sol,dmy in enumerate (solve(v,0)):
      print('solved.'+str(sol+1)+' ',lap('5.3f')[0]+'s','RC=',format(rc,',d'))
      for i in range(9):print(v[i])
 print(lap('5.3f')[0])
