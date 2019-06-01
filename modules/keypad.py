'''
On the Subject of Keypads

• Only one column has all four of the symbols from the keypad.
• Press the four buttons in the order their symbols appear from top to bottom within that column.
'''

class Keypad:
    symbol_table = [
        [ 'oscar', 'tent', 'lambda', 'lightning', 'cat', 'hotel', 'backward' ],
        [ 'euro', 'oscar', 'backward', 'curly', 'light', 'hotel', 'question' ],
        [ 'copyright', 'whiskey', 'curly', 'squid', 'romeo', 'lambda', 'light' ],
        [ 'six', 'paragraph', 'bravo', 'cat', 'squid', 'question', 'smiley' ],
        [ 'trident', 'smiley', 'bravo', 'charlie', 'paragraph', 'three', 'dark' ],
        [ 'six', 'euro', 'railroad', 'greek', 'trident', 'russia', 'omega' ], #edit
    ]

    def try_parse_speech(self, recognized_speech: str) -> bool:
        self.parsed_speech = recognized_speech.replace('6', 'six')
        self.parsed_speech = self.parsed_speech.replace('3', 'three')
        self.parsed_speech = self.parsed_speech.split()

        if len(self.parsed_speech) != 4:
            print('Keypad module: wrong number of input symbols!')
            return False

        return True

    def solve_next_step(self, recognized_speech: str) -> str:
        if not self.try_parse_speech(recognized_speech):
            print('Keypad module: could not parse speech!')
            return ''

        for i in range(len(self.symbol_table)):
            output_symbols = [ '' ] * 4
            count = 0

            for j in range(len(self.symbol_table[0])):
                current_symbol = self.symbol_table[i][j]
                if current_symbol in self.parsed_speech:
                    output_symbols[count] = current_symbol
                    count += 1

                if count == 4:
                    return ', '.join(output_symbols)

        if count != 4:
            print('Keypad module: unrecognized symbol in input!')
            return ''
