'''
On the Subject of The Button

Follow these rules in the order they are listed. Perform the first action that applies:
    1. If the button is blue and the button says "Abort", hold the button and refer to "Releasing a Held Button".
    2. If there is more than 1 battery on the bomb and the button says "Detonate", press and immediately release the button.
    3. If the button is white and there is a lit indicator with label CAR, hold the button and refer to "Releasing a Held Button".
    4. If there are more than 2 batteries on the bomb and there is a lit indicator with label FRK, press and immediately release the button.
    5. If the button is yellow, hold the button and refer to "Releasing a Held Button".
    6. If the button is red and the button says "Hold", press and immediately release the button.
    7. If none of the above apply, hold the button and refer to "Releasing a Held Button".

Releasing a Held Button
If you start holding the button down, a colored strip will light up on the right side of the module.
Based on its color you must release the button at a specific point in time:
    • Blue strip: release when the countdown timer has a 4 in any position.
    • White strip: release when the countdown timer has a 1 in any position.
    • Yellow strip: release when the countdown timer has a 5 in any position.
    • Any other color strip: release when the countdown timer has a 1 in any position.
'''

import modules.bomb

class Button:
    def __init__(self):
        self.stage = 1

    def try_parse_speech(self, recognized_speech: str) -> bool:
        self.parsed_speech = recognized_speech.replace('read', 'red')
        # TODO: make sure single word is color?

        if self.stage == 1:
            words = self.parsed_speech.split()
            if len(words) != 2:
                print('Button module: invalid number of button parameters!')
                return False

            self.parsed_speech = {
                'color': words[0],
                'text': words[1],
            }

        return True

    def solve_next_step(self, recognized_speech: str) -> str:
        if not self.try_parse_speech(recognized_speech):
            print('Button module: could not parse speech!')
            return ''
        if not modules.bomb.is_num_batteries_set:
            print('To solve a button module, I need to know how many batteries on are the bomb.')
            print('You can enter bomb setup mode by saying: "initialize".')
            print('You can then set the number of batteries by saying: "set batteries".')
            return ''
        if not modules.bomb.is_indicators_set:
            print('To solve a button module, I need to know which indicators are lit on are the bomb.')
            print('You can enter bomb setup mode by saying: "initialize".')
            print('You can then set the indicators by saying: "set indicators".')
            return ''

        if self.stage == 1:
            solution = ''
            if ((self.parsed_speech['color'] == 'blue') and (self.parsed_speech['text'] == 'abort')):
                solution =  'hold'
            elif ((modules.bomb.num_batteries > 1) and (self.parsed_speech['text'] == 'detonate')):
                solution =  'press and immediately release'
            elif ((self.parsed_speech['color'] == 'white') and ('car' in modules.bomb.indicators)):
                solution =  'hold'
            elif ((modules.bomb.num_batteries > 2) and ('freak' in modules.bomb.indicators)):
                solution =  'press and immediately release'
            elif self.parsed_speech['color'] == 'yellow':
                solution =  'hold'
            elif ((self.parsed_speech['color'] == 'red') and (self.parsed_speech['text'] == 'hold')):
                solution =  'press and immediately release'
            else:
                solution =  'hold'
            self.stage += 1
            return solution
        elif self.stage == 2:
            if self.parsed_speech == 'blue':
                return 'release when timer has a 4 in any position'
            elif self.parsed_speech == 'white':
                return 'release when timer has a 1 in any position'
            elif self.parsed_speech == 'yellow':
                return 'release when timer has a 5 in any position'
            else:
                return 'release when timer has a 1 in any position'
