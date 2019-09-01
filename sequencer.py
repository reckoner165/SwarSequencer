__author__ = 'Sumanth Srinivasan'

from pyaudio import paInt16
from packages.soundmodular import Patcher
from util.freq import get_frequency
import Queue
import random

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

        self.home_status = {
            'notes': [1],
            'root': [440],
            'duration': [0.2],
            'stutter': [1],
            'degrade': [0]
        }

        self.status = self.home_status

    def sequence(self, queue):
        while True:

            try:
                new_status = queue.get(timeout=0.1)
                self.status = dict(self.status, **new_status)
            except Queue.Empty:
                pass

            '''
            TODO: for note, time in zip(current_status['notes'], current_status['time'])
            '''

            self.play(self.status['notes'], self.status['duration'][0])
            self.status = dict(self.status, **self.home_status)


    def play(self, notes, duration):
        for note in notes:
                # Subdivided notes are in a list
                if type(note) is list:
                    self.play(note, duration/len(note), degrade)
                    continue

                # if random.random() <= degrade:
                #     self.play([0], duration)

                # 0 signifies a rest/silent note
                if note == 0:
                    # Send out a block of silence for one subdivision
                    silence = self.module.silence(duration)
                    self.patcher.to_master(silence, 0, 0)
                    continue

                freq = get_frequency(self.status['root'][0], int(note) - 1)
                for i in range (0, self.status['stutter'][0]):
                    if random.random() <= self.status['degrade'][0]:
                        silence = self.module.silence(duration)
                        self.patcher.to_master(silence, 0, 0)
                    else:
                        osc = self.module.osc_tone(duration / self.status['stutter'][0], freq)
                        self.patcher.to_master(osc, 0.5, 0.5)


