class TicTacToe:
    position = '_________'
    
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
    
    def update_coor(self):
        self.coordinate = [self.position[0:3], self.position[3:6], self.position[6:9]]
        self.coordinate_y = [self.position[0:9:3], self.position[1:9:3], self.position[2:9:3]]
        self.coordinate_xy = [self.position[0:9:4], self.position[2:8:2]]
        

    def fill_coor(self, player):
        while True:
            fill_tmp = input('Enter the coordinates: ').split()
            try:
                x_y = [int(x) for x in fill_tmp]
            except:
                print('You should enter numbers!')
                continue

            x_y = [int(x) for x in fill_tmp]
            x = x_y[0]
            y = x_y[1]
            
            if not 1 <= x <= 3 or not 1 <= y <= 3:
                print('Coordinates should be from 1 to 3!')
            else:
                break
            
        x = 3 - x_y[1]
        y = x_y[0] - 1
        
        choosen_box = self.coordinate[x][y]
        if choosen_box != "_":
            print('This cell is occupied! Choose another one!')
            self.fill_coor()
        else:
            tmp_list = list(self.position)
            tmp_list[(x * 3) + y] = player
            self.position = ''.join(tmp_list)
            self.update_coor()
            print(str(self))

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

    def pvp_game(self):
        self.position = '_________'
        self.update_coor()
        print(str(self))

        def x_move():
            self.fill_coor('X')
        def o_move():
            self.fill_coor('O')
            
        while True:
            x_move()
            if self.check_condition() != "Game not finished":
                print(self.check_condition())
                input()
                exit()
            o_move()
            if self.check_condition() != "Game not finished":
                print(self.check_condition())
                input()
                exit()

this_is_suffering = TicTacToe('_________')
this_is_suffering.pvp_game()
            
            
