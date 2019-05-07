from noteparser import get_raag, get_raag_list
from sequencer import Sequencer

import code
import os
import Queue

from threading import Thread

root = [440]
raag = {'name' : None}

sequencer = Sequencer()
status_queue = Queue.Queue()

status = {
    'notes': [1],
    'root': root,
    'duration': [0.2],
    'stutter': [1]
}

t = Thread(target=sequencer.sequence, args=(status_queue,))
t.daemon = True
t.start()

# Interaction Methods

def aaroha(num_notes, stutter=1):
    global raag
    play_notes = raag['aaroha']
    sequence_notes(play_notes, num_notes, stutter)

def avaroha(num_notes, stutter=1):
    global raag
    play_notes = raag['avaroha']
    sequence_notes(play_notes, num_notes, stutter)

def sequence_notes(note_list, num_notes, stutter):
    status['stutter'] = [stutter]
    if num_notes > len(note_list):
        status['notes'] = note_list
        for n in range(1, num_notes - len(note_list)):
            status['notes'].append(int(note_list[n]) + 12)

    else:
        status['notes'] = note_list[0: num_notes]
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


if __name__ == "__main__":
    code.interact(
        banner="Now interactively running SwarSequencer",
        local=locals()
    )

