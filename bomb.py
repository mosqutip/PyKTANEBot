from enum import Enum

from utilities import parse_nato_to_serial, parse_string_to_number

is_last_digit_of_serial_odd = False
does_serial_contain_vowel = False

num_batteries = None
indicators = None
ports = None
strikes = 0

__all__ = [
    'is_last_digit_of_serial_odd',
    'does_serial_contain_vowel',
    'num_batteries',
    'indicators',
    'ports',
    'strikes'
]

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
        global is_last_digit_of_serial_odd
        global does_serial_contain_vowel

        serial = parse_nato_to_serial(audio_data)
        if ((len(serial) != 6) or '?' in serial):
            return

        does_serial_contain_vowel = False
        for character in serial[:-1]:
            if character in ['AEIOU']:
                does_serial_contain_vowel = True
                break

        if serial[-1] % 2 == 1:
            is_last_digit_of_serial_odd = True
        else:
            is_last_digit_of_serial_odd = False

    def set_batteries(self, audio_data: str) -> None:
        global num_batteries

        # Get last word of command, which should be the number of batteries.
        batteries = audio_data.split()[-1]
        num_batteries = parse_string_to_number(batteries)

    def set_indicators(self, audio_data: str) -> None:
        global indicators

        indicators = []
        for word in audio_data.split()[2:]:
            indicators.append(word)

    def set_ports(self, audio_data: str) -> None:
        global ports

        ports = []
        for word in audio_data.split()[2:]:
            ports.append(word)

    def increment_strikes(self) -> None:
        global strikes

        strikes += 1

    def reset_bomb(self) -> None:
        global is_last_digit_of_serial_odd
        global does_serial_contain_vowel
        global num_batteries
        global indicators
        global ports
        global strikes

        is_last_digit_of_serial_odd = None
        does_serial_contain_vowel = None
        num_batteries = None
        indicators = None
        ports = None
        strikes = 0

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
        global is_last_digit_of_serial_odd
        global does_serial_contain_vowel
        global num_batteries
        global indicators
        global ports
        global strikes

        indicator_string = ', '.join(indicators)
        port_string = ', '.join(ports)

        print('***** Bomb Data *****')
        print(f'Last digit of serial is odd: {is_last_digit_of_serial_odd}')
        print(f'Serial contains vowel: {does_serial_contain_vowel}')
        print(f'Batteries: {num_batteries}')
        print(f'Indicators: {indicator_string}')
        print(f'Ports: {port_string}')
        print(f'Strikes: {strikes}')
        print('***** Bomb Data *****')

class BombMode(Enum):
    Free =           'No active processing. Parallel to RecognitionMode.Keyword.'
    InitializeBomb = 'Bomb initialization mode for setting the serial, batteries, etc.'
    StartModule =    'Module initialization mode for setting up new or resuming modules.'
    SolvingModule =  'Module solving mode for solving the active module.'

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
