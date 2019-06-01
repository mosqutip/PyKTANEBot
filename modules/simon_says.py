'''
On the Subject of Simon Says

1. One of the four colored buttons will flash.
2. Using the correct table below, press the button with the corresponding color.
3. The original button will flash, followed by another. Repeat this sequence in order using the color mapping.
4. The sequence will lengthen by one each time you correctly enter a sequence until the module is disarmed.

       --------------
       |          o |
       |     /\ <---|-Blue
  Red -|--> /\/\    |
       |    \/\/ <--|-Yellow
Green -|---> \/     |
       |            |
       --------------

If the serial number contains a vowel:
                                -------------------------------------
                                |   Red  |  Blue  |  Green | Yellow |
                                |  Flash |  Flash |  Flash |  Flash |
--------------------------------|--------|--------|--------|--------|
|                  | No Strikes |  Blue  |   Red  | Yellow |  Green |
|                  | -----------|--------|--------|--------|--------|
| Button to press: |  1 Strike  | Yellow |  Green |  Blue  |   Red  |
|                  | -----------|--------|--------|--------|--------|
|                  |  2 Strikes |  Green |   Red  | Yellow |  Blue  |
---------------------------------------------------------------------

If the serial number does not contain a vowel:
                                -------------------------------------
                                |   Red  |  Blue  |  Green | Yellow |
                                |  Flash |  Flash |  Flash |  Flash |
--------------------------------|--------|--------|--------|--------|
|                  | No Strikes |  Blue  | Yellow |  Green |   Red  |
|                  | -----------|--------|--------|--------|--------|
| Button to press: |  1 Strike  |   Red  |  Blue  | Yellow |  Green |
|                  | -----------|--------|--------|--------|--------|
|                  |  2 Strikes | Yellow |  Green |  Blue  |   Red  |
---------------------------------------------------------------------
'''

import modules.bomb

class SimonSays:
    def __init__(self) -> None:
        self.stage = 1
        self.press_history = []

    def try_parse_speech(self, recognized_speech: str) -> bool:
        self.parsed_speech = recognized_speech
        return True

    def solve_next_step(self, recognized_speech: str) -> str:
        if not modules.bomb.is_serial_set:
            print('To solve a Simon Says module, I need to know if the serial number contains a vowel.')
            print('You can enter bomb setup mode by saying: "initialize".')
            print('You can then set the serial number by saying: "set serial".')
            return ''

        solution = ''
        if modules.bomb.does_serial_contain_vowel:
            if modules.bomb.strikes == 0:
                if self.parsed_speech == 'red':
                    solution = 'blue'
                elif self.parsed_speech == 'blue':
                    solution = 'red'
                elif self.parsed_speech == 'green':
                    solution = 'yellow'
                elif self.parsed_speech == 'yellow':
                    solution = 'green'
            if modules.bomb.strikes == 1:
                if self.parsed_speech == 'red':
                    solution = 'yellow'
                elif self.parsed_speech == 'blue':
                    solution = 'green'
                elif self.parsed_speech == 'green':
                    solution = 'blue'
                elif self.parsed_speech == 'yellow':
                    solution = 'red'
            if modules.bomb.strikes == 2:
                if self.parsed_speech == 'red':
                    solution = 'green'
                elif self.parsed_speech == 'blue':
                    solution = 'red'
                elif self.parsed_speech == 'green':
                    solution = 'yellow'
                elif self.parsed_speech == 'yellow':
                    solution = 'blue'
        else:
            if modules.bomb.strikes == 0:
                if self.parsed_speech == 'red':
                    solution = 'blue'
                elif self.parsed_speech == 'blue':
                    solution = 'yellow'
                elif self.parsed_speech == 'green':
                    solution = 'green'
                elif self.parsed_speech == 'yellow':
                    solution = 'red'
            if modules.bomb.strikes == 1:
                if self.parsed_speech == 'red':
                    solution = 'red'
                elif self.parsed_speech == 'blue':
                    solution = 'blue'
                elif self.parsed_speech == 'green':
                    solution = 'yellow'
                elif self.parsed_speech == 'yellow':
                    solution = 'green'
            if modules.bomb.strikes == 2:
                if self.parsed_speech == 'red':
                    solution = 'yellow'
                elif self.parsed_speech == 'blue':
                    solution = 'green'
                elif self.parsed_speech == 'green':
                    solution = 'blue'
                elif self.parsed_speech == 'yellow':
                    solution = 'red'

        if solution == '':
            print('Simon Says module: invalid color parameter!')
            return ''
        else:
            self.stage += 1
            self.press_history.append(solution)
            return ', '.join(self.press_history)
 