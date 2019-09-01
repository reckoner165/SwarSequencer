from noteparser import get_raag, get_raag_list
from sequencer import Sequencer

import code
import os
import Queue

from threading import Thread

root = [440]
raag = get_raag('Bhairav')
raag.update({'name': 'Bhairav'})
phrase_length = 16

sequencer = Sequencer()
status_queue = Queue.Queue()

status = {
    'notes': [1],
    'root': root,
    'duration': [0.2],
    'stutter': [1],
    'degrade': [0]
}

t = Thread(target=sequencer.sequence, args=(status_queue,))
t.daemon = True
t.start()

# Interaction Methods

def set_phrase_length(length):
    global phrase_length
    phrase_length = length

def aaroha(stutter=1, degrade=0):
    play_notes = _get_aaroha(phrase_length, stutter)
    status['notes'] = play_notes
    status['degrade'] = [degrade]
    send_notes(status)

def avaroha(stutter=1, degrade=0):
    play_notes = _get_avaroha(phrase_length, stutter)
    status['notes'] = play_notes
    status['degrade'] = [degrade]
    send_notes(status)

def sequence_notes(note_list, num_notes, stutter, is_avaroha = False):
    status['stutter'] = [stutter]
    if num_notes > len(note_list):
        return_notes = note_list
        if is_avaroha:
            for n in range(0, num_notes - len(note_list)):
                return_notes.append(int(note_list[n]) - 12)
        else:
            for n in range(0, num_notes - len(note_list)):
                return_notes.append(int(note_list[n]) + 12)

    else:
        return_notes = note_list[0: num_notes]

    print return_notes
    return return_notes

def send_notes(status):
    status_queue.put(status)

def set_raag(raag_name):
    global raag
    raag = get_raag(raag_name)
    raag.update({'name': raag_name})
    print "raag set to: ", str(raag['name'])

def get_current_raag():
    print raag['name']

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

def bpm(bpm):
    new_duration = 60.00 / bpm
    status['duration'] = [new_duration]
    status_queue.put(status)
    print "Tempo set to", bpm

# Internal Methods
def _get_aaroha(num_notes, stutter=1):
    global raag
    play_notes = raag['aaroha']
    return sequence_notes(play_notes, num_notes, stutter)

def _get_avaroha(num_notes, stutter=1):
    global raag
    play_notes = raag['avaroha']
    return sequence_notes(play_notes, num_notes, stutter, is_avaroha = True)


if __name__ == "__main__":
    code.interact(
        banner="Now interactively running SwarSequencer",
        local=locals()
    )

