import unittest
from NotesApplication import NotesApplication
class NotesApplicationTestSuite(unittest.TestCase):


    def test_NotesApplication_create(self):
        create = NotesApplication('John')
        self.assertEqual("Note created successfully!", create.create(" Nigeria"))

    def test_NotesApplication_create2(self):
        create2 = NotesApplication('John')
        self.assertEqual("Wrong entry! Type a word or text!", create2.User_choice(1), msg = "Wrong entry! Type a word or text!")


    def test_NotesApplication_search(self):
        search = NotesApplication('John')
        self.assertEqual("Not found", search.search(" lime"))

    def test_NotesApplication_list(self):
        lists = NotesApplication('John')
        self.assertEqual("Sorry list is empty!", search.lists("Nice"))

    def test_NotesApplication_get(self):
        get = NotesApplication('John')
        self.assertEqual("Sorry wrong ID! View the list and select the right ID!", get.get(7))

    def test_NotesApplication_delete2(self):
        delete2 = NotesApplication('John')
        self.assertEqual("Sorry wrong ID! View the list and select the right ID!", delete2.delete(7))


    def test_NotesApplication_delete(self):
        delete = NotesApplication('John')
        self.assertEqual("Note successfully deleted!", delete.delete(0))

    def test_NotesApplication_edit(self):
        edit = NotesApplication('John')
        self.assertEqual("Noted edited successfully!", edit.edit(0, "Wonderful!"))


if __name__ == '__main__':
	unittest.main()
