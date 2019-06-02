from enum import Enum
from queue import Queue

from bomb import Bomb, BombMode, ModuleType
from modules.button import Button
from modules.complicated_wires import ComplicatedWires
from modules.keypad import Keypad
from modules.knob import Knob
from modules.maze import Maze
from modules.memory import Memory
from modules.morse_code import MorseCode
from modules.password import Password
from modules.simon_says import SimonSays
from modules.whos_on_first import WhosOnFirst
from modules.wire_sequence import WireSequence
from modules.wires import Wires
from utilities import parse_string_to_number

import queue
import speech_handler as sh
import _thread as thread

# TODO: Logger
    # TODO: More error checking/output on blank return, plus conditions?
# TODO: Class handling / inheritance model
# TODO: Reset module (or just restart?)
# TODO: Class design
# TODO: Add comments (check periods)
# TODO: Enum strings?

class Game:
    def __init__(self) -> None:
        self.speech_queue = Queue()
        self.speech_handler = sh.SpeechHandler(self.speech_queue)
        self.bomb = Bomb()
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
            # Remove the last used module from storage, as it is no longer needed.
            self.stored_modules.pop()
        elif recognized_speech == 'add strike':
            self.bomb.increment_strikes()
        elif recognized_speech == 'print bomb':
            self.bomb.print()
        elif recognized_speech == 'initialize':
            self.bomb_mode = BombMode.InitializeBomb
        elif recognized_speech == 'module wires':
            self.bomb_mode = BombMode.StartModule
            self.current_module_type = ModuleType.Wires
        elif recognized_speech == 'module button':
            self.bomb_mode = BombMode.StartModule
            self.current_module_type = ModuleType.Button
        elif recognized_speech == 'module keypad':
            self.bomb_mode = BombMode.StartModule
            self.current_module_type = ModuleType.Keypad
        elif recognized_speech == 'module simon':
            self.bomb_mode = BombMode.StartModule
            self.current_module_type = ModuleType.SimonSays
        elif recognized_speech == 'module who\'s on first':
            self.bomb_mode = BombMode.StartModule
            self.current_module_type = ModuleType.WhosOnFirst
        elif recognized_speech == 'module memory':
            self.bomb_mode = BombMode.StartModule
            self.current_module_type = ModuleType.Memory
        elif recognized_speech == 'module morse code':
            self.bomb_mode = BombMode.StartModule
            self.current_module_type = ModuleType.MorseCode
        elif recognized_speech == 'module complicated wires':
            self.bomb_mode = BombMode.StartModule
            self.current_module_type = ModuleType.ComplicatedWires
        elif recognized_speech == 'module wire sequence':
            self.bomb_mode = BombMode.StartModule
            self.current_module_type = ModuleType.WireSequence
        elif recognized_speech == 'module maze':
            self.bomb_mode = BombMode.StartModule
            self.current_module_type = ModuleType.Maze
        elif recognized_speech == 'module password':
            self.bomb_mode = BombMode.StartModule
            self.current_module_type = ModuleType.Password
        elif recognized_speech == 'module knob':
            self.bomb_mode = BombMode.StartModule
            self.current_module_type = ModuleType.Knob

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
        if self.current_module_type == ModuleType.Wires:
            self.stored_modules = self.bomb.wire_modules
            new_module = Wires
        elif self.current_module_type == ModuleType.Button:
            self.stored_modules = self.bomb.button_modules
            new_module = Button
        elif self.current_module_type == ModuleType.Keypad:
            self.stored_modules = self.bomb.keypad_modules
            new_module = Keypad
        elif self.current_module_type == ModuleType.SimonSays:
            self.stored_modules = self.bomb.simon_says_modules
            new_module = SimonSays
        elif self.current_module_type == ModuleType.WhosOnFirst:
            self.stored_modules = self.bomb.whos_on_first_modules
            new_module = WhosOnFirst
        elif self.current_module_type == ModuleType.Memory:
            self.stored_modules = self.bomb.memory_modules
            new_module = Memory
        elif self.current_module_type == ModuleType.MorseCode:
            self.stored_modules = self.bomb.morse_code_modules
            new_module = MorseCode
        elif self.current_module_type == ModuleType.ComplicatedWires:
            self.stored_modules = self.bomb.complicated_wires_modules
            new_module = ComplicatedWires
        elif self.current_module_type == ModuleType.WireSequence:
            self.stored_modules = self.bomb.wire_sequence_modules
            new_module = WireSequence
        elif self.current_module_type == ModuleType.Maze:
            self.stored_modules = self.bomb.maze_modules
            new_module = Maze
        elif self.current_module_type == ModuleType.Password:
            self.stored_modules = self.bomb.password_modules
            new_module = Password
        elif self.current_module_type == ModuleType.Knob:
            self.stored_modules = self.bomb.knob_modules
            new_module = Knob

        module_index = 0
        if recognized_speech.startswith('index'):
            module_index = self._get_module_index(recognized_speech)
        elif recognized_speech.startswith('resume'):
            module_index = -1

        # Guard against invalid index accesses.
        if ((len(self.stored_modules) == 0) or (module_index >= len(self.stored_modules)) or (('index' not in recognized_speech) and ('resume') not in recognized_speech)):
            self.current_module = new_module()
            self.stored_modules.append(self.current_module)

        self.bomb_mode = BombMode.SolvingModule
        return ''

    def solve_module_mode(self, recognized_speech: str) -> str:
        return self.current_module.solve_next_step(recognized_speech)

    def _get_module_index(self, recognized_speech: str) -> int:
        words = recognized_speech.split()
        for i in range(len(words)):
            if words[i] == 'index' and ((i + 1) < len(words)):
                return parse_string_to_number(words[i + 1])

        print('No index recognized! Defaulting to 1...')
        return 1

def main():
    Game()

if __name__ == "__main__":
    main()
