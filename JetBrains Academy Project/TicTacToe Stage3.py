class TicTacToe:
    def __init__(self, position):
        self.position = position
        self.coordinate = [position[0:3], position[3:6], position[6:9]]
        self.coordinate_y = [position[0:9:3], position[1:9:3], position[2:9:3]]
        self.coordinate_xy = [position[0:9:4], position[2:8:2]]
        
    def __repr__(self):
        return f'''Current Board Coordinate:
x-coordinate: {self.coordinate}
y-coordinate: {self.coordinate_y}
xy-coordinate: {self.coordinate_xy}'''
    

    def __str__(self):
        return f'''---------
| {self.coordinate[0][0]} {self.coordinate[0][1]} {self.coordinate[0][2]} |
| {self.coordinate[1][0]} {self.coordinate[1][1]} {self.coordinate[1][2]} |
| {self.coordinate[2][0]} {self.coordinate[2][1]} {self.coordinate[2][2]} |
---------'''

    def check_condition(self):
        winner = set()

        for subcoor in [self.coordinate, self.coordinate_y, self.coordinate_xy]:
            for i in subcoor:
                if len(set(i)) == 1:
                    winner.add(i[0])
        winner.discard('_')
        
        if len(winner) == 2 or abs(self.position.count('O') - self.position.count('X')) >= 2:
            return "Impossible"
        elif len(winner) == 1:
            return 'O wins' if 'O' in winner else 'X wins'
        elif len(winner) == 0:
            if '_' in self.position:
                return "Game not finished"
            else:
                return "Draw"

my_tictactoe = TicTacToe(input('Enter cells: '))
DEBUG = False

if DEBUG == True:
    print(repr(my_tictactoe))

print(str(my_tictactoe))
print(my_tictactoe.check_condition())
