class NotesApplication(object):
    """docstring author NotesApplication"""
    def __init__(self, author):
        self.author = author
        self.notes_list = []

    def create(self, note_content):
        self.notes_list.append(note_content)
        print "Note created succesfully!\n"
        note.user_choice()

    def lists(self):
        if len(self.notes_list) < 1:
            print "Sorry list is empty!\n"
        else:
            for index, content in enumerate(self.notes_list):
                print "Note ID: %d \n" %(index) + self.notes_list[index] + "\n\nBy Author  %s" %(self.author)
        note.user_choice()

    def get(self, note_id):
        if len(self.notes_list) < 1:
            print "\nSorry list is empty!\n"
        elif note_id > len(self.notes_list) - 1 or note_id < 0:
            print "\nSorry wrong ID! View the list and select the right ID!\n"
        return self.notes_list[note_id]

    def search(self, search_text):
        print "showing results for \'%s\': \n" %(search_text)
        counter = 0
        if len(self.notes_list) < 1:
            print "Sorry you haven't created any notes...list is empty!\n"
        else:
            for index, notes in enumerate(self.notes_list):
                if search_text in notes:
                    print "Note ID: %d\n" %(index) , self.notes_list[index] , "\n\nBy Author  %s" %(self.author)
                    counter += 1
                if counter < 1:
                    print "Sorry no note(s) found!\n"
        note.user_choice()

    def delete(self, note_id):
        if len(self.notes_list) < 1:
            print "\nSorry list is empty!\n"
        elif note_id > len(self.notes_list) - 1 or note_id < 0:
            print "\nSorry wrong ID! View the list and select the right ID!\n"
        else:
            self.notes_list.pop(note_id)
            print "\n Note successfully deleted!\n"
        note.user_choice()

    def edit(self, note_id, new_content):
        self.notes_list[note_id] = new_content
        print "Noted edited successfully!\n"
        note.user_choice()

    def user_choice(self):
        print "\nPlease select an option by selecting the corresponding number:\n"
        print "\n1. Create a new note\n2. View all notes\n3. Search a note\n\
4. Delete a note\n5. Edit previous note\n6. Exit\n...\n"
        user_choice = raw_input("Please select a number and press enter: ")
        choice = user_choice.isdigit()
        if choice:
            user_choice = int(user_choice)
            if user_choice > 6 or user_choice < 1:
                print "Sorry the number you selected is an invalid number...select a number between 1 to 5\n"
                notes.user_choice()
            else:
                if user_choice == 1:
                    note_content = raw_input("\nPlease type your note below:\n")
                    if len(note_content) < 1:
                        print "Wrong entry! Type a word or text!\n"
                        note.user_choice()
                    else:
                        note.create(note_content)
                elif user_choice == 2:
                    print note.lists()
                elif user_choice == 3:
                    search_text = raw_input("Please enter search text!\n")
                    if len(search_text) < 1:
                        print "Sorry you didn't type any word\n"
                        note.user_choice()
                    else:
                        note.search(search_text)
                elif user_choice == 4:
                    note_id = raw_input("Type the ID of note you want to delete and press enter!\n")
                    choice2 = note_id.isdigit()
                    if choice2:
                        note_id = int(note_id)
                        note.delete(note_id)
                    print "wrong entry!\n"
                    note.user_choice
                elif user_choice == 5:
                    if len(self.notes_list) < 1:
                        print "Sorry list is empty!\n"
                    else:
                        note_id = raw_input("Enter the ID of the note you want to delete and press enter!\n")
                        choice2 = note_id.isdigit
                        if choice2:
                            note_id = int(note_id)
                            if note_id > len(self.notes_list) - 1 or note_id < 0:
                                print "\nSorry wrong ID! View the list and select the right ID!\n"
                                note.user_choice()
                            else:
                                note_content = raw_input("Please enter new content!\n")
                                note.edit(note_id, note_content)
                        else:
                            print "Wrong entry!\n"
                    note.user_choice()
                elif user_choice == 6:
                    print "Aborting..."
                    exit()
        else:
            print "Sorry you selected an invalid number...select a number between 1 to 6\n"
            note.user_choice()

note = NotesApplication("John Sani")
note.user_choice()
