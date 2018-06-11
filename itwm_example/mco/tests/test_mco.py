import unittest

from itwm_example.mco.mco import get_weights


class TestMCO(unittest.TestCase):
    def test_get_weights(self):
        self.assertEqual(get_weights(1, 5), [1.0])
        self.assertEqual(get_weights(2, 5), [
            (0.0, 1.0),
            (0.25, 0.75),
            (0.50, 0.50),
            (0.75, 0.25),
            (1.0, 0.0),
        ])

        self.assertEqual(get_weights(3, 3), [
            (0.0, 0.0, 1.0),
            (0.0, 0.25, 0.75),
            (0.25, 0.0, 0.75),
            (0.0, 0.50, 0.50),
            (0.25, 0.25, 0.50),
            (0.50, 0.0, 0.50),
            (0.0, 0.75, 0.25),
            (0.25, 0.50, 0.25),
            (0.50, 0.25, 0.25),
            (0.75, 0.0, 0.25),
            (0.0, 1.0, 0.0),
            (0.25, 0.75, 0.0),
            (0.50, 0.50, 0.0),
            (0.75, 0.25, 0.0),
            (1.0, 0.0, 0.0),
        ])

        self.assertEqual(get_weights(3, 7), [
            (0.0, 0.0, 1.0),
            (0.0, 0.166666666667, 0.833333333333),
            (0.0, 0.333333333333, 0.666666666667),
            (0.0, 0.5, 0.5),
            (0.0, 0.666666666667, 0.333333333333),
            (0.0, 0.833333333333, 0.166666666667),
            (0.0, 1.0, 0.0),
            (0.166666666667, 0.0, 0.833333333333),
            (0.166666666667, 0.166666666667, 0.666666666667),
            (0.166666666667, 0.333333333333, 0.5),
            (0.166666666667, 0.5, 0.333333333333),
            (0.166666666667, 0.666666666667, 0.166666666667),
            (0.166666666667, 0.833333333333, 0.0),
            (0.333333333333, 0.0, 0.666666666667),
            (0.333333333333, 0.166666666667, 0.5),
            (0.333333333333, 0.333333333333, 0.333333333333),
            (0.333333333333, 0.5, 0.166666666667),
            (0.333333333333, 0.666666666667, 0.0),
            (0.5, 0.0, 0.5),
            (0.5, 0.166666666667, 0.333333333333),
            (0.5, 0.333333333333, 0.166666666667),
            (0.5, 0.5, 0.0),
            (0.666666666667, 0.0 0.333333333333),
            (0.666666666667, 0.166666666667, 0.166666666667),
            (0.666666666667, 0.333333333333, 0.0),
            (0.833333333333, 0.0, 0.166666666667),
            (0.833333333333, 0.166666666667, 0.0),
        ])
