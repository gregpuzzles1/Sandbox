# Random Sound FX Using WAV File
# Updated version of http://code.activestate.com/recipes/578180/
import math
import wave
import array
import random

# Configuration
duration = 5  # seconds
volume = 100  # percent
sample_rate = 44100  # samples per second
num_channels = 1  # mono
sample_width = 2  # bytes per sample (16-bit)
num_samples = sample_rate * duration

# Random parameters for modulation
freq_carrier = random.randint(500, 3000)
freq_am = random.randint(1, 10)
freq_fm = random.randint(1, 10)
freq_fm_deviation = random.randint(100, 400)

phase_carrier = random.random() * math.pi * 2
phase_am = random.random() * math.pi * 2
phase_fm = random.random() * math.pi * 2

# Number of samples per cycle for each modulation type
samples_per_cycle_carrier = sample_rate / freq_carrier
samples_per_cycle_am = sample_rate / freq_am
samples_per_cycle_fm = sample_rate / freq_fm

# Prepare audio data
audio_data = array.array('h')  # 16-bit signed integers

for i in range(num_samples):
    amplitude = 32767 * volume / 100.0

    t_carrier = 2 * math.pi * (i % samples_per_cycle_carrier) / samples_per_cycle_carrier + phase_carrier
    t_fm = 2 * math.pi * (i % samples_per_cycle_fm) / samples_per_cycle_fm + phase_fm
    t_am = 2 * math.pi * (i % samples_per_cycle_am) / samples_per_cycle_am + phase_am

    modulated = math.sin(t_carrier + math.sin(t_fm) * freq_fm_deviation / freq_fm)
    modulated *= (math.sin(t_am) + 1) / 2

    audio_data.append(int(amplitude * modulated))

# Write to WAV file using context manager
output_filename = 'RandomSoundFX.wav'
with wave.open(output_filename, 'w') as wav_file:
    wav_file.setparams((num_channels, sample_width, sample_rate, num_samples, "NONE", "Uncompressed"))
    wav_file.writeframes(audio_data.tobytes())

print(f"WAV file '{output_filename}' has been created successfully.")
