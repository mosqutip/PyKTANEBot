is_serial_set = False
is_num_batteries_set = False
is_indicators_set = False

is_last_digit_of_serial_odd = False
does_serial_contain_vowel = False
num_batteries = 0
indicators = []
strikes = 0

class Bomb:
    word_to_int_mapping = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'zero': 0,
        'one': 1,
        'to': 2,
        'too': 2,
        'two': 2,
        'three': 3,
        'for': 4,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'ate': 8,
        'eight': 8,
        'nine': 9
    }

    wire_modules = []
    button_modules = []
    keypad_modules = []

    def set_serial(self, audio_data: str) -> None:
        global is_last_digit_of_serial_odd
        global does_serial_contain_vowel
        global is_serial_set

        if 'even' in audio_data:
            is_last_digit_of_serial_odd = False
        elif 'odd' in audio_data:
            is_last_digit_of_serial_odd = True

        if 'vowel' in audio_data:
            does_serial_contain_vowel = True

        is_serial_set = True

    def set_batteries(self, audio_data: str) -> None:
        global num_batteries
        global is_num_batteries_set

        if audio_data in self.word_to_int_mapping:
            num_batteries = self.word_to_int_mapping[audio_data]
            is_num_batteries_set = True

    def set_indicators(self, audio_data: str) -> None:
        global indicators
        global is_indicators_set

        is_indicators_set = True
        for word in audio_data.split():
            indicators.append(word)

    def print(self) -> None:
        global num_batteries
        global indicators
        global is_last_digit_of_serial_odd
        global does_serial_contain_vowel
        global is_serial_set
        global is_num_batteries_set
        global is_indicators_set

        indicator_string = ', '.join(indicators)

        print('***** Bomb Data *****')
        print(f'Last digit of serial is odd: {is_last_digit_of_serial_odd}')
        print(f'Serial contains vowel: {does_serial_contain_vowel}')
        print(f'Batteries: {num_batteries}')
        print(f'Indicators: {indicator_string}')
        print(f'Serial set: {is_serial_set}')
        print(f'Batteries set: {is_num_batteries_set}')
        print(f'Indicators set: {is_indicators_set}')
        print('***** Bomb Data *****')

    def increment_strikes(self) -> None:
        global strikes

        strikes += 1
