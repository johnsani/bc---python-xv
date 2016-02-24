import unittest
from notesapplication import NotesApplication


class NotesApplicationTestSuite(unittest.TestCase):
    """docstring author NotesApplicationTestSuite"""

    def test_NotesApplication_create(self):
        """Tests if the create method creates a note."""

        create = NotesApplication('John')
        self.assertEqual(
            "Note created successfully!", create.create(" Nigeria"))

    def test_NotesApplication_create2(self):
        """Tests users inputs correct entry or empty string"""
        create2 = NotesApplication('John')
        self.assertEqual(False,
                         create2.create(""),
                         msg="Wrong entry! Type a word or text!")

    def test_NotesApplication_search(self):
        """Tests if the search method returns a 'Not found' string."""
        search = NotesApplication('John')
        search.create("Nigeria")
        search.create("Andela")
        self.assertEqual(False, search.search("lists"),
                         msg="Wrong entry! Type a word or text!")

    def test_NotesApplication_list(self):
        """Tests if the lists method \
        returns a value when the list \
        is empty.
        """
        lists = NotesApplication('John')
        self.assertEqual(False, lists.lists(), msg="Sorry list is empty!")

    def test_NotesApplication_list2(self):
        """Tests if the lists method \
        returns the number of elements \
        contained in the list.
        """
        list2 = NotesApplication('John')
        list2.create("Nigeria")
        list2.create("Andela")
        counter = list2.lists()
        self.assertEqual(counter, 2, msg="Successful!")

    def test_NotesApplication_list3(self):
        """Tests if the lists method \
        returns the number of elements \
        contained in the list.
        """
        list3 = NotesApplication('John')
        list3.create("Nigeria")
        list3.create("Andela")
        list3.create("Lagos")
        counter = list3.lists()
        self.assertEqual(counter, 3)

    def test_NotesApplication_get(self):
        """Tests if the get method \
        returns False \
        when the ID selected is out of range.
        """
        get1 = NotesApplication('John')
        get1.create("Nigeria")
        get1.create("Andela")
        self.assertEqual(False, get1.get(7),
                         msg="Wrong entry! Type a word or text!")

    def test_NotesApplication_delete2(self):
        """Tests if the delete method \
        returns False \
        when the ID selected is out of range.
        """
        delete2 = NotesApplication('John')
        delete2.create("Nigeria")
        self.assertEqual(False, delete2.delete(7), msg="Index out of range")

    def test_NotesApplication_delete3(self):
        """Tests if the delete method \
        returns a False \
        when the list is empty.\
        """
        delete3 = NotesApplication('John')
        self.assertEqual(False, delete3.delete(3), msg="Sorry list is empty")

    def test_NotesApplication_delete(self):
        """Tests if the delete method \
        returns a True \
        when a note is successfully deleted\
        """
        delete = NotesApplication('John')
        delete.create("Nigeria")
        delete.create("Andela")
        self.assertEqual("Note successfully deleted!", delete.delete(0))

    def test_NotesApplication_edit(self):
        """Tests if the edit method \
        returns True \
        when a note is successfully edited.\
        """
        edit = NotesApplication('John')
        edit.create("Nigeria")
        self.assertEqual(
            "Noted edited successfully!", edit.edit(0, "Wonderful!"))

    def test_NotesApplication_edit2(self):
        """Tests if the delete method \
        returns False \
        when the list is empty.\
        """
        edit2 = NotesApplication('John')
        self.assertEqual(False, edit2.edit(3, "Great"),
                         msg="Sorry list is empty")


if __name__ == '__main__':
    unittest.main()
