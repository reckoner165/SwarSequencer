__author__ = 'Sumanth Srinivasan'

# Pythagorean interval ratios
semitones = {
    0: 1,
    1: 1.053,
    2: 1.125,
    3: 1.185,
    4: 1.265,
    5: 1.333,
    6: 1.4238,
    7: 1.5,
    8: 1.601,
    9: 1.6875,
    10: 1.778,
    11: 1.898,
}

def get_frequency(root_freq, semitone):
    if semitone >= 12:
        return 2 * get_frequency(root_freq, semitone - 12)

    if semitone < 0:
        return 0.5 * get_frequency(root_freq, semitone + 12)

    return root_freq * semitones[semitone]