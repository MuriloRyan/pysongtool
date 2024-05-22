from objects.CircularLinkedList import CircularLinkedList

from objects.scales import scales_list
from objects.chords import chord_list

from exceptions.UnknownChord import UnknownChord
from exceptions.WrongNote import WrongNote

class PySongTool:
    def __init__(self, circular_linked_list_object=CircularLinkedList):
        self.list = circular_linked_list_object()
        self.chords = chord_list

        self.list.append('C')
        self.list.append('C#')
        self.list.append('D')
        self.list.append('D#')
        self.list.append('E')
        self.list.append('F')
        self.list.append('F#')
        self.list.append('G')
        self.list.append('G#')
        self.list.append('A')
        self.list.append('A#')
        self.list.append('B')
    
    def chord(self, root_note: str,chord_name: str):
        root_note = root_note.upper()

        try:
            intervals = chord_list[chord_name]
            
        except:
            raise UnknownChord(root_note, chord_name)

        notes = []

        #get info about the root note (symbol,index)
        try:
            root_info: dict = self.list.find_one(root_note)
        except:
            raise WrongNote(root_note)

        #get the symbol
        notes.append(root_info[0].data)

        for i in intervals:

            #find a note using: root index + chord note interval (in semitones)
            notes.append(self.list[root_info[1] + i].data)

        return {
            'notes': notes
        }

    def scale(self, root_note: str, scale_name: str):
        root_note = root_note.upper()
        notes = []
        chords = []

        try:
            scale_info = scales_list[scale_name]

            intervals = scale_info['notes']
            _chords = scale_info['chords']
            
        except:
            raise UnknownScale(root_note, scale_name)
        
        try:
            root_info: dict = self.list.find_one(root_note)
        except:
            raise WrongNote(root_note)

        #get the symbol
        notes.append(root_info[0].data)

        for i in intervals:

            #find a note using: root index + chord note interval (in semitones)
            notes.append(self.list[root_info[1] + i].data)

        for i in range(len(notes)):
            _current_note = notes[i]
            _current_chord = _chords[i]

            chords.append(f'{_current_note}{_current_chord}')

        return {
            'notes': notes,
            'chords': chords
        }


    
