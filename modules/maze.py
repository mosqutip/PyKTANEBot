'''
On the Subject of Mazes

• Find the maze with matching circular markings.
• The defuser must navigate the white light to the red triangle using the arrow buttons.
•  WARNING: Do not cross the lines shown in the maze. These lines are invisible on the bomb.

========================= ========================= =========================
║ ◦   ◦   ◦ ║ ◦   ◦   ◦ ║ ║ ◦   ◦   ◦ ║ ◦   ◦   ◦ ║ ║ ◦   ◦   ◦ ║ ◦ ║ ◦   ◦ ║
║   ■===■   ║   ■=======║ ║===■   ■===■   ■   ■===║ ║   ■===■   ║   ■   ■   ║
║ o ║ ◦   ◦ ║ ◦   ◦   ◦ ║ ║ ◦   ◦ ║ ◦   ◦ ║ o   ◦ ║ ║ ◦ ║ ◦ ║ ◦ ║ ◦   ◦ ║ ◦ ║
║   ║   ■===║=======■   ║ ║   ■===■   ■=======■   ║ ║===■   ║   ║=======║   ║
║ ◦ ║ ◦   ◦ ║ ◦   ◦   o ║ ║ ◦ ║ ◦   ◦ ║ ◦   ◦   ◦ ║ ║ ◦   ◦ ║ ◦ ║ ◦   ◦ ║ ◦ ║
║   ║===■   ■   ■===■   ║ ║   ■   ■===■   ■===■   ║ ║   ■   ║   ║   ■   ║   ║
║ ◦ ║ ◦   ◦   ◦ ║ ◦   ◦ ║ ║ ◦   o ║ ◦   ◦ ║ ◦ ║ ◦ ║ ║ ◦ ║ ◦ ║ ◦ ║ o ║ ◦ ║ o ║
║   ■===============■   ║ ║   ■===║   ■===■   ║   ║ ║   ║   ■   ║   ║   ║   ║
║ ◦   ◦   ◦ ║ ◦   ◦ ║ ◦ ║ ║ ◦ ║ ◦ ║ ◦ ║ ◦   ◦ ║ ◦ ║ ║ ◦ ║ ◦   ◦ ║ ◦ ║ ◦ ║ ◦ ║
║   ■===■   ■   ■===■   ║ ║   ║   ■   ║   ■===■   ║ ║   ■=======■   ║   ║   ║
║ ◦   ◦ ║ ◦   ◦ ║ ◦   ◦ ║ ║ ◦ ║ ◦   ◦ ║ ◦   ◦   ◦ ║ ║ ◦   ◦   ◦   ◦ ║ ◦ ■ ◦ ║
========================= ========================= =========================
========================= ========================= =========================
║ o   ◦ ║ ◦   ◦   ◦   ◦ ║ ║ ◦   ◦   ◦   ◦   ◦   ◦ ║ ║ ◦ ║ ◦   ◦ ║ ◦   o   ◦ ║
║   ■   ║===========■   ║ ║===============■   ■   ║ ║   ║   ■   ║===■   ■   ║
║ ◦ ║ ◦ ║ ◦   ◦   ◦   ◦ ║ ║ ◦   ◦   ◦   ◦   ◦ ║ ◦ ║ ║ ◦ ║ ◦ ║ ◦ ║ ◦   ◦ ║ ◦ ║
║   ║   ■   ■=======■   ║ ║   ■=======■   ■=======║ ║   ■   ║   ║   ■===■   ║
║ ◦ ║ ◦   ◦ ║ ◦   ◦ ║ ◦ ║ ║ ◦   ◦ ║ ◦   ◦ ║ o   ◦ ║ ║ ◦   ◦ ║ ◦ ║ ◦ ║ ◦   ◦ ║
║   ║=======■    ===■   ║ ║   ■   ■=======║   ■   ║ ║   ■===║===■   ║   ■===║
║ o ║ ◦   ◦   ◦   ◦   ◦ ║ ║ ◦ ║ ◦   ◦   ◦ ║ ◦ ║ ◦ ║ ║ ◦   ◦ ║ ◦   ◦ ║ ◦ ║ ◦ ║
║   ■===============■   ║ ║   ║=======■   ■===■   ║ ║===■   ║   ■   ║   ■   ║
║ ◦   ◦   ◦   ◦   ◦ ║ ◦ ║ ║ ◦ ║ ◦   ◦   ◦   ◦ ║ ◦ ║ ║ ◦   ◦ ║ o ║ ◦ ║ ◦   ◦ ║
║   ■===========■   ║   ║ ║   ║   ■===========■   ║ ║   ■=======■   ║===■   ║
║ ◦   ◦   ◦ ║ ◦   ◦ ║ ◦ ║ ║ ◦ ║ ◦   ◦   o   ◦   ◦ ║ ║ ◦   ◦   ◦   ◦ ║ ◦   ◦ ║
========================= ========================= =========================
========================= ========================= =========================
║ ◦   o   ◦   ◦ ║ ◦   ◦ ║ ║ ◦ ║ ◦   ◦   o ║ ◦   ◦ ║ ║ ◦ ║ ◦   ◦   ◦   ◦   ◦ ║
║   ■=======■   ■   ■   ║ ║   ■   ■===■   ■   ■   ║ ║   ║   ■=======■   ■   ║
║ ◦ ║ ◦   ◦ ║ ◦   ◦ ║ ◦ ║ ║ ◦   ◦   ◦ ║ ◦   ◦ ║ ◦ ║ ║ ◦ ║ ◦ ║ o   ◦ ║ ◦ ║ ◦ ║
║   ■   ■===========■   ║ ║   ■===============║   ║ ║   ■   ■   ■===■   ║   ║
║ ◦   ◦ ║ ◦   ◦ ║ ◦   ◦ ║ ║ ◦ ║ ◦   ◦   ◦   ◦ ║ ◦ ║ ║ ◦   ◦   ◦ ║ ◦   ◦ ║ ◦ ║
║=======║   ■===■   ■===║ ║   ║   ■=======■   ■   ║ ║   ■=======■   ■===■   ║
║ ◦   ◦ ║ ◦   ◦   ◦ ║ ◦ ║ ║ ◦ ║ ◦   o ║ ◦   ◦   ◦ ║ ║ ◦ ║ ◦ ║ ◦   ◦ ║ ◦   ◦ ║
║   ■   ║   ■=======║   ║ ║   ║===■   ■===========║ ║   ║   ║   ■=======■   ║
║ ◦ ║ ◦ ║ ◦   ◦   ◦ ║ ◦ ║ ║ ◦ ║ ◦ ║ ◦   ◦   ◦   ◦ ║ ║ o ║ ◦ ║ ◦ ║ ◦   ◦ ║ ◦ ║
║   ■===========■   ║   ║ ║   ■   ■===============║ ║   ■   ║   ■   ■   ■===║
║ ◦   o   ◦   ◦   ◦ ■ ◦ ║ ║ ◦   ◦   ◦   ◦   ◦   ◦ ║ ║ ◦   ◦ ║ ◦   ◦ ║ ◦   ◦ ║
========================= ========================= =========================
'''

import utilities

maze0 = [
    "o o oxo o o",
    " xxx x xxxx",
    "oxo oxo o o",
    " x xxxxxxx ",
    "oxo oxo o o",
    " xxx x xxx ",
    "oxo o oxo o",
    " xxxxxxxxx ",
    "o o oxo oxo",
    " xxx x xxx ",
    "o oxo oxo o"
]

maze1 = [
    "o o oxo o o",
    "xx xxx x xx",
    "o oxo oxo o",
    " xxx xxxxx ",
    "oxo oxo o o",
    " x xxx xxx ",
    "o oxo oxoxo",
    " xxx xxx x ",
    "oxoxoxo oxo",
    " x x x xxx ",
    "oxo oxo o o"
]

maze2 = [
    "o o oxoxo o",
    " xxx x x x ",
    "oxoxoxo oxo",
    "xx x xxxxx ",
    "o oxoxo oxo",
    " x x x x x ",
    "oxoxoxoxoxo",
    " x x x x x ",
    "oxo oxoxoxo",
    " xxxxx x x ",
    "o o o oxo o"
]

maze3 = [
    "o oxo o o o",
    " x xxxxxxx ",
    "oxoxo o o o",
    " x x xxxxx ",
    "oxo oxo oxo",
    " xxxxx xxx ",
    "oxo o o o o",
    " xxxxxxxxx ",
    "o o o o oxo",
    " xxxxxxx x ",
    "o o oxo oxo"
]

maze4 = [
    "o o o o o o",
    "xxxxxxxx x ",
    "o o o o oxo",
    " xxxxx xxxx",
    "o oxo oxo o",
    " x xxxxx x ",
    "oxo o oxoxo",
    " xxxxx xxx ",
    "oxo o o oxo",
    " x xxxxxxx ",
    "oxo o o o o"
]

maze5 = [
    "oxo oxo o o",
    " x x xxx x ",
    "oxoxoxo oxo",
    " x x x xxx ",
    "o oxoxoxo o",
    " xxxxx x xx",
    "o oxo oxoxo",
    "xx x x x x ",
    "o oxoxoxo o",
    " xxxxx xxx ",
    "o o o oxo o"
]

maze6 = [
    "o o o oxo o",
    " xxxxx x x ",
    "oxo oxo oxo",
    " x xxxxxxx ",
    "o oxo oxo o",
    "xxxx xxx xx",
    "o oxo o oxo",
    " x x xxxxx ",
    "oxoxo o oxo",
    " xxxxxxx x ",
    "o o o o o o"
]

maze7 = [
    "oxo o oxo o",
    " x xxx x x ",
    "o o oxo oxo",
    " xxxxxxxxx ",
    "oxo o o oxo",
    " x  xxxx x ",
    "oxo oxo o o",
    " xxx xxxxxx",
    "oxoxo o o o",
    " x xxxxxxxx",
    "o o o o o o"
]

maze8 = [
    "oxo o o o o",
    " x xxxxx x ",
    "oxoxo oxoxo",
    " x x xxx x ",
    "o o oxo oxo",
    " xxxxx xxx ",
    "oxoxo oxo o",
    " x x xxxxx ",
    "oxoxoxo oxo",
    " x x x x xx",
    "o oxo oxo o"
]

coordinate_to_maze_number = {
    (2,  0): maze0,
    (4, 10): maze0,
    (2,  8): maze1,
    (6,  2): maze1,
    (6,  6): maze2,
    (6, 10): maze2,
    (0,  0): maze3,
    (6,  0): maze3,
    (4,  8): maze4,
    (10, 6): maze4,
    (0,  8): maze5,
    (8,  4): maze5,
    (0,  2): maze6,
    (10, 2): maze6,
    (0,  6): maze7,
    (6,  4): maze7,
    (2,  4): maze8,
    (8,  0): maze8
}

maze_width = maze_height = 10

class Maze:
    def try_parse_speech(self, recognized_speech: str) -> bool:
        recognized_speech = recognized_speech.replace('-', '')
        if recognized_speech.endswith('next'):
            recognized_speech = recognized_speech[0:-5]
        coordinates = recognized_speech.split(' next ')

        if len(coordinates) != 4:
            print('Maze module: invalid number of coordinates!')
            return False

        self.parsed_speech = []
        for coordinate in coordinates:
            stripped_coordinate = coordinate.strip()
            coordinate_data = {
                'circle': False,
                'triangle': False,
                'square': False,
                'numbers': []
            }

            if 'circle' in stripped_coordinate:
                coordinate_data['circle'] = True
                stripped_coordinate = stripped_coordinate.replace('circle', '')
            elif 'triangle' in stripped_coordinate:
                coordinate_data['triangle'] = True
                stripped_coordinate = stripped_coordinate.replace('triangle', '')
            elif 'square' in stripped_coordinate:
                coordinate_data['square'] = True
                stripped_coordinate = stripped_coordinate.replace('square', '')
            else:
                print('Maze module: invalid coordinate parameter!')
                return False

            # Strip again to remove any errant spaces
            numbers = stripped_coordinate.strip()

            # Assume the coordinates were parsed as one number, e.g. (5, 3) -> '53'
            if len(numbers.split()) == 1:
                digits = [digit for digit in numbers]
            elif len(numbers.split()) == 2:
                digits = numbers.split()
            else:
                print('Maze module: invalid number of coordinates!')
                return False

            for digit in digits:
                translated_value = ((utilities.string_to_number(digit) * 2) - 2)
                coordinate_data['numbers'].append(translated_value)

            self.parsed_speech.append(coordinate_data)

        return True

    def solve_next_step(self, recognized_speech: str) -> str:
        if not self.try_parse_speech(recognized_speech):
            print('Maze module: could not parse speech!')
            return ''

        circle_coordinates = []
        self.start_coordinate = None
        self.end_coordinate = None
        for coordinate in self.parsed_speech:
            if coordinate['circle']:
                circle_coordinates.append((coordinate['numbers'][0], coordinate['numbers'][1]))
            elif coordinate['square']:
                self.start_coordinate = (coordinate['numbers'][0], coordinate['numbers'][1])
            elif coordinate['triangle']:
                self.end_coordinate = (coordinate['numbers'][0], coordinate['numbers'][1])

        self.maze = ''
        if ((circle_coordinates[0] in coordinate_to_maze_number) and (circle_coordinates[1] in coordinate_to_maze_number)):
            self.maze = coordinate_to_maze_number[circle_coordinates[0]]
            self.visited = [[False for i in range(11)] for j in range(11)]
        else:
            print('Maze module: invalid coordinates!')
            return False

        steps = []
        self.solve_maze_recursive(self.start_coordinate[0], self.start_coordinate[1], steps)
        steps.reverse()
        return ', '.join(steps)

    def solve_maze_recursive(self, x: int, y: int, steps: [str]) -> bool:
        if (x, y) == self.end_coordinate:
            return True

        if ((self.maze[x][y] == 'x') or (self.visited[x][y] == True)):
            return False

        self.visited[x][y] = True

        if x != 0:
            if self.solve_maze_recursive((x - 1), y, steps):
                if (self.maze[x][y] == 'o'):
                    steps.append('up')

                return True

        if x != maze_height:
            if self.solve_maze_recursive((x + 1), y, steps):
                if self.maze[x][y] == 'o':
                    steps.append('down')

                return True

        if y != 0:
            if self.solve_maze_recursive(x, (y - 1), steps):
                if self.maze[x][y] == 'o':
                    steps.append('left')

                return True

        if y != maze_height:
            if self.solve_maze_recursive(x, (y + 1), steps):
                if self.maze[x][y] == 'o':
                    steps.append('right')

                return True

        return False
