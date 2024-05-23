import random
lst = []
pdict = {
    0: ['             ',
        '             ',
        '             ',
        '             ',
        '             ',
        '             ',
        '             '],
    1: ['* * * o      ',
        '* * * o      ',
        '* * * o      ',
        '* * * o      ',
        '* * * o      ',
        '* * * o      ',
        '* * * o      '],
    2: ['* * * o      ',
        '* * * o      ',
        '* * o        ',
        'o o          ',
        '             ',
        '             ',
        '             '],
    3: ['      o * * *',
        '      o * * *',
        '        o * *',
        '          o o',
        '             ',
        '             ',
        '             '],
    4: ['* * * * * * *',
        '* * * * * * *',
        '* * * * * * *',
        'o o o o o o o',
        '             ',
        '             ',
        '             '],
    5: ['             ',
        '             ',
        '             ',
        'o o          ',
        '* * o        ',
        '* * * o      ',
        '* * * o      '],
    6: ['             ',
        '             ',
        '             ',
        '          o o',
        '        o * *',
        '      o * * *',
        '      o * * *'],
    7: ['* * * o      ',
        '* * * o      ',
        '* * o        ',
        'o o       o o',
        '        o * *',
        '      o * * *',
        '      o * * *'],
    8: ['      o * * *',
        '      o * * *',
        '        o * *',
        'o o       o o',
        '* * o        ',
        '* * * o      ',
        '* * * o      '],
    9: ['* * * * * * *',
        '* * * * * * *',
        '* * * * * * *',
        '* * * * * * *',
        '* * * * * * *',
        '* * * * * * *',
        '* * * * * * *'],
    10: ['      o * * *',
         '      o * * *',
         '      o * * *',
         '      o * * *',
         '      o * * *',
         '      o * * *',
         '      o * * *'],
    11: ['      o * * *',
         '      o * * *',
         '    o * * * *',
         'o o * * * * *',
         '* * * * * * *',
         '* * * * * * *',
         '* * * * * * *'],
    12: ['* * * o      ',
         '* * * o      ',
         '* * * * o    ',
         '* * * * * o o',
         '* * * * * * *',
         '* * * * * * *',
         '* * * * * * *'],
    13: ['             ',
         '             ',
         '             ',
         'o o o o o o o',
         '* * * * * * *',
         '* * * * * * *',
         '* * * * * * *'],
    14: ['* * * * * * *',
         '* * * * * * *',
         '* * * * * * *',
         'o o * * * * *',
         '    o * * * *',
         '      o * * *',
         '      o * * *'],
    15: ['* * * * * * *',
         '* * * * * * *',
         '* * * * * * *',
         '* * * * * o o',
         '* * * * o    ',
         '* * * o      ',
         '* * * o      '],
    16: ['      o * * *',
         '      o * * *',
         '    o * * * *',
         'o o * * * o o',
         '* * * * o    ',
         '* * * o      ',
         '* * * o      '],
    17: ['* * * o      ',
         '* * * o      ',
         '* * * * o    ',
         'o o * * * o o',
         '    o * * * *',
         '      o * * *',
         '      o * * *']
}
cdict = {
    (0, 0, 0): [0, 2, 3, 4],
    (0, 0, 1): [6, 7, 10, 14, 17],
    (0, 1, 0): [1, 5, 8, 15, 16],
    (0, 1, 1): [9, 11, 12, 13],
    (1, 0, 0): [0, 1, 2, 5],
    (1, 0, 1): [6, 7, 12, 13, 17],
    (1, 1, 0): [3, 4, 8, 15, 16],
    (1, 1, 1): [9, 10, 11, 14],
    (2, 0, 0): [0, 3, 6, 10],
    (2, 0, 1): [5, 8, 11, 13, 16],
    (2, 1, 0): [2, 4, 7, 14, 17],
    (2, 1, 1): [1, 9, 12, 15],
    (3, 0, 0): [0, 5, 6, 13],
    (3, 0, 1): [3, 8, 10, 11, 16],
    (3, 1, 0): [1, 2, 7, 12, 17],
    (3, 1, 1): [4, 9, 14, 15]
}
epdict = {
    0: [(0, 0, 0),
        (1, 0, 0),
        (2, 0, 0),
        (3, 0, 0)],
    1: [(0, 1, 0),
        (1, 1, 1),
        (2, 0, 0),
        (3, 1, 0)],
    2: [(0, 1, 0),
        (1, 1, 0),
        (2, 0, 0),
        (3, 0, 0)],
    3: [(0, 0, 1),
        (1, 0, 0),
        (2, 1, 0),
        (3, 0, 0)],
    4: [(0, 1, 1),
        (1, 1, 0),
        (2, 1, 0),
        (3, 0, 0)],
    5: [(0, 0, 0),
        (1, 0, 1),
        (2, 0, 0),
        (3, 1, 0)],
    6: [(0, 0, 0),
        (1, 0, 0),
        (2, 0, 1),
        (3, 0, 1)],
    7: [(0, 1, 0),
        (1, 1, 0),
        (2, 0, 1),
        (3, 0, 1)],
    8: [(0, 0, 1),
        (1, 0, 1),
        (2, 1, 0),
        (3, 1, 0)],
    9: [(0, 1, 1),
        (1, 1, 1),
        (2, 1, 1),
        (3, 1, 1)],
    10: [(0, 0, 1),
         (1, 0, 0),
         (2, 1, 1),
         (3, 0, 1)],
    11: [(0, 0, 1),
         (1, 0, 1),
         (2, 1, 1),
         (3, 1, 1)],
    12: [(0, 1, 0),
         (1, 1, 1),
         (2, 0, 1),
         (3, 1, 1)],
    13: [(0, 0, 0),
         (1, 0, 1),
         (2, 0, 1),
         (3, 1, 1)],
    14: [(0, 1, 1),
         (1, 1, 0),
         (2, 1, 1),
         (3, 0, 1)],
    15: [(0, 1, 1),
         (1, 1, 1),
         (2, 1, 0),
         (3, 1, 0)],
    16: [(0, 0, 1),
         (1, 0, 1),
         (2, 1, 0),
         (3, 1, 0)],
    17: [(0, 1, 0),
         (1, 1, 0),
         (2, 0, 1),
         (3, 0, 1)]
}

class Cell:
    def __init__(self, addr,n=None):
        if n is not None:
            self.pattern = pdict[n]
            self.x, self.y = self.addr = addr
            self.encode = epdict[n]
        else:
            self.encode = [(0, -1, -1), (1, -1, -1), (2, -1, -1), (3, -1, -1)]
            self.possible = set(range(18))
            self.neighbours = [set(range(18)) for i in range(4)]
            self.pattern = ['-------------',
                            '|           |',
                            '|           |',
                            '|           |',
                            '|           |',
                            '|           |',
                            '-------------']

    def draw(self, i):
        print(self.pattern[i], end=" ")
    
    def setval(self, n):
        self.pattern = pdict[n]
        self.encode = epdict[n]
        self.possible = {n}
    
    def setside(self, side, val):
        self.encode[side] = (side, *val)
        self.possible = self.possible.intersection(set(cdict[(3-side, *val)]))
    
    def setneighbour(self, side, vals):
        self.neighbours[side] = set(vals)
        st = set([])
        for v in vals:
            s = epdict[v][3-side]
            st = st.union(set(cdict[s]))
        self.possible = self.possible.intersection(st)
        x = [2**i for i in self.possible]
        if len(x) > 1:
            y = sum(x)
            l = len(str(y))
            self.pattern = [' '*13, ' '*13, ' '*13, str(y) + ' '*(13-l), ' '*13, ' '*13, ' '*13]
        else:
            self.pattern = pdict[list(self.possible)[0]]
    
    def isstable(self):
        return len(self.possible) == 1

class Grid(Cell):
    def __init__(self, n, m):
        self.cells = [[Cell((i, j)) for j in range(m)] for i in range(n)]
        self.n = n
        self.m = m

    def gridstable(self):
        for i in self.cells:
            for j in i:
                if not j.isstable():
                    return False
        return True

    def collapse(self, addr=None):
        if addr:
            x, y = addr
            self.cells[x][y].setval(random.choice(list(self.cells[x][y].possible)))
        else:
            x = random.choice(range(self.n))
            y = random.choice(range(self.m))
            self.cells[x][y].setval(random.choice(list(self.cells[x][y].possible)))

    def printgrid(self):
        l = []
        for i in range(self.n):
            x = []
            for j in range(self.m):
                sum = 0
                for k in self.cells[i][j].possible:
                    sum += 2**k
                x.append(sum)
            l.append(x)
        for i in l:
            for j in i:
                print(j, end = "\t")
            print()
    
    def drawgrid(self):
        print('-'*14*self.m+'---')
        for i in range(self.n):
            for k in range(7):
                print("|", end=" ")
                for j in range(self.m):
                    self.cells[i][j].draw(k)
                print("|")
        print('-'*14*self.m+'---')

    def propagate(self, addr):
        x, y = addr
        if x > 0 and not self.cells[x-1][y].isstable():
            lst.append((x-1, y))
            self.cells[x-1][y].setneighbour(3, self.cells[x][y].possible)
        if x < self.n-1 and not self.cells[x+1][y].isstable():
            lst.append((x+1, y))
            self.cells[x+1][y].setneighbour(0, self.cells[x][y].possible)
        if y > 0 and not self.cells[x][y-1].isstable():
            lst.append((x, y-1))
            self.cells[x][y-1].setneighbour(2, self.cells[x][y].possible)
        if y < self.m-1 and not self.cells[x][y+1].isstable():
            lst.append((x, y+1))
            self.cells[x][y+1].setneighbour(1, self.cells[x][y].possible)
        while not self.gridstable():
            a = lst.pop()
            x, y = a
            self.cells[x][y].setval(random.choice(list(self.cells[x][y].possible)))
            if x > 0 and not self.cells[x-1][y].isstable():
                lst.append((x-1, y))
                self.cells[x-1][y].setneighbour(3, self.cells[x][y].possible)
            if x < self.n-1 and not self.cells[x+1][y].isstable():
                lst.append((x+1, y))
                self.cells[x+1][y].setneighbour(0, self.cells[x][y].possible)
            if y > 0 and not self.cells[x][y-1].isstable():
                lst.append((x, y-1))
                self.cells[x][y-1].setneighbour(2, self.cells[x][y].possible)
            if y < self.m-1 and not self.cells[x][y+1].isstable():
                lst.append((x, y+1))
                self.cells[x][y+1].setneighbour(1, self.cells[x][y].possible)


g = Grid(6, 10)
addr = (random.choice(range(g.n)), random.choice(range(g.m)))
g.collapse(addr)
g.drawgrid()
g.propagate(addr)
g.drawgrid()