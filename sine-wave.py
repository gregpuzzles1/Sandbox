import math
from itertools import count
from typing import Generator


def sine_wave(frequency: float = 440.0, framerate: int = 44100, amplitude: float = 0.5) -> Generator[float, None, None]:
    """
    Generate a sine wave with a given frequency, framerate, and amplitude.
    
    :param frequency: Frequency of the sine wave in Hz.
    :param framerate: Number of samples per second (default 44100).
    :param amplitude: Amplitude of the wave (0.0 to 1.0).
    :return: Infinite generator of sine wave samples.
    """
    amplitude = max(0.0, min(1.0, amplitude))  # Clamp amplitude between 0.0 and 1.0
    period = framerate / frequency
    lookup_table = [amplitude * math.sin(2.0 * math.pi * frequency * (i / framerate)) for i in range(int(period))]

    for i in count(0):
        yield lookup_table[i % len(lookup_table)]


# Example usage (optional):
if __name__ == "__main__":
    wave_gen = sine_wave(frequency=440.0, framerate=44100, amplitude=0.5)
    for _ in range(10):
        print(next(wave_gen))
