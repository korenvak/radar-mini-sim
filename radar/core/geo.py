# radar/core/geo.py
from math import cos, radians

def enu_from_latlon(lat: float, lon: float, lat0: float, lon0: float) -> tuple[float, float]:
    """
    Convert latitude/longitude (degrees) to local ENU offsets (meters)
    relative to the reference point (lat0, lon0), using a flat-Earth approximation.
    Returns (e, n).
    """
    M = 111320.0  # mean meters per degree of latitude (WGS84 average)
    phi0 = radians(lat0)

    n = (lat - lat0) * M
    e = (lon - lon0) * M * cos(phi0)
    return e, n

def latlon_from_enu(e: float, n: float, lat0: float, lon0: float) -> tuple[float, float]:
    """
    Convert local ENU offsets (meters) to latitude/longitude (degrees)
    relative to the reference point (lat0, lon0), using a flat-Earth approximation.
    Returns (lat, lon).
    """
    M = 111320.0
    phi0 = radians(lat0)

    lat = lat0 + (n / M)
    lon = lon0 + (e / (M * cos(phi0)))
    return lat, lon

