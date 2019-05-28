'''
On the Subject of Keypads
    • Only one column has all four of the symbols from the keypad.
    • Press the four buttons in the order their symbols appear from top to bottom within that column.
'''

import modules.bomb

class Keypad:
    symbol_table = [
        [ 'oscar', 'tent', 'lambda', 'lightning', 'kitty', 'hotel', 'backward' ],
        [ 'euro', 'oscar', 'backward', 'curly', 'light', 'hotel', 'question' ],
        [ 'copyright', 'butt', 'curly', 'squid', 'romeo', 'lambda', 'light' ],
        [ 'six', 'paragraph', 'bravo', 'kitty', 'squid', 'question', 'smiley' ],
        [ 'psych', 'smiley', 'bravo', 'charlie', 'paragraph', 'three', 'dark' ],
        [ 'six', 'euro', 'railroad', 'greek', 'psych', 'russia', 'omega' ],
    ]

    def __init__(self, parameters: str) -> None:
        self.parameters = parameters
        self.parse_parameters()

    def parse_parameters(self) -> None:
        self.parsed_parameters = self.parameters.split()

        if len(self.parsed_parameters) != 4:
            print('Wrong number of input symbols!')
            return

    def solve(self) -> str:
        for i in range(len(self.symbol_table)):
            output_symbols = [ '' ] * 4
            count = 0

            for j in range(len(self.symbol_table[0])):
                current_symbol = self.symbol_table[i][j]
                if current_symbol in self.parsed_parameters:
                    output_symbols[count] = current_symbol
                    count += 1

                if count == 4:
                    return output_symbols

        if count != 4:
            print('Unrecognized symbol in input!')
            return ''
