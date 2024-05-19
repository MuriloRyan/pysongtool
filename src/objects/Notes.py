from CircularLinkedList import CircularLinkedList

class NoteList:
    def __init__(self, circular_linked_list_object=CircularLinkedList):
        self.list = circular_linked_list_object()
    
    