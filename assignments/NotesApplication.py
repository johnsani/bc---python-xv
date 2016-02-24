class NotesApplication(object):
    """class that defines a note taking application
    Attributes: author: the author's name,
                notes_list: A list containg all the notes
    """

    def __init__(self, author):
        self.author = author
        self.notes_list = []

    def create(self, note_content):
        """Creates neww note for user"""
        if len(note_content) < 1:
            return False
        else:
            self.notes_list.append(note_content)
            return "Note created successfully!"

    def lists(self):
        """To check the number of notes the user has created"""
        if len(self.notes_list) < 1:
            return False
        else:
            list_counter = 0
            for index, content in enumerate(self.notes_list):
                "Note ID: %d" % (index) + self.notes_list[index] \
                    + "By Author  %s" % (self.author)
                list_counter += 1
        return list_counter

    def get(self, note_id):
        """To return a note from lists of notes created by the user"""
        if len(self.notes_list) < 1:
            return False
        elif note_id > len(self.notes_list) - 1 or note_id < 0:
            return False
        return self.notes_list[note_id]

    def search(self, search_text):
        """searches for text or word from the lists of notes and returns note"""
        counter = 0
        if len(self.notes_list) < 1:
            return False
        else:
            for index, notes in enumerate(self.notes_list):
                if search_text in notes:
                    "Note ID: %d" % (index) + self.notes_list[index]\
                        + "By Author  %s" % (self.author)
                    counter += 1
                if counter < 1:
                    return False

    def delete(self, note_id):
        """Deletes a note from the list of notes"""
        if len(self.notes_list) < 1:
            return False
        elif note_id > len(self.notes_list) - 1 or note_id < 0:
            return False
        else:
            self.notes_list.pop(note_id)
            return "Note successfully deleted!"

    def edit(self, note_id, new_content):
        """edits a specific note in the list"""
        if len(self.notes_list) < 1:
            return False
        else:
            self.notes_list[note_id] = new_content
            return "Noted edited successfully!"

note = NotesApplication("John")
