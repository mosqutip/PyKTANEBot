'''
On the Subject of Wires

• A wire module can have 3-6 wires on it.
• Only the one correct wire needs to be cut to disarm the module.
• Wire ordering begins with the first on the top.

3 wires:
    If there are no red wires, cut the second wire.
    Otherwise, if the last wire is white, cut the last wire.
    Otherwise, if there is more than one blue wire, cut the last blue wire.
    Otherwise, cut the last wire.

4 wires:
    If there is more than one red wire and the last digit of the serial wire_countber is odd, cut the last red wire.
    Otherwise, if the last wire is yellow and there are no red wires, cut the first wire.
    Otherwise, if there is exactly one blue wire, cut the first wire.
    Otherwise, if there is more than one yellow wire, cut the last wire.
    Otherwise, cut the second wire.

5 wires:
    If the last wire is black and the last digit of the serial wire_countber is odd, cut the fourth wire.
    Otherwise, if there is exactly one red wire and there is more than one yellow wire, cut the first wire.
    Otherwise, if there are no black wires, cut the second wire.
    Otherwise, cut the first wire.

6 wires:
    If there are no yellow wires and the last digit of the serial wire_countber is odd, cut the third wire.
    Otherwise, if there is exactly one yellow wire and there is more than one white wire, cut the fourth wire.
    Otherwise, if there are no red wires, cut the last wire.
    Otherwise, cut the fourth wire.
'''

import sys
sys.path.append('..')

import config

class Wires:
    def try_parse_speech(self, recognized_speech: str) -> bool:
        words = recognized_speech.split()
        self.parsed_speech = {
            'wire_count': len(words),
            'last_wire': words[-1],
            'red_count': 0,
            'yellow_count': 0,
            'blue_count': 0,
            'white_count': 0,
            'black_count': 0
        }

        if ((self.parsed_speech['wire_count'] < 3) or (self.parsed_speech['wire_count'] > 6)):
            print('Wires module: invalid number of wires!')
            return False

        for word in words:
            if word == 'red':
                self.parsed_speech['red_count'] += 1
            elif word == 'yellow':
                self.parsed_speech['yellow_count'] += 1
            elif word == 'blue':
                self.parsed_speech['blue_count'] += 1
            elif word == 'white':
                self.parsed_speech['white_count'] += 1
            elif word == 'black':
                self.parsed_speech['black_count'] += 1
            else:
                print('Wires module: invalid wire color!')
                return False

        return True

    def solve_next_step(self, recognized_speech: str) -> str:
        if not self.try_parse_speech(recognized_speech):
            print('Wires module: could not parse speech!')
            return ''
        if not config.is_last_digit_of_serial_odd:
            print('To solve a wires module, I need to know if the last digit of the serial number is even or odd.')
            print('You can enter bomb setup mode by saying: "initialize".')
            print('You can then set the serial number by saying: "set serial".')
            return ''

        if self.parsed_speech['wire_count'] == 3:
            if self.parsed_speech['red_count'] == 0:
                return 'second'
            elif self.parsed_speech['last_wire'] == 'white':
                return 'last'
            elif self.parsed_speech['blue_count'] > 1:
                return 'last blue'
            else:
                return 'last'
        elif self.parsed_speech['wire_count'] == 4:
            if ((self.parsed_speech['red_count'] > 1) and config.is_last_digit_of_serial_odd):
                return 'last red'
            elif ((self.parsed_speech['last_wire'] == 'yellow') and (self.parsed_speech['red_count'] == 0)):
                return 'first'
            elif self.parsed_speech['blue_count'] == 1:
                return 'first'
            elif self.parsed_speech['yellow_count'] > 1:
                return 'last'
            else:
                return 'second'
        elif self.parsed_speech['wire_count'] == 5:
            if ((self.parsed_speech['last_wire'] == 'black') and config.is_last_digit_of_serial_odd):
                return 'fourth'
            elif ((self.parsed_speech['red_count'] == 1) and (self.parsed_speech['yellow_count'] > 1)):
                return 'first'
            elif self.parsed_speech['black_count'] == 0:
                return 'second'
            else:
                return 'first'
        elif self.parsed_speech['wire_count'] == 6:
            if ((self.parsed_speech['yellow_count'] == 0) and config.is_last_digit_of_serial_odd):
                return 'third'
            elif ((self.parsed_speech['yellow_count'] == 1) and (self.parsed_speech['white_count'] > 1)):
                return 'fourth'
            elif self.parsed_speech['red_count'] == 0:
                return 'last'
            else:
                return 'fourth'
        else:
            print('Wires module: invalid wire parameters!')
            return ''
