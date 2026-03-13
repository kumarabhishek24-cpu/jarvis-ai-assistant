import pvporcupine
import pyaudio
import struct
import subprocess

ACCESS_KEY = "PASTE_YOUR_PICOVOICE_KEY"

porcupine = pvporcupine.create(
    access_key="QwcDb6NisSYtslwvYIzfWcR4J7r+oIgP76a2mjZ5R44IBzEoCjHaqQ==",
    keywords=["jarvis"]
)

pa = pyaudio.PyAudio()

audio_stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length
)

print("Jarvis background wake system running...")

while True:
    pcm = audio_stream.read(porcupine.frame_length)
    pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

    keyword_index = porcupine.process(pcm)

    if keyword_index >= 0:
        print("Jarvis Wake Word Detected")

        subprocess.Popen(
            ["python", "C:\\Users\\HP\\jarvis\\main.py"]
        )