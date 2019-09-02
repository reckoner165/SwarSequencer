from noteparser import get_raag, get_raag_list
from sequencer import Sequencer

import code
import os
import Queue
import random

from threading import Thread, Timer

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

def aaroha(subphrases=1, stutter=1, degrade=0):
    play_notes = _get_aaroha(subphrases, phrase_length)
    print "playing aaroha", play_notes
    status['notes'] = play_notes
    status['degrade'] = [degrade]
    status['stutter'] = [stutter]
    send_notes(status)

def avaroha(subphrases=1, stutter=1, degrade=0):
    play_notes = _get_avaroha(subphrases, phrase_length)
    print "playing avaroha", play_notes
    status['notes'] = play_notes
    status['degrade'] = [degrade]
    status['stutter'] = [stutter]
    send_notes(status)

def sequence_phrases(num_phrases, note_list, is_avaroha=False):
    global phrase_length
    used_up_phase_lengths = 0
    phrase = []

    for n in range(0, num_phrases):
        # Pick a random starting point for each subphrase
        seed = random.randint(1,len(note_list))

        # If this is the final subphrase, user remainder length as subphrase length
        if n == num_phrases - 1:
            subphrase_length = phrase_length - used_up_phase_lengths

        else:
            subphrase_length = random.randint(2, phrase_length/num_phrases)
            used_up_phase_lengths += subphrase_length

        phrase += sequence_phrase(note_list, subphrase_length, is_avaroha, seed=seed)

    # BUG: Sometime the phrase comes shorter than phrase_length. Needs to be fixed.
    # if len(phrase) < phrase_length:
    #     print "SHORT!"
    return phrase

def sequence_phrase(note_list, num_notes, is_avaroha, seed=1):
    print num_notes

    start = seed - 1
    offset = start + num_notes

    if offset > len(note_list):
        return_notes = note_list[start:]
        for n in range(0, offset - len(note_list)):
            if is_avaroha is True:
                return_notes.append(get_note_at_index(note_list, n, is_avaroha=True) + 12)
            else:
                return_notes.append(get_note_at_index(note_list, n, is_avaroha=False) + 12)
            print return_notes
    else:
        return_notes = note_list[start:offset]

    return return_notes

'''
Returns note at a given index, given the list of notes.
If the index falls outside the list, the method wraps around the list, while changing the octave.
'''
def get_note_at_index(list, index, is_avaroha=False):
    if index >= len(list):
        if is_avaroha is True:
            return int(get_note_at_index(list, index - len(list), is_avaroha)) - 12
        else:
            print len(list), index
            return int(get_note_at_index(list, index - len(list))) + 12
    else:
        return int(list[index])

def send_notes(status):
    try:
        # Throttle adding data to the queue in case multiple queue values cancel each other out
        status_queue.put(status, timeout=0.1)
    except Queue.Full:
        timer = Timer(0.2, send_notes, status)
        timer.start()

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
def _get_aaroha(subphrases, num_notes):
    global raag
    play_notes = raag['aaroha']
    return sequence_phrases(subphrases, play_notes, num_notes)

def _get_avaroha(subphrases, num_notes):
    global raag
    play_notes = raag['avaroha']
    return sequence_phrases(subphrases, play_notes, is_avaroha = True)


if __name__ == "__main__":
    code.interact(
        banner="Now interactively running SwarSequencer",
        local=locals()
    )

