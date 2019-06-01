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

import modules.bomb

class Knob:
    def __init__(self):
        return

    def try_parse_speech(self, recognized_speech: str) -> bool:
        return False

    def solve_next_step(self, recognized_speech: str) -> str:
        return ''
