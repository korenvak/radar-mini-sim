import unittest
from math import pi
from radar.core.signal import source_tones

class TestSourceTones(unittest.TestCase):
    def test_single_tone(self):
        # A=2, f=10 Hz, phi=0
        self.assertAlmostEqual(source_tones(0.0, [10.0], [2.0], [0.0]), 2.0, places=12)
        # t=0.25s -> 2π*10*0.25 = 5π, cos(5π) = -1 => -2
        self.assertAlmostEqual(source_tones(0.25, [10.0], [2.0], [0.0]), -2.0, places=12)

    def test_two_tones_sum(self):
        # tone1: A=1, f=5, phi=0 ; tone2: A=0.5, f=5, phi=π (180° out of phase)
        # at t=0: cos(0)=1, cos(π)=-1 -> 1*1 + 0.5*(-1) = 0.5
        self.assertAlmostEqual(source_tones(0.0, [5.0, 5.0], [1.0, 0.5], [0.0, pi]), 0.5, places=12)

    def test_length_mismatch_raises(self):
        # amps length != freqs length -> must raise
        with self.assertRaises(ValueError):
            source_tones(0.0, [10.0, 20.0], [1.0], [0.0, 0.0])

    def test_empty_lists_return_zero(self):
        self.assertAlmostEqual(source_tones(0.123, [], [], []), 0.0, places=12)

if __name__ == "__main__":
    unittest.main()
