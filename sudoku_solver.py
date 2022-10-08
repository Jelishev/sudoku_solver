def sudoku(puzzle):
    super = makeUnknowns(puzzle)
    """return the solved puzzle as a 2d array of 9 x 9"""
    for x in range(0,10):
        puzzle = iterate(puzzle, super)
    for x in puzzle:
        print(x)
    return puzzle

def iterate(puzzle, super):
    for sample in all:
        super = reduce(puzzle, super, sample)
        
    collapsables = []
    for id in super:
        #print(super.get(id))
        #all ids with only one possibilty get collapsed here
        if len(super.get(id)) == 1:
            puzzle = collapse(puzzle, id, super)
            collapsables.append(id)
    for id in collapsables:
        super.pop(id)
    return puzzle
            
def collapse(puzzle, num, super):
    id = convert(num)
    puzzle[id[0]][id[1]] = super.get(num)[0]
    return puzzle
    
    
#reduce possibility space of every item in super
def reduce(puzzle, super, sample):
    for x in sample:
        elim = []
        for y in x:
            id = convert(y)
            if puzzle[id[0]][id[1]] != 0:
                elim.append(puzzle[id[0]][id[1]])
        for space in x:
            if space in super:
                for element in elim:
                    try:
                        super[space].remove(element)
                    except: 
                        pass
    return super

def not_solved(puzzle):
    state = True
    for x in puzzle:
        if 0 in x:
            state = False
    return not state



#rando functions that def work are past here
def makeUnknowns(puzzle):
    super = {}
    for x in range (0,9):
        for y in range (0,9):
            if puzzle[x][y] == 0:
                super[x*10 + y] = [1,2,3,4,5,6,7,8,9]
    return super

def convert(num):
    col = int((num - num % 10) / 10)
    row = num % 10
    return [col, row]
    

rows = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [10, 11, 12, 13, 14, 15, 16, 17, 18], [20, 21, 22, 23, 24, 25, 26, 27, 28], [30, 31, 32, 33, 34, 35, 36, 37, 38], [40, 41, 42, 43, 44, 45, 46, 47, 48], [50, 51, 52, 53, 54, 55, 56, 57, 58], [60, 61, 62, 63, 64, 65, 66, 67, 68], [70, 71, 72, 73, 74, 75, 76, 77, 78], [80, 81, 82, 83, 84, 85, 86, 87, 88]]
cols = [[0, 10, 20, 30, 40, 50, 60, 70, 80], [1, 11, 21, 31, 41, 51, 61, 71, 81], [2, 12, 22, 32, 42, 52, 62, 72, 82], [3, 13, 23, 33, 43, 53, 63, 73, 83], [4, 14, 24, 34, 44, 54, 64, 74, 84], [5, 15, 25, 35, 45, 55, 65, 75, 85], [6, 16, 26, 36, 46, 56, 66, 76, 86], [7, 17, 27, 37, 47, 57, 67, 77, 87], [8, 18, 28, 38, 48, 58, 68, 78, 88]]
squares = [[0, 1, 2, 10, 11, 12, 20, 21, 22], [30, 31, 32, 40, 41, 42, 50, 51, 52], [60, 61, 62, 70, 71, 72, 80, 81, 82], [3, 4, 5, 13, 14, 15, 23, 24, 25], [33, 34, 35, 43, 44, 45, 53, 54, 55], [63, 64, 65, 73, 74, 75, 83, 84, 85], [6, 7, 8, 16, 17, 18, 26, 27, 28], [36, 37, 38, 46, 47, 48, 56, 57, 58], [66, 67, 68, 76, 77, 78, 86, 87, 88]]


all = [rows, cols, squares]
