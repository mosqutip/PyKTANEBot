'''
On the Subject of Passwords

• The buttons above and below each letter will cycle through the possibilities for that position.
• Only one combination of the available letters will match a password below.
• Press the submit button once the correct word has been set.

                 -----------------------------------------
                 | about | after | again | below | could |
                 | every | first | found | great | house |
                 | large | learn | never | other | place |
                 | plant | point | right | small | sound |
                 | spell | still | study | their | there |
                 | these | thing | think | three | water |
                 | where | which | world | would | write |
                 -----------------------------------------
'''

import modules.bomb
import utilities

class Password:
    def __init__(self):
        self.dials = {
            1: [],
            2: [],
            3: [],
            4: [],
            5: []
        }
        self.solutions = {
            'about': True, 'after': True, 'again': True, 'below': True, 'could': True,
            'every': True, 'first': True, 'found': True, 'great': True, 'house': True,
            'large': True, 'learn': True, 'never': True, 'other': True, 'place': True,
            'plant': True, 'point': True, 'right': True, 'small': True, 'sound': True,
            'spell': True, 'still': True, 'study': True, 'their': True, 'there': True,
            'these': True, 'thing': True, 'think': True, 'three': True, 'water': True,
            'where': True, 'which': True, 'world': True, 'would': True, 'write': True
        }
        self.possible_solutions = 35

    def try_parse_speech(self, recognized_speech: str) -> bool:
        if not recognized_speech.startswith('dial'):
            print('Password module: no dial given!')
            return False

        letters = recognized_speech.split()
        if len(letters) != 8:
            print('Password module: invalid number of arguments!')
            return False

        self.dial_number = utilities.string_to_number(letters[1])
        for letter in letters[2:]:
            self.dials[self.dial_number].append(utilities.parse_nato_to_letter(letter))

        return True

    def solve_next_step(self, recognized_speech: str) -> str:
        if not self.try_parse_speech(recognized_speech):
            print('Password module: could not parse speech!')
            return ''

        for word in self.solutions:
            if word[self.dial_number - 1] not in self.dials[self.dial_number]:
                self.solutions[word] = False
                self.possible_solutions -= 1

        if self.possible_solutions == 0:
            print('Password module: all possible words eliminated. Invalid state! Please restart the module.')
            return ''
        else:
            possible_passwords = ', '.join([word for word, is_solution in self.solutions.items() if is_solution])
            return f'Possible passwords: { possible_passwords }'
