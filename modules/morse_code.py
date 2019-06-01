'''
On the Subject of Morse Code

• Interpret the signal from the flashing light using the Morse Code chart to spell one of the words in the table.
• The signal will loop, with a long gap between repetitions.
• Once the word is identified, set the corresponding frequency and press the transmit (TX) button.

-----------------------------------------------------------  ---------------------------
|                    How to Interpret                     |  |   If the   | Respond at |
|    1. A short flash represents a dot.                   |  |   word is: | frequency: |
|    2. A long flash represents a dash.                   |  |------------|------------|
|    3. There is a long gap between letters.              |  |    shell   |  3.505 MHz |
|    4. There is a very long gap before the word repeats. |  |------------|------------|
|                                                         |  |    halls   |  3.515 MHz |
|  A • ——                               U • • ——          |  |------------|------------|
|  B —— • • •                           V • • • ——        |  |    slick   |  3.522 MHz |
|  C —— • —— •                          W • —— ——         |  |------------|------------|
|  D —— • •                             X —— • • ——       |  |    trick   |  3.532 MHz |
|  E •                                  Y —— • —— ——      |  |------------|------------|
|  F • • —— •                           Z —— —— • •       |  |    boxes   |  3.535 MHz |
|  G —— —— •                                              |  |------------|------------|
|  H • • • •                                              |  |    leaks   |  3.542 MHz |
|  I • •                                                  |  |------------|------------|
|  J • —— —— ——                                           |  |   strobe   |  3.545 MHz |
|  K —— • ——                            1 • —— —— —— ——   |  |------------|------------|
|  L • —— • •                           2 • • —— —— ——    |  |   bistro   |  3.552 MHz |
|  M —— ——                              3 • • • —— ——     |  |------------|------------|
|  N —— •                               4 • • • • ——      |  |    flick   |  3.555 MHz |
|  O —— —— ——                           5 • • • • •       |  |------------|------------|
|  P • —— —— •                          6 —— • • • •      |  |    bombs   |  3.565 MHz |
|  Q —— —— • ——                         7 —— —— • • •     |  |------------|------------|
|  R • —— •                             8 —— —— —— • •    |  |    break   |  3.572 MHz |
|  S • • •                              9 —— —— —— —— •   |  |------------|------------|
|  T ——                                 0 —— —— —— —— ——  |  |    brick   |  3.575 MHz |
-----------------------------------------------------------  |------------|------------|
                                                             |    steak   |  3.582 MHz |
                                                             |------------|------------|
                                                             |    sting   |  3.592 MHz |
                                                             |------------|------------|
                                                             |   vector   |  3.595 MHz |
                                                             |------------|------------|
                                                             |    beats   |  3.600 MHz |
                                                             ---------------------------
'''

import modules.bomb

morse_to_letter_mapping = {
    '.-':    'a',
    '-...':  'b',
    '-.-.':  'c',
    '-..':   'd',
    '.':     'e',
    '..-.':  'f',
    '--.':   'g',
    '....':  'h',
    '..':    'i',
    '.---':  'j',
    '-.-':   'k',
    '.-..':  'l',
    '--':    'm',
    '-.':    'n',
    '---':   'o',
    '.--.':  'p',
    '--.-':  'q',
    '.-.':   'r',
    '...':   's',
    '-':     't',
    '..-':   'u',
    '...-':  'v',
    '.--':   'w',
    '-..-':  'x',
    '-.--':  'y',
    '--..':  'z',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '-----': '0',
}

word_to_frequency_mapping = {
    'shellshell': '3.505 MHz',
    'hallshalls': '3.515 MHz',
    'slickslick': '3.522 MHz',
    'tricktrick': '3.532 MHz',
    'boxesboxes': '3.535 MHz',
    'leaksleaks': '3.542 MHz',
    'strobestrobe': '3.545 MHz',
    'bistrobistro': '3.552 MHz',
    'flickflick': '3.555 MHz',
    'bombsbombs': '3.565 MHz',
    'breakbreak': '3.572 MHz',
    'brickbrick': '3.575 MHz',
    'steaksteak': '3.582 MHz',
    'stingsting': '3.592 MHz',
    'vectorvector': '3.595 MHz',
    'beatsbeats': '3.600 MHz',
}

class MorseCode:
    def __init__(self):
        self.parsed_speech = []
        self.solutions = {
            'shellshell'   : True,
            'hallshalls'   : True,
            'slickslick'   : True,
            'tricktrick'   : True,
            'boxesboxes'   : True,
            'leaksleaks'   : True,
            'strobestrobe' : True,
            'bistrobistro' : True,
            'flickflick'   : True,
            'bombsbombs'   : True,
            'breakbreak'   : True,
            'brickbrick'   : True,
            'steaksteak'   : True,
            'stingsting'   : True,
            'vectorvector' : True,
            'beatsbeats'   : True
        }
        self.possible_solutions = 16

    def try_parse_speech(self, recognized_speech: str) -> bool:
        words = recognized_speech.split()
        morse_characters = []

        for word in words:
            if word == 'short':
                morse_characters.append('.')
            elif word == 'long':
                morse_characters.append('-')
            else:
                print('Morse code module: invalid character (not dot or dash)!')
                return False

        letter = ''.join(morse_characters)
        if letter in morse_to_letter_mapping:
            self.parsed_speech.append(morse_to_letter_mapping[letter])
            return True
        else:
            print('Morse code module: invalid letter formed!')
            return False

    def solve_next_step(self, recognized_speech: str) -> str:
        if not self.try_parse_speech(recognized_speech):
            print('Morse code module: could not parse speech!')
            return ''

        current_word = ''.join(self.parsed_speech)
        for word in self.solutions:
            if (self.solutions[word] and (current_word not in word)):
                self.solutions[word] = False
                self.possible_solutions -=1

        if self.possible_solutions == 0:
            print('Morse code module: all possible words eliminated. Invalid state! Please restart the module.')
            return ''
        elif self.possible_solutions == 1:
            for word, is_solution in self.solutions.items():
                if is_solution:
                    return word_to_frequency_mapping[word]
        else:
            return current_word
