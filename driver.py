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
                        self.handle_response(response)

    def handle_command(self, recognized_speech: str) -> str:
        command = recognized_speech['command']
        parameters = recognized_speech['parameters']
        print(f'Command: {command}. Parameters: {parameters}')

        if ((command == 'set serial') or (command == 'set cereal')):
            self.bomb.set_serial(parameters)
        elif command == 'set batteries':
            self.bomb.set_batteries(parameters)
        elif command == 'set indicators':
            self.bomb.set_indicators(parameters)
        elif ((command == 'set ports') or (command == 'set portes')):
            self.bomb.set_ports(parameters)
        elif command == 'set strikes':
            self.bomb.set_strikes()
        elif command == 'module wires':
            wires = Wires(parameters)
            solution = wires.solve()
            print(solution)
        elif command == 'module button':
            button = Button(parameters)
            solution = button.solve()
            print(solution)
        elif command == 'module keypad':
            keypad = Keypad(parameters)
            solution = keypad.solve()
            print(solution)
        elif command == 'module simon':
            simon_says = SimonSays(parameters)
            solution = simon_says.solve()
            print(solution)
        elif command == 'module who\'s on first':
            whos_on_first = WhosOnFirst(parameters)
            solution = whos_on_first.solve()
            print(solution)
        elif command == 'module complicated wires':
            complicated_wires = ComplicatedWires(parameters)
            solution = complicated_wires.solve()
            print(solution)
        elif command == 'print bomb':
            self.bomb.print()
        else:
            print(f'Unrecognized command: {recognized_speech["command"]}')

        return ''

    def handle_response(self, response: str) -> None:
        print(response)

    def _clean_name(self, name: str) -> str:
        clean_name = name.replace('set ', '')
        clean_name = clean_name.replace('module ', '')
        clean_name = clean_name.replace('\'', '')
        clean_name = ''.join(clean_name.split())

        return clean_name

def main():
    game = Game()

if __name__ == "__main__":
    main()
