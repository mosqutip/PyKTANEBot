'''
On the Subject of Complicated Wires

• Look at each wire: there is an LED above the wire and a space for a "★" symbol below the wire.
• For each wire/LED/symbol combination, use the Venn diagram below to decide whether or not to cut the wire.
• Each wire may be striped with multiple colors.
'''

import modules.bomb

class ComplicatedWires:
    def try_parse_speech(self, recognized_speech: str) -> bool:
        if recognized_speech.endswith('next'):
            recognized_speech = recognized_speech[0:-5]

        wires = recognized_speech.split(' next ')
        if len(wires) < 1 or len(wires) > 6:
            print('Complicated wires module: invalid number of wires!')
            return False

        self.parsed_speech = []
        for wire in wires:
            wire_data = {
                'led': False,
                'blue': False,
                'red': False,
                'star': False
            }

            if 'light' in wire:
                wire_data['led'] = True
            elif 'blue' in wire:
                wire_data['blue'] = True
            elif 'red' in wire:
                wire_data['red'] = True
            elif 'star' in wire:
                wire_data['star'] = True
            else:
                print('Complicated wires module: invalid wire parameter!')
                return False

            self.parsed_speech.append(wire_data)

        return True

    def solve_next_step(self, recognized_speech: str) -> str:
        if not self.try_parse_speech(recognized_speech):
            print('Complicated wires module: could not parse speech!')
            return ''
        if not modules.bomb.is_num_batteries_set:
            print('To solve a complicated wires module, I need to know how many batteries on are the bomb.')
            print('You can enter bomb setup mode by saying: "initialize".')
            print('You can then set the number of batteries by saying: "set batteries".')
        if not modules.bomb.is_serial_set:
            print('To solve a complicated wires module, I need to know if the last digit of the serial number is even.')
            print('You can enter bomb setup mode by saying: "initialize".')
            print('You can then set the serial number by saying: "set serial".')
        if not modules.bomb.is_ports_set:
            print('To solve a complicated wires module, I need to know which ports are on the bomb.')
            print('You can enter bomb setup mode by saying: "initialize".')
            print('You can then set the ports by saying: "set ports".')
        if ((not modules.bomb.is_num_batteries_set) or (not modules.bomb.is_serial_set) or (not modules.bomb.is_ports_set)):
            return ''

        solution = []
        for wire in self.parsed_speech:
            if wire['led']:
                if wire['blue']:
                    if wire['red']:
                        if wire['star'] or modules.bomb.is_last_digit_of_serial_odd:
                            solution.append('do not cut')
                        else:
                            solution.append('cut')
                    elif 'parallel' in modules.bomb.ports:
                        solution.append('cut')
                    else:
                        solution.append('do not cut')
                elif ((modules.bomb.num_batteries >= 2) and (wire['red'] or wire['star'])):
                    solution.append('cut')
                else:
                    solution.append('do not cut')
            elif wire['star']:
                if wire['red']:
                    if wire['blue'] and 'parallel' not in modules.bomb.ports:
                        solution.append('do not cut')
                    else:
                        solution.append('cut')
                elif wire['blue']:
                    solution.append('do not cut')
                else:
                    solution.append('cut')
            elif wire['red'] or wire['blue']:
                if not modules.bomb.is_last_digit_of_serial_odd:
                    solution.append('cut')
                else:
                    solution.append('do not cut')
            else:
                solution.append('cut')

        return '\n'.join(solution)
