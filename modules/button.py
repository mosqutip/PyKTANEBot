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
    • If you start holding the button down, a colored strip will light up on the right side of the module. Based on its color you must release the button at a specific point in time:
    • Blue strip: release when the countdown timer has a 4 in any position.
    • White strip: release when the countdown timer has a 1 in any position.
    • Yellow strip: release when the countdown timer has a 5 in any position.
    • Any other color strip: release when the countdown timer has a 1 in any position.
'''

import modules.bomb

class Button:
    def __init__(self, parameters: str) -> None:
        self.parameters = parameters
        self.parse_parameters()

    def parse_parameters(self) -> None:
        words = self.parameters.split()
        if len(words) == 1:
            self.parsed_parameters = words
        else:
            if len(words) != 2:
                print('Invalid number of button parameters!')
                return

            self.parsed_parameters = {
                'color': words[0],
                'text': words[1],
            }

    def solve(self) -> str:
        if not modules.bomb.is_num_batteries_set:
            print('To solve a button module, I need to know how many batteries on are the bomb. \nYou can set the number of batteries by saying: "set batteries".')
        if not modules.bomb.is_indicators_set:
            print('To solve a button module, I need to know which 3-letter indicators are set (lit up) on the bomb. \nYou can set the indicators by saying: "set indicators".')
        if ((not modules.bomb.is_num_batteries_set) or (not modules.bomb.is_indicators_set)):
            return ''

        if isinstance(self.parsed_parameters, dict):
            if ((self.parsed_parameters['color'] == 'blue') and (self.parsed_parameters['text'] == 'abort')):
                return 'hold'
            elif ((modules.bomb.num_batteries > 1) and (self.parsed_parameters['text'] == 'detonate')):
                return 'press and immediately release'
            elif ((self.parsed_parameters['color'] == 'white') and ('car' in modules.bomb.indicators)):
                return 'hold'
            elif ((modules.bomb.num_batteries > 2) and ('freak' in modules.bomb.indicators)):
                return 'press and immediately release'
            elif self.parsed_parameters['color'] == 'yellow':
                return 'hold'
            elif ((self.parsed_parameters['color'] == 'red') and (self.parsed_parameters['text'] == 'hold')):
                return 'press and immediately release'
            else:
                return 'hold'
        else:
            if self.parsed_parameters == 'blue':
                return 'release when timer has a 4 in any position'
            elif self.parsed_parameters == 'white':
                return 'release when timer has a 1 in any position'
            elif self.parsed_parameters == 'yellow':
                return 'release when timer has a 5 in any position'
            else:
                return 'release when timer has a 1 in any position'
