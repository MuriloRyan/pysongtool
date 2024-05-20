from CircularLinkedList import CircularLinkedList
from chords import chord_list

class NoteList:
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
        try:
            intervals = chord_list[chord_name]
            
        except:
            raise ChordNotFound

        notes = []

        root_info = self.list.find_one(root_note)

        notes.append(root_info[0].data)

        for i in intervals:
            notes.append(self.list[root_info[1] + i].data)
            print(i)

        return notes

if __name__ == '__main__':

    nt = NoteList()

    print(nt.chord('A', '6'))