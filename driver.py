from modules.bomb import Bomb
from modules.button import Button
from modules.complicated_wires import ComplicatedWires
from modules.keypad import Keypad
from modules.knob import Knob
from modules.simon_says import SimonSays
from modules.wires import Wires

import queue
import speech_handler as sh
import _thread as thread

# TODO: more error checking/output on blank return, plus conditions?

class Game:
    def __init__(self) -> None:
        self.command_queue = queue.Queue()
        self.speech_handler = sh.SpeechHandler(self.command_queue)
        self.bomb = Bomb()
        self.run()

    def run(self) -> None:
        queue_lock = thread.allocate_lock()

        while True:
            try:
                command = self.command_queue.get()
            except queue.Empty:
                pass
            else:
                with queue_lock:
                    response = self.handle_command(command)
                    if response == 'exit':
                        break
                    elif response != '':
                        handle_response(response)

    def handle_command(self, recognized_speech: str) -> str:
        print('Command: {recognized_speech["command"]}. Parameters: {recognized_speech["parameters"]}')

        if recognized_speech['command'] == 'exit':
            return 'exit'
        elif recognized_speech['command'].startswith('set'):
            method_name = '_'.join(recognized_speech['command'].split())
            getattr(self.bomb, method_name)(recognized_speech['parameters'])
        elif recognized_speech['command'].startswith('module'):
            module_name = ''.join(recognized_speech['command'].split())
            module = getattr(self.bomb, module_name)(recognized_speech['parameters'])
            solution = module.solve()
            return solution
        elif recognized_speech['command'] == 'print bomb':
            self.bomb.print()
        else:
            print(f'Unrecognized command: {recognized_speech["command"]}')

        return ''

    def handle_response(self, response: str) -> None:
        print(response)

def main():
    game = Game()

if __name__ == "__main__":
    main()
