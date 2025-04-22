import pyaudio
import random

# Display basic user screen information
print("\n" * 20)
print("$VER: Noise_Generator.py_Version_0.00.10_(C)2012_B.Walker_G0LCU.\n")
print("A DEMO, beginner-level, simple white noise generator for modern systems.\n")
print("Works on macOS, Windows, Linux with Python 3.x and PyAudio.\n")
print("Ensure PyAudio is installed: pip install pyaudio\n")
print("This DEMO lasts for a few seconds. You can easily make it continuous.\n")
print("Issued as Public Domain, you may do with this code as you please.\n")
print("=" * 60)

# Setup PyAudio stream, mono, 8-bit audio, 22050 Hz sample rate
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt8, channels=1, rate=22050, output=True)

# Generate white noise for a specified duration
duration_seconds = 5  # Duration of noise playback
samples = 22050 * duration_seconds  # Total samples based on rate

print(f"\nGenerating white noise for {duration_seconds} seconds...\n")

for _ in range(samples):
    sample = random.randint(0, 255)  # 8-bit sample
    stream.write(bytes([sample]))

# Cleanup
stream.stop_stream()
stream.close()
p.terminate()

print("White noise generation complete. Goodbye!\n")
