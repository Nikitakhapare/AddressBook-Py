from AddressBook import AddressBook
import unittest

class TestAddressBook(unittest.TestCase):


    def setUp(self):
        self.book=AddressBook()

    def test_addContact(self):
        self.book.addContacts("niki","Khapare","Chandur","Amravati","Maharashtra",444726,9075194857,"nikitakhapare53@gmail.com")
        self.book.addContacts("rk","Khapa","chandrapur","Chandrpur","mh",56566,1482415625,"nikikhapare@gmail.com")
        self.assertEqual(len(self.book.contact),2)

    def test_editContact(self):
        self.book.editContact("niki","Khapare","Chandur","Amravati","Maharashtra",444726,9075194857,"nikitakhapare53@gmail.com")
        self.assertEqual(self.book.contact[0][0],"pari")

    
    def test_delateContact(self):
        self.book.delateContact()
        self.assertEqual(len(AddressBook.contact),1)

if __name__=="__main__":
    unittest.main()