'''
On the Subject of Who’s on First

1. Read the display and use step 1 to determine which button label to read.
2. Using this button label, use step 2 determine whichbutton to push.
3. Repeat until the module has been disarmed.

Step 1:
Based on the display, read the label of a particular button and proceed to step 2:

-------------  -------------  -------------  -------------  -------------  -------------
|    YES    |  |   FIRST   |  |  DISPLAY  |  |    OKAY   |  |    SAYS   |  |  NOTHING  |
|-----------|  |-----------|  |-----------|  |-----------|  |-----------|  |-----------|
|     |     |  |     |  o  |  |     |     |  |     |  o  |  |     |     |  |     |     |
|-----|-----|  |-----------|  |-----------|  |-----------|  |-----------|  |-----------|
|  o  |     |  |     |     |  |     |     |  |     |     |  |     |     |  |  o  |     |
|-----|-----|  |-----------|  |-----------|  |-----------|  |-----------|  |-----------|
|     |     |  |     |     |  |     |  o  |  |     |     |  |     |  o  |  |     |     |
-------------  -------------  -------------  -------------  -------------  -------------

-------------  -------------  -------------  -------------  -------------  -------------
|           |  |   BLANK   |  |     NO    |  |    LED    |  |    LEAD   |  |    READ   |
|-----------|  |-----------|  |-----------|  |-----------|  |-----------|  |-----------|
|     |     |  |     |     |  |     |     |  |     |     |  |     |     |  |     |     |
|-----------|  |-----------|  |-----------|  |-----------|  |-----------|  |-----------|
|     |     |  |     |  o  |  |     |     |  |  o  |     |  |     |     |  |     |  o  |
|-----------|  |-----------|  |-----------|  |-----------|  |-----------|  |-----------|
|  o  |     |  |     |     |  |     |  o  |  |     |     |  |     |  o  |  |     |     |
-------------  -------------  -------------  -------------  -------------  -------------

-------------  -------------  -------------  -------------  -------------  -------------
|    RED    |  |    REED   |  |    LEED   |  |  HOLD ON  |  |    YOU    |  |  YOU ARE  |
|-----------|  |-----------|  |-----------|  |-----------|  |-----------|  |-----------|
|     |     |  |     |     |  |     |     |  |     |     |  |     |     |  |     |     |
|-----------|  |-----------|  |-----------|  |-----------|  |-----------|  |-----------|
|     |  o  |  |     |     |  |     |     |  |     |     |  |     |  o  |  |     |     |
|-----------|  |-----------|  |-----------|  |-----------|  |-----------|  |-----------|
|     |     |  |  o  |     |  |  o  |     |  |     |  o  |  |     |     |  |     |  o  |
-------------  -------------  -------------  -------------  -------------  -------------

-------------  -------------  -------------  -------------  -------------  -------------
|    YOUR   |  |   YOU'RE  |  |     UR    |  |   THERE   |  |  THEY'RE  |  |   THEIR   |
|-----------|  |-----------|  |-----------|  |-----------|  |-----------|  |-----------|
|     |     |  |     |     |  |  o  |     |  |     |     |  |     |     |  |     |     |
|-----------|  |-----------|  |-----------|  |-----------|  |-----------|  |-----------|
|     |  o  |  |     |  o  |  |     |     |  |     |     |  |     |     |  |     |  o  |
|-----------|  |-----------|  |-----------|  |-----------|  |-----------|  |-----------|
|     |     |  |     |     |  |     |     |  |     |  o  |  |  o  |     |  |     |     |
-------------  -------------  -------------  -------------  -------------  -------------

             -------------  -------------  -------------  -------------
             | THEY ARE  |  |    SEE    |  |     C     |  |    CEE    |
             |-----------|  |-----------|  |-----------|  |-----------|
             |     |     |  |     |     |  |     |  o  |  |     |     |
             |-----------|  |-----------|  |-----------|  |-----------|
             |  o  |     |  |     |     |  |     |     |  |     |     |
             |-----------|  |-----------|  |-----------|  |-----------|
             |     |     |  |     |  o  |  |     |     |  |     |  o  |
             -------------  -------------  -------------  -------------

Step 2:
Using the label from step 1, push the first button that appears in its corresponding list:

----------------------------------------------------------------------------------------------------------
|  "READY":  | YES, OKAY, WHAT, MIDDLE, LEFT, PRESS, RIGHT, BLANK, READY, NO, FIRST, UHHH, NOTHING, WAIT |
|--------------------------------------------------------------------------------------------------------|
|  "FIRST":  | LEFT, OKAY, YES, MIDDLE, NO, RIGHT, NOTHING, UHHH, WAIT, READY, BLANK, WHAT, PRESS, FIRST |
|--------------------------------------------------------------------------------------------------------|
|    "NO":   | BLANK, UHHH, WAIT, FIRST, WHAT, READY, RIGHT, YES, NOTHING, LEFT, PRESS, OKAY, NO, MIDDLE |
|--------------------------------------------------------------------------------------------------------|
|  "BLANK":  | WAIT, RIGHT, OKAY, MIDDLE, BLANK, PRESS, READY, NOTHING, NO, WHAT, LEFT, UHHH, YES, FIRST |
|--------------------------------------------------------------------------------------------------------|
| "NOTHING": | UHHH, RIGHT, OKAY, MIDDLE, YES, BLANK, NO, PRESS, LEFT, WHAT, WAIT, FIRST, NOTHING, READY |
|--------------------------------------------------------------------------------------------------------|
|   "YES":   | OKAY, RIGHT, UHHH, MIDDLE, FIRST, WHAT, PRESS, READY, NOTHING, YES, LEFT, BLANK, NO, WAIT |
|--------------------------------------------------------------------------------------------------------|
|   "WHAT":  | UHHH, WHAT, LEFT, NOTHING, READY, BLANK, MIDDLE, NO, OKAY, FIRST, WAIT, YES, PRESS, RIGHT |
|--------------------------------------------------------------------------------------------------------|
|   "UHHH":  | READY, NOTHING, LEFT, WHAT, OKAY, YES, RIGHT, NO, PRESS, BLANK, UHHH, MIDDLE, WAIT, FIRST |
|--------------------------------------------------------------------------------------------------------|
|   "LEFT":  | RIGHT, LEFT, FIRST, NO, MIDDLE, YES, BLANK, WHAT, UHHH, WAIT, PRESS, READY, OKAY, NOTHING |
|--------------------------------------------------------------------------------------------------------|
|  "RIGHT":  | YES, NOTHING, READY, PRESS, NO, WAIT, WHAT, RIGHT, MIDDLE, LEFT, UHHH, BLANK, OKAY, FIRST |
|--------------------------------------------------------------------------------------------------------|
|  "MIDDLE": | BLANK, READY, OKAY, WHAT, NOTHING, PRESS, NO, WAIT, LEFT, MIDDLE, RIGHT, FIRST, UHHH, YES |
|--------------------------------------------------------------------------------------------------------|
|   "OKAY":  | MIDDLE, NO, FIRST, YES, UHHH, NOTHING, WAIT, OKAY, LEFT, READY, BLANK, PRESS, WHAT, RIGHT |
|--------------------------------------------------------------------------------------------------------|
|   "WAIT":  | UHHH, NO, BLANK, OKAY, YES, LEFT, FIRST, PRESS, WHAT, WAIT, NOTHING, READY, RIGHT, MIDDLE |
|--------------------------------------------------------------------------------------------------------|
|  "PRESS":  | RIGHT, MIDDLE, YES, READY, PRESS, OKAY, NOTHING, UHHH, BLANK, LEFT, FIRST, WHAT, NO, WAIT |
|--------------------------------------------------------------------------------------------------------|
|   "YOU":   | SURE, YOU ARE, YOUR, YOU'RE, NEXT, UH HUH, UR, HOLD, WHAT?, YOU, UH UH, LIKE, DONE, U     |
|--------------------------------------------------------------------------------------------------------|
| "YOU ARE": | YOUR, NEXT, LIKE, UH HUH, WHAT?, DONE, UH UH, HOLD, YOU, U, YOU'RE, SURE, UR, YOU ARE     |
|--------------------------------------------------------------------------------------------------------|
|   "YOUR":  | UH UH, YOU ARE, UH HUH, YOUR, NEXT, UR, SURE, U, YOU'RE, YOU, WHAT?, HOLD, LIKE, DONE     |
|--------------------------------------------------------------------------------------------------------|
|  "YOU'RE": | YOU, YOU'RE, UR, NEXT, UH UH, YOU ARE, U, YOUR, WHAT?, UH HUH, SURE, DONE, LIKE, HOLD     |
|--------------------------------------------------------------------------------------------------------|
|    "UR":   | DONE, U, UR, UH HUH, WHAT?, SURE, YOUR, HOLD, YOU'RE, LIKE, NEXT, UH UH, YOU ARE, YOU     |
|--------------------------------------------------------------------------------------------------------|
|    "U":    | UH HUH, SURE, NEXT, WHAT?, YOU'RE, UR, UH UH, DONE, U, YOU, LIKE, HOLD, YOU ARE, YOUR     |
|--------------------------------------------------------------------------------------------------------|
|  "UH HUH": | UH HUH, YOUR, YOU ARE, YOU, DONE, HOLD, UH UH, NEXT, SURE, LIKE, YOU'RE, UR, U, WHAT?     |
|--------------------------------------------------------------------------------------------------------|
|  "UH UH":  | UR, U, YOU ARE, YOU'RE, NEXT, UH UH, DONE, YOU, UH HUH, LIKE, YOUR, SURE, HOLD, WHAT?     |
|--------------------------------------------------------------------------------------------------------|
|  "WHAT?":  | YOU, HOLD, YOU'RE, YOUR, U, DONE, UH UH, LIKE, YOU ARE, UH HUH, UR, NEXT, WHAT?, SURE     |
|--------------------------------------------------------------------------------------------------------|
|   "DONE":  | SURE, UH HUH, NEXT, WHAT?, YOUR, UR, YOU'RE, HOLD, LIKE, YOU, U, YOU ARE, UH UH, DONE     |
|--------------------------------------------------------------------------------------------------------|
|   "NEXT":  | WHAT?, UH HUH, UH UH, YOUR, HOLD, SURE, NEXT, LIKE, DONE, YOU ARE, UR, YOU'RE, U, YOU     |
|--------------------------------------------------------------------------------------------------------|
|   "HOLD":  | YOU ARE, U, DONE, UH UH, YOU, UR, SURE, WHAT?, YOU'RE, NEXT, HOLD, UH HUH, YOUR, LIKE     |
|--------------------------------------------------------------------------------------------------------|
|   "SURE":  | YOU ARE, DONE, LIKE, YOU'RE, YOU, HOLD, UH HUH, UR, SURE, U, WHAT?, NEXT, YOUR, UH UH     |
|--------------------------------------------------------------------------------------------------------|
|   "LIKE":  | YOU'RE, NEXT, U, UR, HOLD, DONE, UH UH, WHAT?, UH HUH, YOU, LIKE, SURE, YOU ARE, YOUR     |
----------------------------------------------------------------------------------------------------------
'''

import modules.bomb

class WhosOnFirst:
    step_one_word_mapping = {
        'yes': 'middle left',
        'first': 'upper right',
        'display': 'lower right',
        'okay': 'upper right',
        'says': 'lower right',
        'nothing': 'middle left',
        'null': 'lower left',
        'blank': 'middle right',
        'no': 'lower right',
        'light': 'middle left',
        'lead metal': 'lower right',
        'read book': 'middle right',
        'red color': 'middle right',
        'reed plant': 'lower left',
        'lead energy': 'lower left',
        'hold on': 'lower right',
        'you': 'middle right',
        'you are': 'lower right',
        'your possessive': 'middle right',
        'you are contraction': 'middle right',
        'you are letters': 'upper left',
        'there location': 'lower right',
        'their location': 'lower right',
        'they are contraction': 'lower left',
        'their possessive': 'middle right',
        'there possessive': 'middle right',
        'they are': 'middle left',
        'see': 'lower right',
        'sea': 'lower right',
        'c': 'lower right',
        'see letter': 'upper right',
        'sea letter': 'upper right',
        'c letter': 'upper right',
        'see bad': 'lower right',
        'sea bad': 'lower right',
        'c bad': 'lower right'
    }

    step_two_word_mapping = {
        'ready':               ['yes', 'okay', 'what', 'middle', 'left', 'press', 'right', 'blank', 'ready', 'no', 'first', 'uhhh', 'nothing', 'wait'],
        'first':               ['left', 'okay', 'yes', 'middle', 'no', 'right', 'nothing', 'uhhh', 'wait', 'ready', 'blank', 'what', 'press', 'first'],
        'no':                  ['blank', 'uhhh', 'wait', 'first', 'what', 'ready', 'right', 'yes', 'nothing', 'left', 'press', 'okay', 'no', 'middle'],
        'blank':               ['wait', 'right', 'okay', 'middle', 'blank', 'press', 'ready', 'nothing', 'no', 'what', 'left', 'uhhh', 'yes', 'first'],
        'nothing':             ['uhhh', 'right', 'okay', 'middle', 'yes', 'blank', 'no', 'press', 'left', 'what', 'wait', 'first', 'nothing', 'ready'],
        'yes':                 ['okay', 'right', 'uhhh', 'middle', 'first', 'what', 'press', 'ready', 'nothing', 'yes', 'left', 'blank', 'no', 'wait'],
        'what':                ['uhhh', 'what', 'left', 'nothing', 'ready', 'blank', 'middle', 'no', 'okay', 'first', 'wait', 'yes', 'press', 'right'],
        'triple h':            ['ready', 'nothing', 'left', 'what', 'okay', 'yes', 'right', 'no', 'press', 'blank', 'uhhh', 'middle', 'wait', 'first'],
        'left':                ['right', 'left', 'first', 'no', 'middle', 'yes', 'blank', 'what', 'uhhh', 'wait', 'press', 'ready', 'okay', 'nothing'],
        'right':               ['yes', 'nothing', 'ready', 'press', 'no', 'wait', 'what', 'right', 'middle', 'left', 'uhhh', 'blank', 'okay', 'first'],
        'middle':              ['blank', 'ready', 'okay', 'what', 'nothing', 'press', 'no', 'wait', 'left', 'middle', 'right', 'first', 'uhhh', 'yes'],
        'okay':                ['middle', 'no', 'first', 'yes', 'uhhh', 'nothing', 'wait', 'okay', 'left', 'ready', 'blank', 'press', 'what', 'right'],
        'wait':                ['uhhh', 'no', 'blank', 'okay', 'yes', 'left', 'first', 'press', 'what', 'wait', 'nothing', 'ready', 'right', 'middle'],
        'press':               ['right', 'middle', 'yes', 'ready', 'press', 'okay', 'nothing', 'uhhh', 'blank', 'left', 'first', 'what', 'no', 'wait'],
        'you':                 ['sure', 'you are', 'your', 'you\'re', 'next', 'uh huh', 'ur', 'hold', 'what?', 'you', 'uh uh', 'like', 'done', 'u'],
        'you are':             ['your', 'next', 'like', 'uh huh', 'what?', 'done', 'uh uh', 'hold', 'you', 'u', 'you\'re', 'sure', 'ur', 'you are'],
        'your possessive':     ['uh uh', 'you are', 'uh huh', 'your', 'next', 'ur', 'sure', 'u', 'you\'re', 'you', 'what?', 'hold', 'like', 'done'],
        'you are contraction': ['you', 'you\'re', 'ur', 'next', 'uh uh', 'you are', 'u', 'your', 'what?', 'uh huh', 'sure', 'done', 'like', 'hold'],
        'you are letters':     ['done', 'u', 'ur', 'uh huh', 'what?', 'sure', 'your', 'hold', 'you\'re', 'like', 'next', 'uh uh', 'you are', 'you'],
        'letter u':            ['uh huh', 'sure', 'next', 'what?', 'you\'re', 'ur', 'uh uh', 'done', 'u', 'you', 'like', 'hold', 'you are', 'your'],
        'casual yes':          ['uh huh', 'your', 'you are', 'you', 'done', 'hold', 'uh uh', 'next', 'sure', 'like', 'you\'re', 'ur', 'u', 'what?'],
        'casual no':           ['ur', 'u', 'you are', 'you\'re', 'next', 'uh uh', 'done', 'you', 'uh huh', 'like', 'your', 'sure', 'hold', 'what?'],
        'what question':       ['you', 'hold', 'you\'re', 'your', 'u', 'done', 'uh uh', 'like', 'you are', 'uh huh', 'ur', 'next', 'what?', 'sure'],
        'done':                ['sure', 'uh huh', 'next', 'what?', 'your', 'ur', 'you\'re', 'hold', 'like', 'you', 'u', 'you are', 'uh uh', 'done'],
        'next':                ['what?', 'uh huh', 'uh uh', 'your', 'hold', 'sure', 'next', 'like', 'done', 'you are', 'ur', 'you\'re', 'u', 'you'],
        'hold':                ['you are', 'u', 'done', 'uh uh', 'you', 'ur', 'sure', 'what?', 'you\'re', 'next', 'hold', 'uh huh', 'your', 'like'],
        'sure':                ['you are', 'done', 'like', 'you\'re', 'you', 'hold', 'uh huh', 'ur', 'sure', 'u', 'what?', 'next', 'your', 'uh uh'],
        'like':                ['you\'re', 'next', 'u', 'ur', 'hold', 'done', 'uh uh', 'what?', 'uh huh', 'you', 'like', 'sure', 'you are', 'your'],
    }

    def __init__(self, parameters: str) -> None:
        self.parameters = parameters
        self.parse_parameters()
        print(self.solve())

    def parse_parameters(self) -> None:
        if 'one' in self.parameters:
            step = 1
            offset = self.parameters.find('one') + 4
        elif '1' in self.parameters:
            step = 1
            offset = self.parameters.find('1') + 2
        elif 'two' in self.parameters:
            step = 2
            offset = self.parameters.find('two') + 4
        elif '2' in self.parameters:
            step = 2
            offset = self.parameters.find('2') + 2
        else:
            print('No stage information given! Please give the current stage with Who\'s on First commands. To use the Who\'s on First module, say "[step] one|two <word>".')
            return

        self.parsed_parameters = {
            'step': step,
            'words': self.parameters[offset:]
        }

    def solve(self) -> str:
        if ((self.parsed_parameters['step'] == 1) and (self.parsed_parameters['words'] in self.step_one_word_mapping)):
                return self.step_one_word_mapping[self.parsed_parameters['words']]
        elif ((self.parsed_parameters['step'] == 2) and (self.parsed_parameters['words'] in self.step_two_word_mapping)):
            return ', '.join(self.step_two_word_mapping[self.parsed_parameters['words']])
        else:
            print('Invalid configuration!')
            return ''
