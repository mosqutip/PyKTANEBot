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
        self.current_module_type = None

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
        elif recognized_speech == 'finish':
            self.bomb_mode = BombMode.Free
        elif recognized_speech == 'add strike':
            self.bomb.increment_strikes()
        elif recognized_speech == 'print bomb':
            self.bomb.print()
        elif recognized_speech == 'initialize':
            self.bomb_mode = BombMode.InitializeBomb
        elif recognized_speech == 'module wires':
            self.bomb_mode = BombMode.StartModule
            self.current_module_type = Module.Wires
        elif recognized_speech == 'module button':
            self.bomb_mode = BombMode.StartModule
            self.current_module_type = Module.Button
        elif recognized_speech == 'module keypad':
            self.bomb_mode = BombMode.StartModule
            self.current_module_type = Module.Keypad
        elif recognized_speech == 'module simon':
            self.bomb_mode = BombMode.StartModule
            self.current_module_type = Module.SimonSays
        elif recognized_speech == 'module who\'s on first':
            self.bomb_mode = BombMode.StartModule
            self.current_module_type = Module.WhosOnFirst
        elif recognized_speech == 'module complicated wires':
            self.bomb_mode = BombMode.StartModule
            self.current_module_type = Module.ComplicatedWires
        elif recognized_speech == 'module memory':
            self.bomb_mode = BombMode.StartModule
            self.current_module_type = Module.Memory

        if self.bomb_mode != BombMode.Free:
            return self.handle_mode(recognized_speech)

        return ''

    def handle_response(self, response: str) -> None:
        print(response)

    def handle_mode(self, recognized_speech: str) -> str:
        if self.bomb_mode == BombMode.InitializeBomb:
            return self.initialize_bomb_mode(recognized_speech)
        elif self.bomb_mode == BombMode.StartModule:
            return self.start_module_mode(recognized_speech)
        elif self.bomb_mode == BombMode.SolvingModule:
            return self.solve_module_mode(recognized_speech)
        else:
            print(f'Unrecognized command: {recognized_speech}')
            return ''

    def initialize_bomb_mode(self, recognized_speech: str) -> str:
        if (('serial' in recognized_speech) or ('cereal' in recognized_speech)):
            self.bomb.set_serial(recognized_speech)
        elif 'batteries' in recognized_speech:
            self.bomb.set_batteries(recognized_speech)
        elif (('jack' in recognized_speech) or ('jax' in recognized_speech) or ('jack\'s' in recognized_speech) or ('jacks' in recognized_speech)):
            self.bomb.set_ports(recognized_speech)
        elif 'indicators' in recognized_speech:
            self.bomb.set_indicators(recognized_speech)

        return ''

    def start_module_mode(self, recognized_speech: str) -> str:
        if self.current_module_type == Module.Wires:
            stored_modules = self.bomb.wire_modules
            new_module = Wires
        elif self.current_module_type == Module.Button:
            stored_modules = self.bomb.button_modules
            new_module = Button
        elif self.current_module_type == Module.Keypad:
            stored_modules = self.bomb.keypad_modules
            new_module = Keypad
        elif self.current_module_type == Module.SimonSays:
            stored_modules = self.bomb.simon_says_modules
            new_module = SimonSays
        elif self.current_module_type == Module.WhosOnFirst:
            stored_modules = self.bomb.whos_on_first_modules
            new_module = WhosOnFirst
        elif self.current_module_type == Module.ComplicatedWires:
            stored_modules = self.bomb.complicated_wires_modules
            new_module = ComplicatedWires
        elif self.current_module_type == Module.Memory:
            stored_modules = self.bomb.memory_modules
            new_module = Memory

        if recognized_speech.startswith('index'):
            module_index = self._get_module_index(recognized_speech)
            self.current_module = stored_modules[module_index]
        else:
            self.current_module = new_module()
            stored_modules.append(self.current_module)

        self.bomb_mode = BombMode.SolvingModule
        return ''

    def solve_module_mode(self, recognized_speech: str) -> str:
        return self.current_module.solve_next_step(recognized_speech)

    def _get_module_index(self, recognized_speech: str) -> int:
        words = recognized_speech.split()
        for i in range(len(words)):
            if words[i] == 'index' and ((i + 1) < len(words)):
                return utilities.string_to_number(words[i + 1])

        print('No index recognized! Defaulting to 1...')
        return 1

class BombMode(Enum):
    Free = 0
    InitializeBomb = 1
    StartModule = 2
    SolvingModule = 3

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
