__author__ = 'Sumanth Srinivasan'

from pyaudio import paInt16
from packages.soundmodular import Patcher
from util.freq import get_frequency
import Queue

class Sequencer:
    def __init__(self):
        options = {
            'format': paInt16,
            'channels': 2,
            'sampling_rate': 22000,
            'save_file': 'testfile.wav'
        }

        self.patcher = Patcher(options)
        self.module = self.patcher.module

    def sequence(self, queue):
        current_status = {
            'notes': [1],
            'root': [440],
            'duration': [0.2],
            'stutter': [1]
        }

        while True:

            try:
                new_status = queue.get(timeout=0.1)
                current_status = dict(current_status, **new_status)
            except Queue.Empty:
                pass

            '''
            TODO: for note, time in zip(current_status['notes'], current_status['time'])
            '''

            for note in current_status['notes']:
                if note == 0:
                    continue

                freq = get_frequency(current_status['root'][0], int(note) - 1)
                for i in range (0, current_status['stutter'][0]):
                    osc = self.module.osc_tone(current_status['duration'][0] / current_status['stutter'][0], freq)
                    self.patcher.to_master(osc, 0.5, 0.5)


