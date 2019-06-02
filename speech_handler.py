from enum import Enum

import queue
import speech_recognition as sr

class RecognitionMode(Enum):
    Keyword = 'Listen in background for specific keywords. Only recognized keywords trigger an action.'
    Module =  'Listen in background for all audio. All audio is treated as input to the active module.'
    Exit =    'Exit program'

class SpeechHandler:
    def __init__(self, speech_queue: queue.Queue) -> None:
        self.speech_queue = speech_queue
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.state = RecognitionMode.Keyword

        with self.microphone:
            self.recognizer.adjust_for_ambient_noise(self.microphone)
            self.recognizer.energy_threshold = 2000

        self.stop_listening = self.recognizer.listen_in_background(self.microphone, self.recognize_keyword)

    def recognize_keyword(self, recognizer: sr.Recognizer, audio_data: sr.AudioData) -> None:
        try:
            recognized_speech = str.lower(recognizer.recognize_google(audio_data))

            if (('exit' in recognized_speech) or ('quit' in recognized_speech) or ('stop' in recognized_speech)):
                print('RECOGNITION: Exit command.')

                self.stop_listening(False)
                self.state = RecognitionMode.Exit
                self.speech_queue.put('exit')
            if (recognized_speech.startswith('print')):
                print('RECOGNITION: Print command.')

                self.speech_queue.put('print bomb')
            if (recognized_speech.startswith('strike')):
                print('RECOGNITION: Strike command.')

                self.speech_queue.put('add strike')
            elif (recognized_speech.startswith('initialize') or recognized_speech.startswith('setup')):
                print(f'RECOGNITION: Initialization.')

                self.state = RecognitionMode.Module
                self.speech_queue.put('initialize')
            elif recognized_speech.startswith('module'):
                print('RECOGNITION: Module start.')

                self.state = RecognitionMode.Module
                self.speech_queue.put(recognized_speech)
            elif self.state == RecognitionMode.Module:
                if (('finish' in recognized_speech) or ('complete' in recognized_speech)):
                    print('RECOGNITION: Module complete.')

                    self.state = RecognitionMode.Keyword
                else:
                    print('RECOGNITION: Module in progress.')

                    self.speech_queue.put(recognized_speech)
            else:
                print('RECOGNITION: No matching command found. Ignoring...')
        except sr.UnknownValueError:
            print('Sorry, I could not understand that.')
        except sr.RequestError as request_error:
            print(f'Sorry, I could not request results from the Google Speech Recognition Service: {request_error}')
