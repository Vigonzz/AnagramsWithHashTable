# Test cases for the hashtable file

import unittest
from hashtable import HashTable

class TestHash(unittest.TestCase):

    
    def test_empty_table(self):
        ''' Test to ensure the table is empty '''
        test_table = HashTable()
        self.assertEqual(test_table.size(), 0)
    
    
    def test_inserting(self):
        ''' Test insert into the table '''
        insert_table = HashTable()

        insert_table.insert("sister")
        insert_table.insert("good")
        insert_table.insert("darcy")

        self.assertEqual(insert_table.size(), 3)

    
    def test_duplicates(self):
        ''' Test duplicates '''
        duplicate_table = HashTable()

        word = duplicate_table.insert("mr")
        words = duplicate_table.insert("mr")

        self.assertEqual(duplicate_table.size(), 1)
        self.assertFalse(words)
        self.assertTrue(word)

    def test_collisions(self):
        ''' Test for collision, ensure the the words can still 
        exist as one chain in a 0 slot. Proves collision handling works '''

        collision = HashTable(1)

        collision.insert("good morning")
        collision.insert("good afternoon")
        collision.insert("good night")
        self.assertEqual(collision.size(), 3)

        word_collision = collision.insert("good morning")
        self.assertEqual(collision.size(), 3)

        self.assertFalse(word_collision)

    def test_empty_string(self):
        ''' Test handling for an empty string '''
        empty_string = HashTable()
        blank = empty_string.insert("")
        self.assertTrue(blank)
        self.assertEqual(empty_string.size(), 1)
        
        blanks = empty_string.insert("")
        self.assertFalse(blanks)
        self.assertEqual(empty_string.size(), 1)


if __name__ == "__main__":
    unittest.main()