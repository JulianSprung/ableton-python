## Projects / ToDos
1. Create Overview Diagram (and components to resources below)
2. Using Python as MIDI Input Device: whistling/humming to live MIDI input
3. Using PyLive + Ableton OSC for ???
4. Using Python Remote Scripts for my Akai MPK mini mk II to map MIDI controls to Ableton[example](https://github.com/jorgalad/nano_remote_script):
    * Mode1: Producing
        - 8 Min/Max Knobs -> 
        - 8+8 Pads as Notes ->
        - 8+8 Pads as CC -> 
        - 8+8 Pads as Prog Change -> 
    * Mode2: Playing
        - 8 Min/Max Knobs -> 
        - 8+8 Pads as Notes -> 
        - 8+8 Pads as CC -> 
        - 8+8 Pads as Prog Change -> 

## 2. Using Python as MIDI Input: Mic to MIDI
Install requirements with pip.
Set `AUDIO_DEVICE_NAME` and `MIDI_PORT_NAME` in the `mic_to_midi.py` script.
Run it.
Example outputs:
>
        ableton-python/.venv/bin/python ableton-python/mic_to_midi.py
        Available audio input devices:
          0: MacBook Air Microphone ( MaxChannels: 1 )
        Available MIDI ports:
          0: MPKmini2
          1: IAC Driver from_python
          2: MIDI Monitor (Untitled)
        Recording and detecting notes from the microphone...
        [ NoteOn, Velocity, NoteOff] using MIDI convention, e.g. C3 = 60
        E6  [note on]  Velocity:  110.0
        E6  [note off]
        C#6  [note on]  Velocity:  109.0
        C#6  [note off]
        E6  [note on]  Velocity:  114.0
        E6  [note off]
        C7  [note on]  Velocity:  102.0
        C7  [note off]
        A6  [note on]  Velocity:  128.0
        A6  [note off]
        F#5  [note on]  Velocity:  110.0
        F#5  [note off]
        B6  [note on]  Velocity:  106.0
        B6  [note off]
        B6  [note on]  Velocity:  105.0
        B6  [note off]
        A5  [note on]  Velocity:  114.0
        A5  [note off]
        D6  [note on]  Velocity:  99.0
        D6  [note off]
        Recording stopped.

## 4. Using Python Remote Scripts
To update fist the MIDI notes and control messages that are sent for each button/fader/key etc [see here](https://www.youtube.com/watch?v=goUUzwead2A) 

## Resources
1. [Udemy Course: Learn Python through Music with Ableton Live](https://www.udemy.com/course/learning-python-with-ableton-live/) from [@jorgalad](https://github.com/jorgalad)
1.  [Ableton OSC: Control Ableton Live 11 via Open Sound Control (OSC)](https://github.com/ideoforms/AbletonOSC)
1. [PyLive: Query and control Ableton Live from Python (interacting with Ableton OSC as Remote Script)](https://github.com/ideoforms/pylive)
1. [The Abletong Live Object Model (LOM)](https://docs.cycling74.com/max8/vignettes/live_object_model)
1. [Youtube: Traversing the LOM](https://www.youtube.com/watch?v=qeabaagMZr8)
1. [Unofficial repository for Ableton Live 11 MIDI Remote Scripts Python Sources decompiled by Julien Bayle](https://github.com/gluon/AbletonLive11_MIDIRemoteScripts)
1. [Live API version 11 Unofficial Live API documentation](https://nsuspray.github.io/Live_API_Doc/11.0.0.xml)

1. [Mido Python Package:](https://github.com/mido/mido) Midi Objects for Python
1. [rtmidi Python Package:](https://pypi.org/project/python-rtmidi/) A Python binding for the RtMidi C++ library implemented using Cython.