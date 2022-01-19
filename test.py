import unittest
from main import suggest, load_words, load_common_words

class TestRespondToName(unittest.TestCase):

  def test_suggestion(self):
    all_words = load_words()
    common_words = load_common_words()
    self.assertEqual(suggest("", all_words, common_words), "Please enter a word")

    self.assertEqual(suggest("where", all_words, common_words), "where is a word")
  

if __name__ == '__main__':
    unittest.main()