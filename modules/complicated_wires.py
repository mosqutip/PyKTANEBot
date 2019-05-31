'''
On the Subject of Complicated Wires

• Look at each wire: there is an LED above the wire and a space for a "★" symbol below the wire.
• For each wire/LED/symbol combination, use the Venn diagram below to decide whether or not to cut the wire.
• Each wire may be striped with multiple colors.
'''

import modules.bomb

class ComplicatedWires:
    def __init__(self, parameters: str) -> None:
        if not modules.bomb.is_num_batteries_set:
            print('To solve a complicated wires module, I need to know how many batteries on are the bomb. \nYou can set the number of batteries by saying: "set batteries".')
        if not modules.bomb.is_serial_set:
            print('To solve a complicated wires module, I need to know if the last digit of the serial number is even. \nYou can set the serial by saying: "set serial".')
        if not modules.bomb.is_ports_set:
            print('To solve a complicated wires module, I need to know which ports are on the bomb. \nYou can set the ports by saying: "set ports".')
        if ((not modules.bomb.is_num_batteries_set) or (not modules.bomb.is_serial_set) or (not modules.bomb.is_ports_set)):
            return

        self.parameters = parameters
        self.parse_parameters()
        print(self.solve())

    def parse_parameters(self) -> None:
        wires = self.parameters.rstrip('next')
        wires = wires.rstrip('done')
        wires = wires.split('next')
        if len(wires) < 1 or len(wires) > 6:
            print('Wrong number of wires!')
            return

        self.parsed_parameters = []
        for wire in wires:
            wire_data = {
                'led': False,
                'blue': False,
                'red': False,
                'star': False
            }

            if 'light' in wire:
                wire_data['led'] = True
            if 'blue' in wire:
                wire_data['blue'] = True
            if 'red' in wire:
                wire_data['red'] = True
            if 'star' in wire:
                wire_data['star'] = True

            self.parsed_parameters.append(wire_data)

    def solve(self) -> str:
        if not self.parse_parameters:
            print('Module initialization failed! Please re-initialize module.')
            return ''

        result = []
        for wire in self.parsed_parameters:
            if wire['led']:
                if wire['blue']:
                    if wire['red']:
                        if wire['star'] or modules.bomb.is_last_digit_of_serial_odd:
                            result.append('do not cut')
                        else:
                            result.append('cut')
                    elif 'parallel' in modules.bomb.ports:
                        result.append('cut')
                    else:
                        result.append('do not cut')
                elif ((modules.bomb.num_batteries >= 2) and (wire['red'] or wire['star'])):
                    result.append('cut')
                else:
                    result.append('do not cut')
            elif wire['star']:
                if wire['red']:
                    if wire['blue'] and 'parallel' not in modules.bomb.ports:
                        result.append('do not cut')
                    else:
                        result.append('cut')
                elif wire['blue']:
                    result.append('do not cut')
                else:
                    result.append('cut')
            elif wire['red'] or wire['blue']:
                if not modules.bomb.is_last_digit_of_serial_odd:
                    result.append('cut')
                else:
                    result.append('do not cut')
            else:
                result.append('cut')

        return '\n'.join(result)
