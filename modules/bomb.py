import utilities

is_serial_set = False
is_num_batteries_set = False
is_indicators_set = False
is_ports_set = False

is_last_digit_of_serial_odd = False
does_serial_contain_vowel = False
num_batteries = -1
indicators = []
ports = []
strikes = 0

class Bomb:
    wire_modules = []
    button_modules = []
    keypad_modules = []
    simon_says_modules = []
    whos_on_first_modules = []
    complicated_wires_modules = []
    memory_modules = []

    def set_serial(self, audio_data: str) -> None:
        global is_last_digit_of_serial_odd
        global does_serial_contain_vowel
        global is_serial_set

        if 'even' in audio_data:
            is_last_digit_of_serial_odd = False
        elif (('odd' in audio_data) or ('aud' in audio_data)):
            is_last_digit_of_serial_odd = True

        if 'vowel' in audio_data:
            does_serial_contain_vowel = True

        is_serial_set = True

    def set_batteries(self, audio_data: str) -> None:
        global num_batteries
        global is_num_batteries_set

        # Get last word of command, which should be the number of batteries.
        batteries = audio_data.split()[-1]
        num_batteries = utilities.string_to_number(batteries)
        if num_batteries != -1:
            is_num_batteries_set = True
        else:
            print('Could not parse batteries! Please re-enter the number of batteries by saying "batteries <number>".')

    def set_indicators(self, audio_data: str) -> None:
        global indicators
        global is_indicators_set

        is_indicators_set = True
        for word in audio_data.split()[2:]:
            indicators.append(word)

    def set_ports(self, audio_data: str) -> None:
        global ports
        global is_ports_set

        is_ports_set = True
        for word in audio_data.split()[2:]:
            ports.append(word)

    def increment_strikes(self) -> None:
        global strikes

        strikes += 1

    def print(self) -> None:
        global is_last_digit_of_serial_odd
        global does_serial_contain_vowel
        global num_batteries
        global indicators
        global ports
        global is_serial_set
        global is_num_batteries_set
        global is_indicators_set
        global is_ports_set

        indicator_string = ', '.join(indicators)
        port_string = ', '.join(ports)

        print('***** Bomb Data *****')
        print(f'Last digit of serial is odd: {is_last_digit_of_serial_odd}')
        print(f'Serial contains vowel: {does_serial_contain_vowel}')
        print(f'Batteries: {num_batteries}')
        print(f'Indicators: {indicator_string}')
        print(f'Ports: {port_string}')
        print(f'Serial set: {is_serial_set}')
        print(f'Batteries set: {is_num_batteries_set}')
        print(f'Indicators set: {is_indicators_set}')
        print(f'Ports set: {is_ports_set}')
        print('***** Bomb Data *****')
