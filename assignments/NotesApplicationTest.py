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
        self.assertEqual("Not found", search.search("lists"))

    def test_NotesApplication_list(self):
        lists = NotesApplication('John')
        self.assertEqual("Sorry list is empty!", lists.lists())

    def test_NotesApplication_list2(self):
        list2 = NotesApplication('John')
        counter = list2.list()
        self.assertEqual(counter, 2)

    def test_NotesApplication_list3(self):
        list3 = NotesApplication('John')
        counter = list3.list()
        self.assertEqual(counter, 3)


    def test_NotesApplication_get(self):
        get = NotesApplication('John')
        self.assertEqual("Sorry wrong ID! View the list and select the right ID!", get.get(7))

    def test_NotesApplication_delete2(self):
        delete2 = NotesApplication('John')
        self.assertEqual("Sorry wrong ID! View the list and select the right ID!", delete2.delete(7))


    def test_NotesApplication_delete3(self):
        delete3 = NotesApplication('John')
        self.assertEqual("Sorry list is empty!", delete3.delete(3))


    def test_NotesApplication_delete(self):
        delete = NotesApplication('John')
        self.assertEqual("Note successfully deleted!", delete.delete(0))

    def test_NotesApplication_edit(self):
        edit = NotesApplication('John')
        self.assertEqual("Noted edited successfully!", edit.edit(0, "Wonderful!"))

    def test_NotesApplication_edit2(self):
        edit2 = NotesApplication('John')
        self.assertEqual("Sorry list is empty!", edit2.edit(3, "Great"))



if __name__ == '__main__':
	unittest.main()
