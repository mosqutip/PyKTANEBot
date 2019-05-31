from enum import Enum

from modules.bomb import Bomb
from modules.button import Button
from modules.complicated_wires import ComplicatedWires
from modules.keypad import Keypad
from modules.knob import Knob
from modules.simon_says import SimonSays
from modules.whos_on_first import WhosOnFirst
from modules.wires import Wires

import queue
import speech_handler as sh
import _thread as thread

# TODO: more error checking/output on blank return, plus conditions?
# TODO: class handling / inheritance model
# TODO: static method naming
# TODO: Reset bomb
# TODO: Reset module
# TODO: class design
# TODO: NATO->serial

class Game:
    def __init__(self) -> None:
        self.speech_queue = queue.Queue()
        self.speech_handler = sh.SpeechHandler(self.speech_queue)

        self.bomb = Bomb()
        self.bomb_mode = BombMode.Free

        self.bomb.current_wires_module = None
        self.bomb.current_button_module = None
        self.bomb.current_keypad_module = None
        self.bomb.current_simon_says_module = None
        self.bomb.current_whos_on_first_module = None
        self.bomb.current_complicated_wires_module = None

        self.run()

    def run(self) -> None:
        queue_lock = thread.allocate_lock()

        while True:
            try:
                recognized_speech = self.speech_queue.get()
            except queue.Empty:
                pass
            else:
                with queue_lock:
                    response = self.handle_speech(recognized_speech)
                    if response == 'exit':
                        break
                    elif response != '':
                        self.handle_response(response)

    def handle_speech(self, recognized_speech: str) -> str:
        print(f'HANDLE Recognized speech: {recognized_speech}.')

        if recognized_speech == 'exit':
            return 'exit'
        elif ((recognized_speech == 'done') or (recognized_speech == 'finish')):
            self.bomb_mode = BombMode.Free
        elif recognized_speech == 'initialize':
            self.bomb_mode = BombMode.Initialize
        elif recognized_speech == 'module wires':
            self.bomb_mode = BombMode.Wires
        elif recognized_speech == 'module button':
            self.bomb_mode = BombMode.Button
        elif recognized_speech == 'module keypad':
            self.bomb_mode = BombMode.Keypad
        elif recognized_speech == 'module simon':
            self.bomb_mode = BombMode.Simon_Says
        elif recognized_speech == 'module who\'s on first':
            self.bomb_mode = BombMode.Whos_On_First
        elif recognized_speech == 'module complicated wires':
            self.bomb_mode = BombMode.Complicated_Wires
        elif recognized_speech == 'strike':
            self.bomb.increment_strikes()
        elif recognized_speech == 'print bomb':
            self.bomb.print()
        else:
            if self.bomb_mode == BombMode.Initialize:
                return self.initialize_mode(recognized_speech)
            elif self.bomb_mode == BombMode.Wires:
                return self.wires_mode(recognized_speech)
            elif self.bomb_mode == BombMode.Button:
                return self.button_mode(recognized_speech)
            elif self.bomb_mode == BombMode.Keypad:
                return self.keypad_mode(recognized_speech)
            elif self.bomb_mode == BombMode.Simon_Says:
                return self.simon_says_mode(recognized_speech)
            elif self.bomb_mode == BombMode.Whos_On_First:
                return self.whos_on_first_mode(recognized_speech)
            elif self.bomb_mode == BombMode.Complicated_Wires:
                return self.complicated_wires_mode(recognized_speech)
            else:
                print(f'Unrecognized command: {recognized_speech["command"]}')

        return ''

    def handle_response(self, response: str) -> None:
        print(response)

    def initialize_mode(self, recognized_speech: str) -> None:
        if (('serial' in recognized_speech) or ('cereal' in recognized_speech)):
            self.bomb.set_serial(recognized_speech)
        elif 'batteries' in recognized_speech:
            self.bomb.set_batteries(recognized_speech)
        elif (('ports' in recognized_speech) or ('portes' in recognized_speech)):
            self.bomb.set_ports(recognized_speech)
        elif 'indicators' in recognized_speech:
            self.bomb.set_indicators(recognized_speech)

        return

    def wires_mode(self, recognized_speech: str) -> str:
        if (recognized_speech.startswith('resume') or recognized_speech.startswith('continue')):
            print('Continuing on last accessed wires module.')
        elif recognized_speech.startswith('index'):
            module_index = self._get_module_index(recognized_speech)
            self.bomb.current_wires_module = self.bomb.wire_modules[module_index]
        else:
            self.bomb.current_wires_module = Wires()
            self.bomb.wire_modules.append(self.bomb.current_wires_module)

        return self.bomb.current_wires_module.solve_next_step(recognized_speech)

    def button_mode(self, recognized_speech: str) -> str:
        if (recognized_speech.startswith('start') or recognized_speech.startswith('new')):
            self.bomb.current_wires_module = Wires()
            self.bomb.wire_modules.append(self.bomb.current_wires_module)
        elif recognized_speech.startswith('index'):
            module_index = self._get_module_index(recognized_speech)
            self.bomb.current_wires_module = self.bomb.wire_modules[module_index]

        return self.bomb.current_wires_module.solve_next_step(recognized_speech)

    def keypad_mode(self, recognized_speech: str) -> str:
        if (recognized_speech.startswith('start') or recognized_speech.startswith('new')):
            self.bomb.current_wires_module = Wires()
            self.bomb.wire_modules.append(self.bomb.current_wires_module)
        elif recognized_speech.startswith('index'):
            module_index = self._get_module_index(recognized_speech)
            self.bomb.current_wires_module = self.bomb.wire_modules[module_index]

        return self.bomb.current_wires_module.solve_next_step(recognized_speech)

    def simon_says_mode(self, recognized_speech: str) -> str:
        if (recognized_speech.startswith('start') or recognized_speech.startswith('new')):
            self.bomb.current_wires_module = Wires()
            self.bomb.wire_modules.append(self.bomb.current_wires_module)
        elif recognized_speech.startswith('index'):
            module_index = self._get_module_index(recognized_speech)
            self.bomb.current_wires_module = self.bomb.wire_modules[module_index]

        return self.bomb.current_wires_module.solve_next_step(recognized_speech)

    def whos_on_first_mode(self, recognized_speech: str) -> str:
        if (recognized_speech.startswith('start') or recognized_speech.startswith('new')):
            self.bomb.current_wires_module = Wires()
            self.bomb.wire_modules.append(self.bomb.current_wires_module)
        elif recognized_speech.startswith('index'):
            module_index = self._get_module_index(recognized_speech)
            self.bomb.current_wires_module = self.bomb.wire_modules[module_index]

        return self.bomb.current_wires_module.solve_next_step(recognized_speech)

    def complicated_wires_mode(self, recognized_speech: str) -> str:
        if (recognized_speech.startswith('start') or recognized_speech.startswith('new')):
            self.bomb.current_wires_module = Wires()
            self.bomb.wire_modules.append(self.bomb.current_wires_module)
        elif recognized_speech.startswith('index'):
            module_index = self._get_module_index(recognized_speech)
            self.bomb.current_wires_module = self.bomb.wire_modules[module_index]

        return self.bomb.current_wires_module.solve_next_step(recognized_speech)

    def _get_module_index(self, recognized_speech: str) -> int:
        words = recognized_speech.split()
        for i in range(len(words)):
            if words[i] == 'index' and ((i + 1) < len(words)):
                return string_to_number(words[i + 1])

        print('No index recognized! Defaulting to 1...')
        return 1

class BombMode(Enum):
    Free = 0
    Initialize = 1
    Wires = 2
    Button = 3
    Keypad = 4
    Simon_Says = 5
    Whos_On_First = 6
    Complicated_Wires = 7

def string_to_number(index: str) -> int:
    if ((index == '0') or (index == 'zero') or (index == 'none')):
        return 0
    elif ((index == '1') or (index == 'one') or (index == 'won')):
        return 1
    elif ((index == '2') or (index == 'two') or (index == 'to') or (index == 'too')):
        return 2
    elif ((index == '3') or (index == 'three')):
        return 3
    elif ((index == '4') or (index == 'four') or (index == 'for') or (index == 'fore')):
        return 4
    elif ((index == '5') or (index == 'five')):
        return 5
    elif ((index == '6') or (index == 'six')):
        return 6
    elif ((index == '7') or (index == 'seven')):
        return 7
    elif ((index == '8') or (index == 'eight') or (index == 'ate')):
        return 8
    elif ((index == '9') or (index == 'nine')):
        return 9

def main():
    game = Game()

if __name__ == "__main__":
    main()
