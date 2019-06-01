'''
On the Subject of Memory

• Press the correct button to progress the module to the next stage. Complete all stages to disarm the module.
• Pressing an incorrect button will reset the module back to stage 1.
• Button positions are ordered from left to right.

Stage 1:
    If the display is 1, press the button in the second position.
    If the display is 2, press the button in the second position.
    If the display is 3, press the button in the third position.
    If the display is 4, press the button in the fourth position.
Stage 2:
    If the display is 1, press the button labeled "4".
    If the display is 2, press the button in the same position as you pressed in stage 1.
    If the display is 3, press the button in the first position.
    If the display is 4, press the button in the same position as you pressed in stage 1.
Stage 3:
    If the display is 1, press the button with the same label you pressed in stage 2.
    If the display is 2, press the button with the same label you pressed in stage 1.
    If the display is 3, press the button in the third position.
    If the display is 4, press the button labeled "4".
Stage 4:
    If the display is 1, press the button in the same position as you pressed in stage 1.
    If the display is 2, press the button in the first position.
    If the display is 3, press the button in the same position as you pressed in stage 2.
    If the display is 4, press the button in the same position as you pressed in stage 2.
Stage 5:
    If the display is 1, press the button with the same label you pressed in stage 1.
    If the display is 2, press the button with the same label you pressed in stage 2.
    If the display is 3, press the button with the same label you pressed in stage 4.
    If the display is 4, press the button with the same label you pressed in stage 3.
'''

import modules.bomb
import utilities

# TODO: handle missing a 'finishing' step (no position or label filled in for stage)

class Memory:
    def __init__(self):
        self.stage = 1
        self.press_history = [
            {},
            { 'position': '', 'label': '' },
            { 'position': '', 'label': '' },
            { 'position': '', 'label': '' },
            { 'position': '', 'label': '' }
        ]

    def try_parse_speech(self, recognized_speech: str) -> bool:
        words = recognized_speech.split()

        if words[0] == 'stage':
            self.stage = utilities.string_to_number(words[1])
            self.parsed_speech = ''
            print(f'Resetting memory module to stage {words[1]}')
            return True
        elif (('pressing' in words) and len(words) == 3):
            if 'position' in words:
                self.press_history[self.stage]['position'] = utilities.string_to_number(words[2])
            elif 'pressing' in words:
                self.press_history[self.stage]['label'] = utilities.string_to_number(words[2])
            else:
                print('Invalid memory command!')
                return False

            self.parsed_speech = ''
            self.stage += 1
            return True
        elif words[0] == 'display':
            self.parsed_speech = utilities.string_to_number(words[1])
            return True
        else:
            self.parsed_speech = ''
            return False

    def solve_next_step(self, recognized_speech: str) -> str:
        if not self.try_parse_speech(recognized_speech):
            print('Could not parse speech!')
            return ''

        if self.parsed_speech != '':
            if self.stage == 1:
                return self.solve_stage_one()
            elif self.stage == 2:
                return self.solve_stage_two()
            elif self.stage == 3:
                return self.solve_stage_three()
            elif self.stage == 4:
                return self.solve_stage_four()
            elif self.stage == 5:
                return self.solve_stage_five()

    def solve_stage_one(self) -> str:
        if ((self.parsed_speech == 1) or (self.parsed_speech == 2)):
            self.press_history[1]['position'] = 2
            return 'Press the button in the second position'
        elif self.parsed_speech == 3:
            self.press_history[1]['position'] = 3
            return 'Press the button in the third position'
        elif self.parsed_speech == 4:
            self.press_history[1]['position'] = 4
            return 'Press the button in the fourth position'
        else:
            return 'Invalid display value!'

    def solve_stage_two(self) -> str:
        if self.parsed_speech == 1:
            self.press_history[2]['label'] = 4
            return 'Press the button labelled 4.'
        elif ((self.parsed_speech == 2) or (self.parsed_speech == 4)):
            self.press_history[2]['position'] = self.press_history[1]['position']
            return f'Press the button in the same position (position {self.press_history[1]["position"]}) as the button you pressed in stage one.'
        elif self.parsed_speech == 3:
            self.press_history[2]['position'] = 1
            return 'Press the button in the first position'
        else:
            return 'Invalid display value!'

    def solve_stage_three(self) -> str:
        if self.parsed_speech == 1:
            self.press_history[3]['position'] = self.press_history[2]['position']
            return f'Press the button in the same position (position {self.press_history[1]["position"]}) as the button you pressed in stage two.'
        elif self.parsed_speech == 2:
            self.press_history[3]['position'] = self.press_history[1]['position']
            return f'Press the button in the same position (position {self.press_history[0]["position"]}) as the button you pressed in stage one.'
        elif self.parsed_speech == 3:
            self.press_history[3]['position'] = 3
            return 'Press the button in the third position'
        elif self.parsed_speech == 4:
            self.press_history[3]['label'] = 4
            return 'Press the button labelled 4.'
        else:
            return 'Invalid display value!'

    def solve_stage_four(self) -> str:
        if self.parsed_speech == 1:
            self.press_history[4]['position'] = self.press_history[1]['position']
            return f'Press the button in the same position (position {self.press_history[1]["position"]}) as the button you pressed in stage one.'
        elif self.parsed_speech == 2:
            self.press_history[4]['position'] = 1
            return 'Press the button in the first position'
        elif ((self.parsed_speech == 3) or (self.parsed_speech == 4)):
            self.press_history[4]['position'] = self.press_history[2]['position']
            return f'Press the button in the same position (position {self.press_history[2]["position"]}) as the button you pressed in stage two.'
        else:
            return 'Invalid display value!'

    def solve_stage_five(self) -> str:
        if self.parsed_speech == 1:
            return f'Press the button with the same label (label {self.press_history[1]["label"]}) as the button you pressed in stage one.'
        elif self.parsed_speech == 2:
            return f'Press the button with the same label (label {self.press_history[2]["label"]}) as the button you pressed in stage two.'
        elif self.parsed_speech == 3:
            return f'Press the button with the same label (label {self.press_history[4]["label"]}) as the button you pressed in stage four.'
        elif self.parsed_speech == 4:
            return f'Press the button with the same label (label {self.press_history[3]["label"]}) as the button you pressed in stage three.'
        else:
            return 'Invalid display value!'
