# SwarSequencer
A sequencer that enables tonal improvisation over 163 Indian Sampurna Ragas

This is a work in progress and both the code and README will be updated with time.

## Dependencies

- python2.7
- pyaudio

## Usage

Clone this repository, ensure you have all dependencies and then run repl.py. This should start a custom python interpreter.

```python
Setting up soundmodular Patcher.
Now interactively running SwarSequencer
>>>
```

Use `get_raags()` to obtain a list of available raags.
Set raag to one from the list using `set_raag()` thus

```python
>>> set_raag('Bhairav')
raag set to:  Bhairav
>>>
```


Use a raag from the list to play the basic aaroha and avaroha scale traversal.

```python
>>> aaroha(3)
>>>
```
Should play the 3-note ascending figure from the Bhairav raag. Similarly,

```python
>>> avaroha(4)
>>>

```

Should play the 4-note descending melodic figure.

To exit the interpreter, type `exit()` 

This will terminate your session and export a `testfile.wav` in the root directory of your cloned repo.

## List of Methods (WIP documentation)

 - aaroha(number_of_notes, stutter)
 - avaroha(number_of_notes, stutter)
 - bpm(beats_per_minute)
 - get_raags()
 - set_raag(raag_name)
 - get_current_raag()
 - set_root(root_note_frequency)
 - sequence_notes(list_of_notes, number_of_notes_to_play, stutter)
 - exit()


## Shoulders

This project stands on the shoulders of a glorious corpus of Indian raags put together by [shockmonger](https://github.com/shockmonger) in their [ragaDB](https://github.com/shockmonger/ragaDB).