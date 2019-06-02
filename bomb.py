from enum import Enum

from utilities import parse_nato_to_serial, parse_string_to_number

import config

class Bomb:
    wire_modules = []
    button_modules = []
    keypad_modules = []
    simon_says_modules = []
    whos_on_first_modules = []
    memory_modules = []
    morse_code_modules = []
    complicated_wires_modules = []
    wire_sequence_modules = []
    maze_modules = []
    password_modules = []
    knob_modules = []

    def __init__(self) -> None:
        self.bomb_mode = BombMode.Free
        self.current_module_type = None

    def set_serial(self, audio_data: str) -> None:
        raw_serial = audio_data.split()[2:]
        serial = parse_nato_to_serial(raw_serial)
        if ((len(serial) != 6) or '?' in serial):
            return

        config.does_serial_contain_vowel = False
        for character in serial[:-1]:
            if character in ['aeiou']:
                config.does_serial_contain_vowel = True
                break

        if serial[-1] % 2 == 1:
            config.is_last_digit_of_serial_odd = True
        else:
            config.is_last_digit_of_serial_odd = False

    def set_batteries(self, audio_data: str) -> None:
        # Get last word of command, which should be the number of batteries.
        batteries = audio_data.split()[-1]
        config.num_batteries = parse_string_to_number(batteries)

    def set_indicators(self, audio_data: str) -> None:
        config.indicators = []
        for word in audio_data.split()[2:]:
            config.indicators.append(word)

    def set_ports(self, audio_data: str) -> None:
        config.ports = []
        for word in audio_data.split()[2:]:
            config.ports.append(word)

    def increment_strikes(self) -> None:
        config.strikes += 1

    def reset_bomb(self) -> None:
        config.is_last_digit_of_serial_odd = None
        config.does_serial_contain_vowel = None
        config.num_batteries = None
        config.indicators = None
        config.ports = None
        config.strikes = 0

        self.bomb_mode = BombMode.Free
        self.current_module_type = None

        self.wire_modules = []
        self.button_modules = []
        self.keypad_modules = []
        self.simon_says_modules = []
        self.whos_on_first_modules = []
        self.memory_modules = []
        self.morse_code_modules = []
        self.complicated_wires_modules = []
        self.wire_sequence_modules = []
        self.maze_modules = []
        self.password_modules = []
        self.knob_modules = []

    def print(self) -> None:
        indicator_string = '' if not config.indicators else ', '.join(config.indicators)
        port_string = '' if not config.ports else ', '.join(config.ports)

        print('***** Bomb Data *****')
        print(f'Last digit of serial is odd: {config.is_last_digit_of_serial_odd}')
        print(f'Serial contains vowel: {config.does_serial_contain_vowel}')
        print(f'Batteries: {config.num_batteries}')
        print(f'Indicators: {indicator_string}')
        print(f'Ports: {port_string}')
        print(f'Strikes: {config.strikes}')
        print('***** Bomb Data *****')

class BombMode(Enum):
    Free =       'No active processing. Parallel to RecognitionMode.Keyword.'
    Initialize = 'Bomb initialization mode for setting the serial, batteries, etc.'
    Module =     'Module mode for initializing and solving the active module.'

class ModuleType(Enum):
    Wires =            'Wires module.'
    Button =           'Button module.'
    Keypad =           'Keypad module.'
    SimonSays =        'Simon Says module.'
    WhosOnFirst =      'Who\'s on First module.'
    Memory =           'Memory module.'
    MorseCode =        'Morse code module.'
    ComplicatedWires = 'Complicated wires module.'
    WireSequence =     'Wire sequence module.'
    Maze =             'Maze module.'
    Password =         'Password module.'
    Knob =             'Knob module.'
