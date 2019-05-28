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

import modules.bomb

class Wires:
    def __init__(self, parameters: str) -> None:
        self.parameters = parameters
        self.parse_parameters()
        self.solve()

    def parse_parameters(self) -> None:
        words = self.parameters.split()
        self.parsed_parameters = {
            'wire_count': len(words),
            'last_wire': words[-1],
            'red_count': 0,
            'yellow_count': 0,
            'blue_count': 0,
            'white_count': 0,
            'black_count': 0
        }

        if ((self.parsed_parameters['wire_count'] < 3) or (self.parsed_parameters['wire_count'] > 6)):
            print('Invalid number of wires!')
            return

        for word in words:
            if word == 'red':
                self.parsed_parameters['red_count'] += 1
            elif word == 'yellow':
                self.parsed_parameters['yellow_count'] += 1
            elif word == 'blue':
                self.parsed_parameters['blue_count'] += 1
            elif word == 'white':
                self.parsed_parameters['white_count'] += 1
            elif word == 'black':
                self.parsed_parameters['black_count'] += 1
            else:
                print('Invalid wire color!')
                return

    def solve(self) -> str:
        if not modules.bomb.is_serial_set:
            print('To solve a wires module, I need to know if the last digit of the serial number is even or odd. \nYou can set the serial number by saying: "set serial".')
            return ''

        if self.parsed_parameters['wire_count'] == 3:
            if self.parsed_parameters['red_count'] == 0:
                return 'second'
            elif self.parsed_parameters['last_wire'] == 'white':
                return 'last'
            elif self.parsed_parameters['blue_count'] > 1:
                return 'last blue'
            else:
                return 'last'
        elif self.parsed_parameters['wire_count'] == 4:
            if ((self.parsed_parameters['red_count'] > 1) and modules.bomb.is_last_digit_of_serial_odd):
                return 'last red'
            elif ((self.parsed_parameters['last_wire'] == 'yellow') and (self.parsed_parameters['red_count'] == 0)):
                return 'first'
            elif self.parsed_parameters['blue_count'] == 1:
                return 'first'
            elif self.parsed_parameters['yellow_count'] > 1:
                return 'last'
            else:
                return 'second'
        elif self.parsed_parameters['wire_count'] == 5:
            if ((self.parsed_parameters['last_wire'] == 'black') and modules.bomb.is_last_digit_of_serial_odd):
                return 'fourth'
            elif ((self.parsed_parameters['red_count'] == 1) and (self.parsed_parameters['yellow_count'] > 1)):
                return 'first'
            elif self.parsed_parameters['black_count'] == 0:
                return 'second'
            else:
                return 'first'
        elif self.parsed_parameters['wire_count'] == 6:
            if ((self.parsed_parameters['yellow_count'] == 0) and modules.bomb.is_last_digit_of_serial_odd):
                return 'third'
            elif ((self.parsed_parameters['yellow_count'] == 1) and (self.parsed_parameters['white_count'] > 1)):
                return 'fourth'
            elif self.parsed_parameters['red_count'] == 0:
                return 'last'
            else:
                return 'fourth'
        else:
            print('Invalid wire parameters!')
            return ''
