import pyaudio
import numpy as np
import aubio
import rtmidi

# Constants for the audio stream
FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 44100
CHUNK = 1024


# Initialize PyAudio
audio = pyaudio.PyAudio()
info = audio.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
audio_input_devices = {}
print("Available audio input devices:")
for i in range(0, numdevices):
        maxInChannels = (audio.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) 
        if maxInChannels > 0:
            device_name = audio.get_device_info_by_host_api_device_index(0, i).get('name') 
            print( f"  {i}: {device_name} ( MaxChannels: {maxInChannels} )")
            audio_input_devices[device_name] = i

# Initialize Aubio's note detection object
nDetection = aubio.notes("default", CHUNK, CHUNK//2, RATE)
nDetection.set_silence(-40)

# Initialize MIDI
midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()
print("Available MIDI ports:")
_ = [print(f"  {i}: {p}") for i,p in enumerate(available_ports)]

# Select the MIDI port and audio input device to be used from the printed lists above
AUDIO_DEVICE_NAME = 'MacBook Air Microphone'
MIDI_PORT_NAME = 'IAC Driver from_python'

# Start the audio stream
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK,
                    input_device_index=audio_input_devices[AUDIO_DEVICE_NAME])

# Only start if the desired MIDI port is available
if  MIDI_PORT_NAME in available_ports:
    midiout.open_port(available_ports.index(MIDI_PORT_NAME))

    print("Recording and detecting notes from the microphone...")
    print("[ NoteOn, Velocity, NoteOff] using MIDI convention, e.g. C3 = 60")
    last_note = 0
    # Record a few seconds of audio and detect notes.
    # Then send found notes as MIDI messages.
    for i in range(0, int(RATE / CHUNK * 20)):
        data = stream.read(CHUNK//2)
        samples = np.frombuffer(data, dtype=aubio.float_type)
        notes_found = nDetection(samples)
        if  any(notes_found):
            #print(notes_found)
            if notes_found[2] > 0 and notes_found[0] != notes_found[2]:
                note_off = [0x80, notes_found[2], 0]
                midiout.send_message(note_off)
                print(aubio.midi2note(int(notes_found[2])), " [note off]")
            if notes_found[0] > 0 and notes_found[0] != notes_found[2]:
                note_on = [0x90, notes_found[0], notes_found[1]]
                midiout.send_message(note_on)
                last_note = notes_found[0]
                print( aubio.midi2note(int(notes_found[0])), " [note on]"," Velocity: ", notes_found[1])
            
# Clear the last note played (avoiding hanging notes)
midiout.send_message([0x80, last_note, 0])

# Stop and close the stream
stream.stop_stream()
stream.close()
audio.terminate() 

print("Recording stopped.")

