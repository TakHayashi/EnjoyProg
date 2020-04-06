# sud_ClsS42B.py
# version 4 update from version 2
from sud_ClsS2 import Sudoku

import itertools
from swatch import startwatch


class Sudoku(Sudoku):
    """depth first solver using recursion.
    place number with constraint propagation by candidate list.
    """

    def __init__(self, v):
        super().__init__(v)
        self.cd = [[list(range(1, 10)) for i in range(9)] for j in range(9)]
        # synchronize board list and candidate list
        for r in range(9):
            for c in range(9):
                n = self.vs[r][c]
                if n > 0:
                    self.__place(self.vs, self.cd, r, c, n)

    def solve(self, n, onlyone=True):
        self.lap = startwatch()
        self.__solver(self.vs, self.cd, n, onlyone)
        self.t = self.lap()[0]  # stamp time before check / print
        self.printbrd()
        chk = 'OK' if self.checkres() else 'NG'
        return (chk, self.vs, self.ncall, self.nret, self.nsol, self.t)

    def __solver(self, vs, cd, n, onlyone=True):  # depth first recursive solver
        def cpy(fm, to):
            for i, j in itertools.product(range(9), range(9)):
                to[i][j][:] = fm[i][j]
        self.ncall += 1
        ncd = [[[] for i in range(9)] for j in range(9)]
        while n < 81:
            r, c = n // 9, n % 9
            if cd[r][c] != []:
                break
            n += 1
        if n >= 81:  # found?
            self.nsol += 1
            if onlyone == False:
                chk = 'OK' if self.checkres() else 'NG'
                self.printbrd()  # print solution
                self.printresult(chk+' found:')
            return onlyone
        cda = cd[r][c]
        cpy(cd, ncd)
        # for m in cd[r][c]:
        for m in self.__sortorder(cd, r, c):
            if self.__place(vs, cd, r, c, m) and self.__solver(vs, cd, n+1, onlyone):
                self.nret += 1
                return True  # place and propagation
            cpy(ncd, cd)  # recover cand list if place fail
        else:
            vs[r][c] = 0
        # return False #can be omitted

    def __sortorder(self, cd, r, c):
        t = cd[r][c]  # get  candidate list
        cnt = [[e, 0]for e in t]
        for i in range(len(t)):
            for j in range(9):
                if len(cd[r][j]) > 0 and j != c:  # count row direction
                    if cnt[i][0] in cd[r][j]:
                        cnt[i][1] += 1
                if len(cd[j][c]) > 0 and j != r:  # count column direction
                    if cnt[i][0] in cd[j][c]:
                        cnt[i][1] += 1
            r0, c0 = r // 3 * 3, c // 3 * 3
            for j, k in itertools.product(range(r0, r0+3), range(c0, c0+3)):
                if len(cd[j][k]) > 0 and not(j == r or k == c):
                    if cnt[i][0] in cd[j][k]:
                        cnt[i][1] += 1  # count block direction
        # sort ascending order for less frequent number in sections first.
        # ascending order of count. will be mimimum recursion
        cnt.sort(key=lambda x: x[1])
        # cnt.sort(key=lambda x: x[1],reverse=True) #descending order of count. will be maximum recursion
        return [n for n, _ in cnt]

    def __place(self, v, cd, r, c, n):  # place at (r,c) and propagate constraint
        v[r][c] = n
        cd[r][c] = []
        # constraint propagation
        return self.__propagate(cd, r, c, n)

    def __propagate(self, cd, r, c, n):
        rm = [n]
        if not self.propr(cd, r, rm, [c]):
            return False
        if not self.propc(cd, c, rm, [r]):
            return False
        if not self.propb(cd, r, c, rm, [r, c]):
            return False
        return True
    # rml:remove number list, exl:exception index(0-8) list

    def proprc(self, cd, isrow, r, c, rm, exl):
        if isrow:
            self.propr(cd, r, rm, exl)
        else:
            self.propc(cd, c, rm, exl)

    def propr(self, cd, r, rm, exl):
        rng = set(range(9)) - set(exl)
        for i in rng:
            for j in range(len(rm)):
                n = rm[j]
                if n in cd[r][i]:
                    if len(cd[r][i]) > 1:
                        cd[r][i].remove(n)
                    else:
                        return False
        return True

    def propc(self, cd, c, rm, exl):  # propagate column
        rng = set(range(9)) - set(exl)
        for i in rng:
            for j in range(len(rm)):
                n = rm[j]
                if n in cd[i][c]:
                    if len(cd[i][c]) > 1:
                        cd[i][c].remove(n)
                    else:
                        return False
        return True

    def propb(self, cd, r, c, rm, exl):  # propagate block
        r3, c3 = r // 3 * 3, c // 3 * 3
        for i, j in itertools.product(range(r3, r3+3), range(c3, c3+3)):
            if [i, j] not in exl:
                for k in range(len(rm)):
                    n = rm[k]
                    if n in cd[i][j]:
                        if len(cd[i][j]) > 1:
                            cd[i][j].remove(n)
                        else:
                            return False
        return True


if __name__ == '__main__':

    Sudoku.PrintOnOff(True)
    v = [[5, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 4, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 8, 0, 2],
         [0, 4, 0, 0, 0, 0, 0, 3, 0], [0, 0, 3, 0, 1,
                                       0, 9, 0, 0], [2, 6, 0, 0, 7, 8, 1, 0, 0],
         [0, 9, 0, 0, 0, 0, 0, 2, 0], [0, 0, 8, 0, 0, 0, 7, 6, 0], [0, 0, 7, 5, 0, 6, 0, 0, 0]]
    v = '500000000000140000010000802040000030003010900260078100090000020008000760007506000'
    solver = Sudoku(v)
    chk, vs, ncall, nret, nsol, t = solver.solve(0, True)
    print('solve end.'+' '+'{:5.3f}'.format(t)+'s  rc='+'{:,d}'.format(ncall))
