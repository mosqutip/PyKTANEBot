from modules.bomb import Bomb
from modules.button import Button
from modules.keypad import Keypad
from modules.simon import Simon
from modules.wires import Wires

import queue
import speech_handler as sh
import _thread as thread

class Game:
    def __init__(self) -> None:
        self.command_queue = queue.Queue()
        self.speech_handler = sh.SpeechHandler(self.command_queue)
        self.bomb = Bomb()
        self.run()

    def run(self) -> None:
        queue_lock = thread.allocate_lock()
        command = ''

        while command != 'exit':
            try:
                command = self.command_queue.get()
            except queue.Empty:
                pass
            else:
                with queue_lock:
                    command = self.handle_command(command)

    def handle_command(self, recognized_speech: str) -> str:
        print(recognized_speech['command'])
        print(recognized_speech['parameters'])

        if recognized_speech['command'] == 'exit':
            return 'exit'
        elif ((recognized_speech['command'] == 'set serial') or (recognized_speech['command'] == 'set cereal')):
            self.bomb.set_serial(recognized_speech['parameters'])
        elif recognized_speech['command'] == 'set batteries':
            self.bomb.set_batteries(recognized_speech['parameters'])
        elif recognized_speech['command'] == 'set indicators':
            self.bomb.set_indicators(recognized_speech['parameters'])
        elif recognized_speech['command'] == 'print bomb':
            self.bomb.print()
        elif recognized_speech['command'] == 'strike':
            self.bomb.increment_strikes()
        elif recognized_speech['command'] == 'module wires':
            wires = Wires(recognized_speech['parameters'])
            solution = wires.solve()
            print(solution)
        elif recognized_speech['command'] == 'module button':
            button = Button(recognized_speech['parameters'])
            solution = button.solve()
            print(solution)
        elif recognized_speech['command'] == 'module keypad':
            keypad = Keypad(recognized_speech['parameters'])
            solution = keypad.solve()
            print(solution)
        elif recognized_speech['command'] == 'module simon':
            simon = Simon(recognized_speech['parameters'])
            solution = simon.solve()
            print(solution)
        else:
            print(f'Unrecognized command: {recognized_speech["command"]}')
        return ''

def main():
    game = Game()

if __name__ == "__main__":
    main()
