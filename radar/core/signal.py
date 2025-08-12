from typing import Tuple
from typing import Sequence
from math import cos, tau

def trajectory_line_pos(t: float,
                        start_xy: Tuple[float, float],
                        v_xy: Tuple[float, float]) -> Tuple[float, float]:
    """
    Position on a straight-line trajectory with constant velocity.
    r_s(t) = start_xy + v_xy * t

    Parameters
    ----------
    t : float
        Time [s] since reference.
    start_xy : (x0, y0) in meters.
    v_xy : (vx, vy) in m/s.

    Returns
    -------
    (x, y) at time t in meters.
    """
    x0, y0 = start_xy
    vx, vy = v_xy
    x = x0 + vx * t
    y = y0 + vy * t
    return x, y


def trajectory_line_vel(t: float,
                        v_xy: Tuple[float, float]) -> Tuple[float, float]:
    """
    Constant velocity for the straight-line trajectory.
    v_s(t) = v_xy

    Parameters
    ----------
    t : float
        Time [s] (ignored).
    v_xy : (vx, vy) in m/s.

    Returns
    -------
    (vx, vy) in m/s.
    """
    vx, vy = v_xy
    return vx, vy

def source_tones(t: float,
                 freqs: Sequence[float],
                 amps: Sequence[float],
                 phases: Sequence[float]) -> float:
    """
    Sum of cosine tones at time t:
        s(t) = sum_k amps[k] * cos(2π * freqs[k] * t + phases[k])

    Parameters
    ----------
    t : float
        Time [s].
    freqs : sequence of float
        Frequencies [Hz].
    amps : sequence of float
        Amplitudes (same length as freqs).
    phases : sequence of float
        Phases [rad] (same length as freqs).

    Returns
    -------
    float
        Signal value s(t).
    """
    # Validate lengths: each tone must have (f, A, phi)
    if not (len(freqs) == len(amps) == len(phases)):
        raise ValueError("freqs, amps, and phases must have the same length")

    s = 0.0
    for f, A, phi in zip(freqs, amps, phases):
        s += A * cos(tau * f * t + phi)  # tau = 2π
    return s




