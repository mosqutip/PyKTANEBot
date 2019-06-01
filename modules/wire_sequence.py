'''
On the Subject of Wire Sequences

• Within this module there are several panels with wires on them, but only one panel is visible at a time.
  Switch to the next panel by using the down button and the previous panel by using the up button.
• Do not switch to the next panel until you are sure that you have cut all necessary wires on the current panel.
• Cut the wires as directed by the following table. Wire occurrences are cumulative over all panels within the module.

--------------------------------  --------------------------------  --------------------------------
|     Red Wire Occurrences     |  |     Blue Wire Occurrences    |  |    Black Wire Occurrences    |
|------------------------------|  |------------------------------|  |------------------------------|
| Wire Occurrence |   Out if   |  | Wire Occurrence |   Out if   |  | Wire Occurrence |   Out if   |
|                 |  connected |  |                 |  connected |  |                 |  connected |
|                 |     to:    |  |                 |     to:    |  |                 |     to:    |
--------------------------------  --------------------------------  -------------------------------
| First red       | C          |  | First blue      | B          |  | First black     | A, B or C  |
| occurrence      |            |  | occurrence      |            |  | occurrence      |            |
--------------------------------  --------------------------------  --------------------------------
| Second red      | B          |  | Second blue     | A or C     |  | Second black    | A or C     |
| occurrence      |            |  | occurrence      |            |  | occurrence      |            |
--------------------------------  --------------------------------  --------------------------------
| Third red       | A          |  | Third blue      | B          |  | Third black     | B          |
| occurrence      |            |  | occurrence      |            |  | occurrence      |            |
--------------------------------  --------------------------------  --------------------------------
| Fourth red      | A or C     |  | Fourth  lue     | A          |  | Fourth          | A or C     |
| occurrence      |            |  | occurrence      |            |  | occurrence      |            |
--------------------------------  --------------------------------  --------------------------------
| Fifth red       | B          |  | Fifth blue      | B          |  | Fifth black     | B          |
| occurrence      |            |  | occurrence      |            |  | occurrence      |            |
--------------------------------  --------------------------------  --------------------------------
| Sixth red       | A or C     |  | Sixth blue      | B or C     |  | Sixth black     | B or C     |
| occurrence      |            |  | occurrence      |            |  | occurrence      |            |
--------------------------------  --------------------------------  --------------------------------
| Seventh red     | A, B or C  |  | Seventh blue    | C          |  | Seventh black   | A or B     |
| occurrence      |            |  | occurrence      |            |  | occurrence      |            |
--------------------------------  --------------------------------  --------------------------------
| Eighth red      | A or B     |  | Eighth blue     | A or C     |  | Eighth black    | C          |
| occurrence      |            |  | occurrence      |            |  | occurrence      |            |
--------------------------------  --------------------------------  --------------------------------
| Ninth red       | B          |  | Ninth blue      | A          |  | Ninth black     | C          |
| occurrence      |            |  | occurrence      |            |  | occurrence      |            |
--------------------------------  --------------------------------  --------------------------------
'''

import modules.bomb

class WireSequence:
    def __init__(self):
        return

    def try_parse_speech(self, recognized_speech: str) -> bool:
        return False

    def solve_next_step(self, recognized_speech: str) -> str:
        return ''
