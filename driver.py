from enum import Enum

from modules.bomb import Bomb
from modules.button import Button
from modules.complicated_wires import ComplicatedWires
from modules.keypad import Keypad
from modules.knob import Knob
from modules.memory import Memory
from modules.simon_says import SimonSays
from modules.whos_on_first import WhosOnFirst
from modules.wires import Wires

import utilities

import queue
import speech_handler as sh
import _thread as thread

# TODO: more error checking/output on blank return, plus conditions?
# TODO: class handling / inheritance model
# TODO: static method naming
# TODO: Reset bomb
# TODO: Reset module
# TODO: class design
# TODO: remove modules when done?
# TODO: comments (periods)
# TODO: common speech mapping in speech_handler?

class Game:
    def __init__(self) -> None:
        self.speech_queue = queue.Queue()
        self.speech_handler = sh.SpeechHandler(self.speech_queue)

        self.bomb = Bomb()
        self.bomb_mode = BombMode.Free
        self.current_module = None

        self.bomb.current_wires_module = None
        self.bomb.current_button_module = None
        self.bomb.current_keypad_module = None
        self.bomb.current_simon_says_module = None
        self.bomb.current_whos_on_first_module = None
        self.bomb.current_complicated_wires_module = None
        self.bomb.current_memory_module = None

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

    def handle_speech(self, recognized_speech: str) -> bool:
        print(f'HANDLE Recognized speech: {recognized_speech}.')

        if recognized_speech == 'exit':
            return False
        elif ((recognized_speech == 'done') or (recognized_speech == 'finish')):
            self.bomb_mode = BombMode.Free
        elif recognized_speech == 'strike':
            self.bomb.increment_strikes()
        elif recognized_speech == 'print bomb':
            self.bomb.print()
        elif recognized_speech == 'initialize':
            self.bomb_mode = BombMode.Initialize
        elif recognized_speech == 'module wires':
            self.bomb_mode = BombMode.Module
            self.current_module = Module.Wires
        elif recognized_speech == 'module button':
            self.bomb_mode = BombMode.Module
            self.current_module = Module.Button
        elif recognized_speech == 'module keypad':
            self.bomb_mode = BombMode.Module
            self.current_module = Module.Keypad
        elif recognized_speech == 'module simon':
            self.bomb_mode = BombMode.Module
            self.current_module = Module.SimonSays
        elif recognized_speech == 'module who\'s on first':
            self.bomb_mode = BombMode.Module
            self.current_module = Module.WhosOnFirst
        elif recognized_speech == 'module complicated wires':
            self.bomb_mode = BombMode.Module
            self.current_module = Module.ComplicatedWires
        elif recognized_speech == 'module memory':
            self.bomb_mode = BombMode.Module
            self.current_module = Module.Memory
        elif self.bomb_mode != BombMode.Free:
            return self.handle_mode(recognized_speech)
        else:
            print(f'Unrecognized command: {recognized_speech}')

        return ''

    def handle_response(self, response: str) -> None:
        print(response)

    def handle_mode(self, recognized_speech: str) -> str:
        if self.bomb_mode == BombMode.Initialize:
            return self.initialize_mode(recognized_speech)
        elif self.bomb_mode == BombMode.Module:
            return self.module_mode(recognized_speech)
        else:
            print(f'Unrecognized command: {recognized_speech}')
            return ''

    def initialize_mode(self, recognized_speech: str) -> str:
        if (('serial' in recognized_speech) or ('cereal' in recognized_speech)):
            self.bomb.set_serial(recognized_speech)
        elif 'batteries' in recognized_speech:
            self.bomb.set_batteries(recognized_speech)
        elif (('ports' in recognized_speech) or ('portes' in recognized_speech)):
            self.bomb.set_ports(recognized_speech)
        elif 'indicators' in recognized_speech:
            self.bomb.set_indicators(recognized_speech)

        return ''

    def module_mode(self, recognized_speech: str) -> str:
        if self.current_module == Module.Wires:
            current_module = self.bomb.current_wires_module
            stored_modules = self.bomb.wire_modules
            new_module = Wires
        if self.current_module == Module.Button:
            current_module = self.bomb.current_button_module
            stored_modules = self.bomb.button_modules
            new_module = Button
        if self.current_module == Module.Keypad:
            current_module = self.bomb.current_keypad_module
            stored_modules = self.bomb.keypad_modules
            new_module = Keypad
        if self.current_module == Module.SimonSays:
            current_module = self.bomb.current_simon_says_module
            stored_modules = self.bomb.simon_says_modules
            new_module = SimonSays
        if self.current_module == Module.WhosOnFirst:
            current_module = self.bomb.current_whos_on_first_module
            stored_modules = self.bomb.whos_on_first_modules
            new_module = WhosOnFirst
        if self.current_module == Module.ComplicatedWires:
            current_module = self.bomb.current_complicated_wires_module
            stored_modules = self.bomb.complicated_wires_modules
            new_module = ComplicatedWires
        if self.current_module == Module.Memory:
            current_module = self.bomb.current_memory_module
            stored_modules = self.bomb.memory_modules
            new_module = Memory

        if not current_module:
            current_module = new_module()
            stored_modules.append(current_module)
            self.bomb.current_memory_module = current_module
        elif recognized_speech.startswith('index'):
            module_index = self._get_module_index(recognized_speech)
            current_module = stored_modules[module_index]

        return current_module.solve_next_step(recognized_speech)

    def _get_module_index(self, recognized_speech: str) -> int:
        words = recognized_speech.split()
        for i in range(len(words)):
            if words[i] == 'index' and ((i + 1) < len(words)):
                return utilities.string_to_number(words[i + 1])

        print('No index recognized! Defaulting to 1...')
        return 1

class BombMode(Enum):
    Free = 0
    Initialize = 1
    Module = 2

class Module(Enum):
    Wires = 0
    Button = 1
    Keypad = 2
    SimonSays = 3
    WhosOnFirst = 4
    ComplicatedWires = 5
    Memory = 6

def main():
    game = Game()

if __name__ == "__main__":
    main()
