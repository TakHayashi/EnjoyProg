# nsolve_ClsS2.py
# base class
import itertools
from swatch import startwatch

class Nsolve:
    """
    depth first num-place solver using recursion.
    used as base class of delived (version-up) class.
    same class name expected in version-up.
    """
    Print = False  # class variable to suppress  print board

    def __init__(self, v):
        self.ncall = 0
        self.nret = 0
        self.nsol = 0
        self.lap = None
        self.t = 0
        # vr as problem reference ,no change in __solver()
        if type(v) is str:
            if len(v) < 81:
                print('Fail init. string len must be >=81.')
                return None
            chars = v[:81]  # first 81 chars
            if not all(c in '1234567890.' for c in chars):
                print('Fail init. char must be 0123456789.')
                return None
            self.vr = [[int(v[r*9+c]) for c in range(9)] for r in range(9)]
        else:
            self.vr = [[v[j][i] for i in range(9)] for j in range(9)]
        # result board
        self.vs = [[self.vr[j][i] for i in range(9)] for j in range(9)]

    def solve(self, n, onlyone=True):
        self.lap = startwatch()
        self.__solver(self.vs, n, onlyone)
        self.t = self.lap()[0]  # stamp time before check and print
        self.printbrd()
        chk = 'OK' if self.checkres() else 'NG'
        return (chk, self.vs, self.ncall, self.nret, self.nsol, self.t)

    def __solver(self, vs, n, onlyone=True):  # depth first recursive solver
        # internal functions of __solver
        def check(v, r, c, i):  # chack related cells( row, column, block)
            return row(v, r, i) and column(v, c, i) and block(v, r, c, i)

        def row(v, r, i):
            return i not in v[r]  # True if not used in row

        def column(v, c, i):
            return all(True if i != v[r][c] else False for r in range(9))

        def block(v, r, c, i):  # 17Sec faster than above
            c0, r0 = (c // 3) * 3, (r // 3) * 3
            return all(True if i not in v[r][c0:c0 + 3]
                       else False for r in range(r0, r0 + 3))
        # __solver from here
        self.ncall += 1
        while n < 81:
            r, c = n // 9, n % 9
            if vs[r][c] == 0:
                break
            n += 1
        if n >= 81:  # solution found?
            self.nsol += 1
            if onlyone == False:
                chk = 'OK' if self.checkres() else 'NG'
                self.printbrd()  # print solution
                self.printresult(chk+' found:')
            return onlyone
        for i in range(1, 10):  # try 1 - 9
            if check(self.vs, r, c, i):  # possible to place?
                vs[r][c] = i  # place it
                if self.__solver(vs, n + 1, onlyone):
                    self.nret += 1
                    return True
        vs[r][c] = 0  # nothing to place ,cancel current placement

    @classmethod
    def PrintOnOff(cls, On=True):
        Nsolve.Print = On

    def printbrd(self):
        if not Nsolve.Print:
            return
        print()
        for i in range(9):
            print(self.vs[i])

    def printresult(self, titl):
        # print(titl,'sols=',self.nsol,f'time={self.t:5.3f}s '+
        # f'ncall={self.ncall:,d} nret={self.nret:,d}')
        print(titl, 'sols=', self.nsol,
              'time={:5.3f}s ncall={:,d} nret={:,d}'.
              format(self.t, self.ncall, self.nret))

    def getcount(self):
        return (self.ncall, self.nsol)

    def countzero(self, v):
        return sum(v[i].count(0) for i in range(9))

    # check correctness of result
    def checkres(self):
        for i in range(9):
            for j in range(9):
                if self.vr[i][j] > 0:
                    if self.vr[i][j] != self.vs[i][j]:
                        return False
        else:
            s19 = set(range(1, 10))
            vt = list(map(list, zip(*self.vs)))  # invert row/column
            for i in range(9):
                if s19-set(self.vs[i]) != set():
                    return False
                if s19-set(vt[i]) != set():
                    return False
            for i in range(0, 9, 3):  # block
                for j in range(0, 9, 3):
                    s = set(self.vs[i][j:j+3])
                    s |= set(self.vs[i+1][j: j+3])
                    s |= set(self.vs[i+2][j: j+3])
                    if s19-s != set():
                        return False
                return True


if __name__ == '__main__':
    from nsolve_common import v
    #from nsolve_allzero import v
    Nsolve.PrintOnOff(True)
    solver = Nsolve(v)
    solver.printbrd()
    solver.solve(0)
    solver.printresult('')
    solver.printbrd()
