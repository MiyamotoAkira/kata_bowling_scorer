import unittest
from bowling import bowling_scorer
from nose_parameterized import parameterized

class BowlingTests(unittest.TestCase):
#    def test_spares_of_fives_and_five(self):
#        spares_of_fives_and_five="5/5/5/5/5/5/5/5/5/5/5"
#        score = bowling_scorer.get_score_from_line(spares_of_fives_and_five)
#        self.assertEqual(150, score)
#
#
#    def test_all_strikes(self):
#        all_strike_line="XXXXXXXXXXXX"
#        score = bowling_scorer.get_score_from_line(all_strike_line)
#        self.assertEqual(300, score)

    @parameterized.expand([
    ("-", 0),
    ("1", 1),
    ("2", 2),
    ("3", 3),
    ("4", 4),
    ("5", 5),
    ("6", 6),
    ("7", 7),
    ("8", 8),
    ("9", 9),
    ("X", 10),
    ("11", 2),
    ("9/", 10),
    ("1/", 10),
    ("-/", 10),
    ("9-9-9-9-9-9-9-9-9-9-",90),
    ("-/5", 20),
    ])
    def test_roll(self, line, expected_score):
        score = bowling_scorer.get_score_from_line(line)
        self.assertEqual(expected_score, score)




