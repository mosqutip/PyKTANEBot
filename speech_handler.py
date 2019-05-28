import queue
import speech_recognition as sr

class SpeechHandler:
    def __init__(self, command_queue: queue.Queue) -> None:
        self.command_queue = command_queue
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        with self.microphone:
            self.recognizer.adjust_for_ambient_noise(self.microphone)

        # TODO: investigate phrase timeout
        # TODO: investigate keyword tuning
        # TODO: sensitivity/timeout tuning
        self.stop_listening = self.recognizer.listen_in_background(self.microphone, self.recognize_keyword)

    def recognize_keyword(self, recognizer: sr.Recognizer, audio_data: sr.AudioData) -> None:
        try:
            command = str.lower(recognizer.recognize_google(audio_data))
            if command.startswith('exit') or command.startswith('quit') or command.startswith('stop'):
                print('Got Exit')
                self.stop_listening(False)
                self.command_queue.put({ 'command' : 'exit' })
            elif command.startswith('set') or command.startswith('module'):
                print(f'Got command: {command}')
                self.recognize(recognizer, self.microphone, command)
        except sr.UnknownValueError:
            print('Sorry, I could not understand that.')
        except sr.RequestError as request_error:
            print(f'Sorry, I could not request results from the Google Speech Recognition Service: {request_error}')

    def recognize(self, recognizer: sr.Recognizer, microphone: sr.Microphone, command: str) -> None:
        audio_data = recognizer.listen(microphone, timeout = None, phrase_time_limit = 5)

        try:
            input_data = {
                'command': command,
                'parameters' : str.lower(recognizer.recognize_google(audio_data))
            }
            self.command_queue.put(input_data)
            print(f'Submitted command: {command}, parameters: {input_data["parameters"]}')
        except sr.UnknownValueError:
            print('Sorry, I could not understand that.')
        except sr.RequestError as request_error:
            print(f'Sorry, I could not request results from the Google Speech Recognition Service: {request_error}')
