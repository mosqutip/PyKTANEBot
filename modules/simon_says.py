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
    def __init__(self, parameters: str) -> None:
        if not modules.bomb.is_serial_set:
            print('To solve a Simon Says module, I need to know if the serial number contains a vowel. \nYou can set the serial number by saying: "set serial".')
            return

        self.parameters = parameters
        print(self.solve())

    def solve(self) -> str:
        if modules.bomb.does_serial_contain_vowel:
            if modules.bomb.strikes == 0:
                if self.parameters == 'red':
                    return 'blue'
                elif self.parameters == 'blue':
                    return 'red'
                elif self.parameters == 'green':
                    return 'yellow'
                elif self.parameters == 'yellow':
                    return 'green'
                else:
                    print('Invalid color parameter!')
                    return ''
            if modules.bomb.strikes == 1:
                if self.parameters == 'red':
                    return 'yellow'
                elif self.parameters == 'blue':
                    return 'green'
                elif self.parameters == 'green':
                    return 'blue'
                elif self.parameters == 'yellow':
                    return 'red'
                else:
                    print('Invalid color parameter!')
                    return ''
            if modules.bomb.strikes == 2:
                if self.parameters == 'red':
                    return 'green'
                elif self.parameters == 'blue':
                    return 'red'
                elif self.parameters == 'green':
                    return 'yellow'
                elif self.parameters == 'yellow':
                    return 'blue'
                else:
                    print('Invalid color parameter!')
                    return ''
        else:
            if modules.bomb.strikes == 0:
                if self.parameters == 'red':
                    return 'blue'
                elif self.parameters == 'blue':
                    return 'yellow'
                elif self.parameters == 'green':
                    return 'green'
                elif self.parameters == 'yellow':
                    return 'red'
                else:
                    print('Invalid color parameter!')
                    return ''
            if modules.bomb.strikes == 1:
                if self.parameters == 'red':
                    return 'red'
                elif self.parameters == 'blue':
                    return 'blue'
                elif self.parameters == 'green':
                    return 'yellow'
                elif self.parameters == 'yellow':
                    return 'green'
                else:
                    print('Invalid color parameter!')
                    return ''
            if modules.bomb.strikes == 2:
                if self.parameters == 'red':
                    return 'yellow'
                elif self.parameters == 'blue':
                    return 'green'
                elif self.parameters == 'green':
                    return 'blue'
                elif self.parameters == 'yellow':
                    return 'red'
                else:
                    print('Invalid color parameter!')
                    return ''
