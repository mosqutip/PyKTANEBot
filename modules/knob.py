'''
On the Subject of Knobs

• The knob can be turned to one of four different positions.
• The knob must be in the correct position when this module's timer hits zero.
• The correct position can be determined by the on/off configuration of the twelve LEDs.
• Knob positions are relative to the "UP" label, which may be rotated.

LED Configurations
Up Position:
-------------------------  -------------------------
|   |   | X |   | X | X |  | X |   | X |   | X |   |
|---|---|---|---|---|---|  |---|---|---|---|---|---|
| X | X | X | X |   | X |  |   | X | X |   | X | X |
-------------------------  -------------------------

Down Position:
-------------------------  -------------------------
|   | X | X |   |   | X |  | X |   | X |   | X |   |
|---|---|---|---|---|---|  |---|---|---|---|---|---|
| X | X | X | X |   | X |  |   | X |   |   |   | X |
-------------------------  -------------------------

Left Position:
-------------------------  -------------------------
|   |   |   |   | X |   |  |   |   |   |   | X |   |
|---|---|---|---|---|---|  |---|---|---|---|---|---|
| X |   |   | X | X | X |  |   |   |   | X | X |   |
-------------------------  -------------------------

Right Position:
-------------------------  -------------------------
| X |   | X | X | X | X |  | X |   | X | X |   |   |
|---|---|---|---|---|---|  |---|---|---|---|---|---|
| X | X | X |   |   | X |  | X | X | X |   | X |   |
-------------------------  -------------------------

X = Lit LED
'''

configurations = {
    'OOXOXXXXXXOX': 'up',
    'XOXOXOOXXOXX': 'up',
    'OXXOOXXXXXOX': 'down',
    'XOXOXOOXOOOX': 'down',
    'OOOOXOXOOXXX': 'left',
    'OOOOXOOOOXXO': 'left',
    'XOXXXXXXXOXO': 'right',
    'XOXXOOXXXOXO': 'right',
}

class Knob:
    def try_parse_speech(self, recognized_speech: str) -> bool:
        words = recognized_speech.split()
        lights = []
        for word in words:
            if word == 'on':
                lights.append('X')
            elif word == 'off':
                lights.append('O')
            else:
                print('Knob module: invalid state!')
                return False

        self.parsed_speech = ''.join(lights)
        return True

    def solve_next_step(self, recognized_speech: str) -> str:
        if not self.try_parse_speech(recognized_speech):
            print('Knob module: could not parse speech!')
            return ''

        if self.parsed_speech in configurations:
            return configurations[self.parsed_speech]
        else:
            print('Knob module: invalid light configuration!')
            return ''
