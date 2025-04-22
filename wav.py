import math
import wave
import array

# Configuration
duration = 3         # seconds
frequency = 440      # Hz (frequency of the sine wave)
volume = 100         # percent (0 to 100)
sample_rate = 44100  # samples per second
num_channels = 1     # mono
bit_depth = 16       # 16-bit audio

def generate_sine_wave(filename: str, duration: int, frequency: int, volume: int):
    num_samples = sample_rate * duration
    data = array.array('h')  # signed 16-bit integers

    amplitude = int(32767 * volume / 100)
    num_samples_per_cycle = sample_rate / frequency

    for i in range(num_samples):
        sample = amplitude * math.sin(2 * math.pi * (i % num_samples_per_cycle) / num_samples_per_cycle)
        data.append(int(sample))

    with wave.open(filename, 'w') as f:
        f.setparams((num_channels, bit_depth // 8, sample_rate, num_samples, "NONE", "Uncompressed"))
        f.writeframes(data.tobytes())

    print(f"Sine wave file '{filename}' generated: {duration}s at {frequency}Hz, volume {volume}%.")

# Run generator
output_filename = f"SineWave_{frequency}Hz.wav"
generate_sine_wave(output_filename, duration, frequency, volume)
