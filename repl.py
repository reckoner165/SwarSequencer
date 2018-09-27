from pyaudio import paInt16

from packages.soundmodular import Patcher
from noteparser import get_raag, get_raag_list
from util.freq import get_frequency

import code
import os

options = {
    'format': paInt16,
    'channels': 2,
    'sampling_rate': 22000,
    'save_file': 'testfile.wav'
}

root = [440]

patcher = Patcher(options)
module = patcher.module
T = 0.3

def play_aaroha(raag_name):
    raag = get_raag(raag_name)
    for note in raag['aaroha']:
        freq = get_frequency(root[0], int(note) - 1)
        osc = module.osc_tone(T, freq)
        patcher.to_master(osc, 0.5, 0.5)

def play_avaroha(raag_name):
    raag = get_raag(raag_name)
    for note in raag['avaroha']:
        freq = get_frequency(root[0], int(note) - 1)
        osc = module.osc_tone(T, freq)
        patcher.to_master(osc, 0.5, 0.5)

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