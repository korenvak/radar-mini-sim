# tests/test_geo.py
import unittest
from math import isclose
from radar.core.geo import enu_from_latlon, latlon_from_enu

class TestGeo(unittest.TestCase):
    def test_reference_point_is_zero(self):
        lat0, lon0 = 31.252, 34.791
        e, n = enu_from_latlon(lat0, lon0, lat0, lon0)
        self.assertTrue(isclose(e, 0.0, abs_tol=1e-9))
        self.assertTrue(isclose(n, 0.0, abs_tol=1e-9))

    def test_separate_east_north_effects(self):
        lat0, lon0 = 31.252, 34.791

        # shift longitude only -> east should change, north ~ 0
        e1, n1 = enu_from_latlon(lat0, lon0 + 1e-4, lat0, lon0)
        self.assertTrue(abs(e1) > 0.5)    # ~ few meters
        self.assertTrue(abs(n1) < 0.5)    # near zero

        # shift latitude only -> north should change, east ~ 0
        e2, n2 = enu_from_latlon(lat0 + 1e-4, lon0, lat0, lon0)
        self.assertTrue(abs(n2) > 0.5)
        self.assertTrue(abs(e2) < 0.5)

    def test_round_trip(self):
        lat0, lon0 = 31.252, 34.791
        # a nearby point (small deltas)
        lat, lon = 31.2535, 34.7923

        e, n = enu_from_latlon(lat, lon, lat0, lon0)
        lat2, lon2 = latlon_from_enu(e, n, lat0, lon0)

        # degrees tolerance ~1e-7 is sub-meter-ish
        self.assertTrue(isclose(lat, lat2, abs_tol=1e-7))
        self.assertTrue(isclose(lon, lon2, abs_tol=1e-7))

if __name__ == "__main__":
    unittest.main()

