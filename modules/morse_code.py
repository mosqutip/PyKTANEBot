'''
On the Subject of Morse Code

• Interpret the signal from the flashing light using the Morse Code chart to spell one of the words in the table.
• The signal will loop, with a long gap between repetitions.
• Once the word is identified, set the corresponding frequency and press the transmit (TX) button.

-----------------------------------------------------------  ---------------------------
|                    How to Interpret                     |  |   If the   | Respond at |
|    1. A short flash represents a dot.                   |  |   word is: | frequency: |
|    2. A long flash represents a dash.                   |  |------------|------------|
|    3. There is a long gap between letters.              |  |    shell   |  3.505 MHz |
|    4. There is a very long gap before the word repeats. |  |------------|------------|
|                                                         |  |    halls   |  3.515 MHz |
|  A • ——                               U • • ——          |  |------------|------------|
|  B —— • • •                           V • • • ——        |  |    slick   |  3.522 MHz |
|  C —— • —— •                          W • —— ——         |  |------------|------------|
|  D —— • •                             X —— • • ——       |  |    trick   |  3.532 MHz |
|  E •                                  Y —— • —— ——      |  |------------|------------|
|  F • • —— •                           Z —— —— • •       |  |    boxes   |  3.535 MHz |
|  G —— —— •                                              |  |------------|------------|
|  H • • • •                                              |  |    leaks   |  3.542 MHz |
|  I • •                                                  |  |------------|------------|
|  J • —— —— ——                                           |  |   strobe   |  3.545 MHz |
|  K —— • ——                            1 • —— —— —— ——   |  |------------|------------|
|  L • —— • •                           2 • • —— —— ——    |  |   bistro   |  3.552 MHz |
|  M —— ——                              3 • • • —— ——     |  |------------|------------|
|  N —— •                              4 • • • • ——       |  |    flick   |  3.555 MHz |
|  O —— —— ——                           5 • • • • •       |  |------------|------------|
|  P • —— —— •                          6 —— • • • •      |  |    bombs   |  3.565 MHz |
|  Q —— —— • ——                         7 —— —— • • •     |  |------------|------------|
|  R • —— •                             8 —— —— —— • •    |  |    break   |  3.572 MHz |
|  S • • •                              9 —— —— —— —— •   |  |------------|------------|
|  T ——                                 0 —— —— —— —— ——  |  |    brick   |  3.575 MHz |
-----------------------------------------------------------  |------------|------------|
                                                             |    steak   |  3.582 MHz |
                                                             |------------|------------|
                                                             |    sting   |  3.592 MHz |
                                                             |------------|------------|
                                                             |   vector   |  3.595 MHz |
                                                             |------------|------------|
                                                             |    beats   |  3.600 MHz |
                                                             ---------------------------
'''

import modules.bomb

class MorseCode:
    def __init__(self, parameters: str) -> None:
        self.parameters = parameters
        self.parse_parameters()

    def parse_parameters(self) -> None:
        return

    def solve(self) -> str:
        return ''
