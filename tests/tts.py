import math
import wave
import struct

def generate_frequency(frequency, duration, volume=1, sample_rate=44100):
    num_samples = int(sample_rate * duration)
    factor = float(frequency) * (math.pi * 2) / sample_rate
    samples = [math.sin(x * factor) for x in range(num_samples)]
    return samples

def save_wave_file(file_name, samples, sample_rate=44100, sample_width=2):
    wave_file = wave.open(file_name, 'w')
    wave_file.setparams((1, sample_width, sample_rate, len(samples), 'NONE', 'not compressed'))
    for sample in samples:
        wave_file.writeframes(struct.pack('h', int(sample * 32767.0)))
    wave_file.close()

def text_to_speech(text, file_name):
    # تبدیل متن به لیستی از کلمات
    words = text.split()

    # تولید فایل صوتی برای هر کلمه در متن
    for word in words:
        # تولید فرکانس مشخص برای هر کلمه
        frequency = len(word) * 50
        duration = 0.5

        # تولید نمونه‌های صوتی با استفاده از تابع generate_frequency
        samples = generate_frequency(frequency, duration)

        # ذخیره فایل صوتی با استفاده از تابع save_wave_file
        save_wave_file(f"{word}.wav", samples)

    # ترکیب فایل‌های صوتی کلمات به یک فایل صوتی کامل
    full_samples = []
    for word in words:
        with wave.open(f"{word}.wav", 'r') as wave_file:
            full_samples.extend(list(struct.unpack('h', wave_file.readframes(wave_file.getnframes()))))
    save_wave_file(file_name, full_samples)

text_to_speech("Hello world", "hello_world.wav")