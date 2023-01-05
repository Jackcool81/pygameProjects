import mido
import rtmidi
from mido import MidiFile


for msg in MidiFile('simpl.mid').play():
    print(msg)
    if count < 2:
        count+=1
    else:
        if msg.note <= 70:
            print('ewq')

