string_to_number_mapping = {
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
    'none': 0,
    'one': 1,
    'won': 1,
    'two': 2,
    'to': 2,
    'too': 2,
    'three': 3,
    'four': 4,
    'for': 4,
    'five': 5,
    'v': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'ate': 8,
    'nine': 9
}

def string_to_number(recognized_speech: str) -> int:
    if recognized_speech in string_to_number_mapping:
        return string_to_number_mapping[recognized_speech]
    else:
        print(f'Could not parse number: {recognized_speech}')
        return -1

nato_to_letter_mapping = {
    'alpha': 'a',
    'alfa': 'a',
    'bravo': 'b',
    'charlie': 'c',
    'delta': 'd',
    'echo': 'e',
    'foxtrot': 'f',
    'golf': 'g',
    'hotel': 'h',
    'india': 'i',
    'juliet': 'j',
    'kilo': 'k',
    'lima': 'l',
    'mike': 'm',
    'november': 'n',
    'oscar': 'o',
    'papa': 'p',
    'quebec': 'q',
    'romeo': 'r',
    'sierra': 's',
    'tango': 't',
    'uniform': 'u',
    'victor': 'v',
    'whiskey': 'w',
    'whisky': 'w',
    'xray': 'x',
    'x-ray': 'x',
    'yankee': 'y',
    'zulu': 'z',
}

# def parse_nato_to_letters(recognized_speech: str) -> str:
#     translation = []

#     for word in recognized_speech:
#         if word in nato_to_letter_mapping:
#             translation.append(nato_to_letter_mapping[word])
#         else:
#             translation.append('?')

#     return ''.join(translation)

def parse_nato_to_letter(recognized_speech: str) -> str:
    if recognized_speech in nato_to_letter_mapping:
        return nato_to_letter_mapping[recognized_speech]
    else:
        print(f'Could not parse NATO word: {recognized_speech}')
        return -1
