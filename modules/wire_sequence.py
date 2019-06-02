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

A = 0x4
B = 0x2
C = 0x1

red_cuts = [
    0x0, C, B, A, (A | C), B, (A | C), (A | B | C), (A | B), B
]

blue_cuts = [
    0x0, B, (A | C), B, A, B, (B | C), C, (A | C), A
]

black_cuts = [
    0x0, (A | B | C), (A | C), B, (A | C), B, (B | C), (A | B), C, C
]

class WireSequence:
    def __init__(self):
        self.red_count = 0
        self.blue_count = 0
        self.black_count = 0

    def try_parse_speech(self, recognized_speech: str) -> bool:
        recognized_speech = recognized_speech.replace('read', 'red')
        recognized_speech = recognized_speech.replace('bleu', 'blue')
        words = recognized_speech.split()
        if len(words) % 2 != 0:
            print('Wire sequence module: odd number of parameters!')
            return False

        self.parsed_speech = []
        for i in range(0, len(words), 2):
            if words[i + 1] == 'alpha':
                self.parsed_speech.append((words[i], A))
            elif words[i + 1] == 'bravo':
                self.parsed_speech.append((words[i], B))
            elif words[i + 1] == 'charlie':
                self.parsed_speech.append((words[i], C))

        return True

    def solve_next_step(self, recognized_speech: str) -> str:
        if not self.try_parse_speech(recognized_speech):
            print('Wire sequence module: could not parse speech!')
            return ''

        solution = []
        for wire in self.parsed_speech:
            if wire[0] == 'red':
                self.red_count += 1
                solution.append('cut') if (wire[1] & red_cuts[self.red_count]) else solution.append('do not cut')
            elif wire[0] == 'blue':
                self.blue_count += 1
                solution.append('cut') if (wire[1] & blue_cuts[self.blue_count]) else solution.append('do not cut')
            elif wire[0] == 'black':
                self.black_count += 1
                solution.append('cut') if (wire[1] & black_cuts[self.black_count]) else solution.append('do not cut')
            else:
                print('Wire sequence module: invalid wire color!')
                return ''

        return '\n'.join(solution)
