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
Use a raag from the list to play the basic aaroha and avaroha scale traversal.

```python
>>> play_aaroha('Bhairav')
>>>
```
Should play the ascending traversal from the Bhairav raag. Similarly, 

```python
>>> play_avaroha('Hamsadhwani')
>>>

```

Should play the descending traversal from the Hamsadhwani raag.

To exit the interpreter, type `exit()` 

This will terminate your session and export a `testfile.wav` in the root directory of your cloned repo.

## Shoulders

This project stands on the shoulders of a glorious corpus of Indian raags put together by [shockmonger](https://github.com/shockmonger) in their [ragaDB](https://github.com/shockmonger/ragaDB).