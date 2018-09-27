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
notes_queue = Queue.Queue()


def sequence(queue):
    print "playing notes!"
    old_notes = [1]
    while True:

        try:
            new_notes = queue.get(timeout=0.1)
            old_notes = new_notes[:]
        except Queue.Empty:
            pass

        for note in old_notes:
            freq = get_frequency(root[0], int(note) - 1)
            osc = module.osc_tone(T, freq)
            patcher.to_master(osc, 0.5, 0.5)


t = Thread(target=sequence, args=(notes_queue,))
t.daemon = True
t.start()


def play_aaroha(raag_name):
    raag = get_raag(raag_name)
    notes = raag['aaroha']
    notes_queue.put(notes)

def play_avaroha(raag_name):
    raag = get_raag(raag_name)
    notes = raag['avaroha']
    notes_queue.put(notes)

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

