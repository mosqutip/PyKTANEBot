'''
On the Subject of Passwords

• The buttons above and below each letter will cycle through the possibilities for that position.
• Only one combination of the available letters will match a password below.
• Press the submit button once the correct word has been set.

                 -----------------------------------------
                 | about | after | again | below | could |
                 | every | first | found | great | house |
                 | large | learn | never | other | place |
                 | plant | point | right | small | sound |
                 | spell | still | study | their | there |
                 | these | thing | think | three | water |
                 | where | which | world | would | write |
                 -----------------------------------------
'''

import modules.bomb

class Password:
    def __init__(self, parameters: str) -> None:
        self.parameters = parameters
        self.parse_parameters()

    def parse_parameters(self) -> None:
        return

    def solve(self) -> str:
        return ''
