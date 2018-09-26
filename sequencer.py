__author__ = 'Sumanth Srinivasan'

from pyaudio import paInt16

from packages.soundmodular import Patcher
from noteparser import get_raag
from util.freq import get_frequency

options = {
    'format': paInt16,
    'channels': 2,
    'sampling_rate': 22000,
    'save_file': 'testfile.wav'
}

root = [440]
raag_name = ['Adana']
raag = get_raag(raag_name[0])
print raag['aaroha']

patcher = Patcher(options)
module = patcher.module
T = 0.3                 # Time in seconds

for note in raag['aaroha']:
    # print (type(note))
    freq = get_frequency(root[0], int(note) - 1)
    osc = module.osc_tone(T, freq)
    patcher.to_master(osc, 0.5, 0.5)

patcher.terminate()