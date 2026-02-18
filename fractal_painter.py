"""
Refactor of ActiveState recipe 578051 for Python 3.13.

Original: http://code.activestate.com/recipes/578051/
Creates a camo / Pollock-like fractal splatter using tkinter Canvas.
"""

from __future__ import annotations

import math
import random
import tkinter as tk
from dataclasses import dataclass
from typing import Callable, Dict, Tuple

# ----------------------------
# Critical parameters (tweak!)
# ----------------------------

W = 800        # canvas width
H = 500        # canvas height (rough golden-ish ratio)
nLow = 25      # recursion limiter (tile size threshold)

nCover = 0.05  # probability threshold per sweep for painting
nMSpan = 10.0  # span for "coverage" mapping (depends on recursion depth)
nCSpan = 8.0   # span for colour range
nSplatterSize = 0.25

# scale factor per recursion (not scale-invariant)
aScale = [
    0.05, 0.1, 0.6, 0.9, 0.9, 0.3, 0.1, 0.1, 0.1,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

# colour factor per recursion
aColour = [0.5] * 13

# Globals set in main()
canvas: tk.Canvas
nHorizFactor: float
nDiagFactor: float

nMinR: int
nMaxR: int
nMinG: int
nMaxG: int
nMinB: int
nMaxB: int


# ----------------------------
# Data model
# ----------------------------

@dataclass(frozen=True)
class Splat:
    z: float
    r: float
    g: float
    b: float
    rg: float
    rb: float
    gb: float
    rgb: float


# ----------------------------
# Utility functions
# ----------------------------

def col_str(x: int) -> str:
    """Clamp/wrap-ish like the original: if out of bounds, flip to 0/255."""
    if x > 255:
        x = 0
    if x < 0:
        x = 255
    s = f"{x:x}"  # hex without 0x
    return s.zfill(2)


def load(grid: Dict[str, Splat], x: int, y: int, value: Splat) -> Splat:
    """If (x,y) exists, return stored, else store provided and return it."""
    key = f"{x}_{y}"
    if key in grid:
        return grid[key]
    grid[key] = value
    return value


def zero_to_one(m: float, span: float) -> float:
    """Map real line to [0,1]."""
    return math.atan(m * span) / math.pi + 0.5


def mid(n1: int, n2: int) -> int:
    return int((n1 + n2) / 2)


def dist(p: float, scale: float) -> float:
    return p + (random.random() - 0.5) * scale


def odist(points: list[Splat], s1: float, s2: float) -> Splat:
    """Average a list of Splats then add random perturbations."""
    z = r = g = b = rg = rb = gb = rgb = 0.0
    for sp in points:
        z += sp.z
        r += sp.r
        g += sp.g
        b += sp.b
        rg += sp.rg
        rb += sp.rb
        gb += sp.gb
        rgb += sp.rgb

    l = float(len(points))
    z = dist(z / l, s1)
    r = dist(r / l, s2)
    g = dist(g / l, s2)
    b = dist(b / l, s2)
    rg = dist(rg / l, s2)
    rb = dist(rb / l, s2)
    gb = dist(gb / l, s2)
    rgb = dist(rgb / l, s2)

    return Splat(z, r, g, b, rg, rb, gb, rgb)


def colour_range() -> Tuple[int, int]:
    """Return (min, span)."""
    n_min = int(random.random() * 255)
    n_max = int(random.random() * 255)
    if n_min > n_max:
        n_min, n_max = n_max, n_min
    return n_min, (n_max - n_min)


# ----------------------------
# Painting / scheme
# ----------------------------

ColourScheme = Callable[[Splat, float], str]


def vibrant_house_paint(m: Splat, r_scale: float) -> str:
    """Original colour scheme port (RGB derived from coupled channels)."""
    rg = m.rg
    rb = m.rb
    gb = m.gb

    # note: nMax* variables are "span", so add min like original
    c_r = col_str(int((zero_to_one(m.r + rg - rb - m.rgb, nCSpan * r_scale)) * nMaxR) + nMinR)
    c_g = col_str(int((zero_to_one(m.g - rg + gb - m.rgb, nCSpan * r_scale)) * nMaxG) + nMinG)
    c_b = col_str(int((zero_to_one(m.b + gb - rb - m.rgb, nCSpan * r_scale)) * nMaxB) + nMinB)

    return f"#{c_r}{c_g}{c_b}"


def draw_drip(x: int, y: int, m: Splat, r_scale: float, scheme: ColourScheme) -> None:
    colour = scheme(m, r_scale)

    # similar sizing behavior
    n_l = (nLow + 0.0) * r_scale / 3.0
    x1 = dist(x, n_l * nSplatterSize)
    y1 = dist(y, n_l * nSplatterSize)
    l2 = dist(n_l, n_l)

    canvas.create_oval(x1, y1, x1 + l2, y1 + l2, fill=colour, width=0)
    canvas.create_rectangle(x1, y1, x1 + l2 / 2.0, y1 + l2 / 2.0, fill=colour, width=0)
    canvas.update_idletasks()


# ----------------------------
# Fractal recursion
# ----------------------------

def frac_down(
    grid: Dict[str, Splat],
    x1: int, y1: int, x2: int, y2: int,
    tl: Splat, tr: Splat, bl: Splat, br: Splat,
    lim: float,
    rec: int,
    scheme: ColourScheme,
) -> None:
    dx = x2 - x1
    dy = y2 - y1

    # guard if recursion index exceeds arrays
    idx = rec if rec < len(aScale) else (len(aScale) - 1)
    idxc = rec if rec < len(aColour) else (len(aColour) - 1)

    s = aScale[idx]
    sc = aColour[idxc]

    t = odist([tl, tr], s * nHorizFactor, sc)
    l = odist([tl, bl], s, sc)
    r = odist([tr, br], s, sc)
    b = odist([bl, br], s * nHorizFactor, sc)
    m = odist([tl, tr, bl, br], s * nDiagFactor, sc)

    xm = mid(x1, x2)
    ym = mid(y1, y2)

    tl = load(grid, x1, y2, tl)
    tr = load(grid, x2, y2, tr)
    bl = load(grid, x1, y1, bl)
    br = load(grid, x2, y1, br)

    if dx <= nLow and dy <= nLow:
        # keep the same "paint if" idea
        if zero_to_one(m.z, nMSpan * math.sqrt(rec)) > lim:
            draw_drip(xm, ym, m, math.sqrt(rec), scheme)
        return

    tasks = [
        (grid, x1, ym, xm, y2, tl, t,  l,  m,  lim, rec + 1, scheme),
        (grid, xm, ym, x2, y2, t,  tr, m,  r,  lim, rec + 1, scheme),
        (grid, x1, y1, xm, ym, l,  m,  bl, b,  lim, rec + 1, scheme),
        (grid, xm, y1, x2, ym, m,  r,  b,  br, lim, rec + 1, scheme),
    ]
    random.shuffle(tasks)

    for args in tasks:
        frac_down(*args)


def frac(lim: float, scheme: ColourScheme) -> None:
    grid: Dict[str, Splat] = {}

    z0 = Splat(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    frac_down(grid, 0, 0, W - 1, H - 1, z0, z0, z0, z0, lim, 1, scheme)


# ----------------------------
# Main
# ----------------------------

def main() -> None:
    global canvas, nHorizFactor, nDiagFactor
    global nMinR, nMaxR, nMinG, nMaxG, nMinB, nMaxB

    random.seed()

    root = tk.Tk()
    root.title("Fractal Splatter (Python 3.13)")

    canvas = tk.Canvas(root, width=W, height=H)
    canvas.pack(side=tk.TOP)

    canvas.create_rectangle(0, 0, W, H, fill="gray", width=0)

    nHorizFactor = (W + 0.0) / (H + 0.0)
    nDiagFactor = math.sqrt(H**2 + W**2) / (H + 0.0)

    nMinR, nMaxR = colour_range()
    nMinG, nMaxG = colour_range()
    nMinB, nMaxB = colour_range()

    frac(nCover, vibrant_house_paint)

    print("done")

    root.mainloop()


if __name__ == "__main__":
    main()
