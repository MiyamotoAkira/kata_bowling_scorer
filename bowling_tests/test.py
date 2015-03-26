import unittest
from bowling import bowling_scorer
from nose_parameterized import parameterized

class BowlingTests(unittest.TestCase):
    def assert_line_score(self, line, expected_score):
        score = bowling_scorer.get_score_from_line(line)
        self.assertEqual(expected_score, score)

    def test_nines_and_misses(self):
        self.assert_line_score("9-9-9-9-9-9-9-9-9-9-",90)

    def test_spares_of_fives_and_five(self):
        spares_of_fives_and_five="5/5/5/5/5/5/5/5/5/5/5"
        score = bowling_scorer.get_score_from_line(spares_of_fives_and_five)
        self.assertEqual(150, score)


    def test_all_strikes(self):
        all_strike_line="XXXXXXXXXXXX"
        score = bowling_scorer.get_score_from_line(all_strike_line)
        self.assertEqual(300, score)

    @parameterized.expand([
    ("-", 0),
    ("1", 1),
    ("2", 2),
    ])
    def test_one_roll(self, line, expected_score):
        self.assert_line_score(line, expected_score)




