from pyaudio import paInt16

from packages.soundmodular import Patcher
from noteparser import get_raag, get_raag_list
from util.freq import get_frequency

import code
import os

from threading import Thread
import Queue

options = {
    'format': paInt16,
    'channels': 2,
    'sampling_rate': 22000,
    'save_file': 'testfile.wav'
}

root = [440]

patcher = Patcher(options)
module = patcher.module
T = 0.2

status_queue = Queue.Queue()

status = {
    'notes': [],
    'root': root
}


def sequence(queue):
    current_status = {
        'notes': [1],
        'root': [440]
    }
    while True:

        try:
            new_status = queue.get(timeout=0.1)
            current_status = new_status.copy()
        except Queue.Empty:
            pass

        '''
        TODO: for note, time in zip(current_status['notes'], current_status['time'])
        '''

        for note in current_status['notes']:
            freq = get_frequency(current_status['root'][0], int(note) - 1)
            osc = module.osc_tone(T, freq)
            patcher.to_master(osc, 0.5, 0.5)


t = Thread(target=sequence, args=(status_queue,))
t.daemon = True
t.start()

# Interaction Methods

def play_aaroha(raag_name):
    raag = get_raag(raag_name)
    status['notes'] = raag['aaroha']
    status_queue.put(status)

def play_avaroha(raag_name):
    raag = get_raag(raag_name)
    status['notes'] = raag['avaroha']
    status_queue.put(status)

def set_root(new_root):
    status['root'] = [new_root]
    status_queue.put(status)

def repl_exit():
    patcher.terminate()
    exit()


def get_raags():
    print get_raag_list()

def honk(message):
    os.system('say "' + message + '"')


if __name__ == "__main__":
    code.interact(
        banner="Now interactively running SwarSequencer",
        local=locals()
    )

