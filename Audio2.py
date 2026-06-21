import threading
import sys
try:
    import pyaudio
    import numpy as np
    import matplotlib.pyplot as plt
    import speech_recognition as sr
    from speech_recognition import AudioData
except ImportError as e:
    print(f"Missing Library: {e.name}")
    print("\nInstall commands:")
    print("Windows: pip install pyaudio numpy matplotlib SpeechRecognition")
    print("MacOS: brew install portaudio && pip install pyaudio numpy matplotlib SpeechRecognition")
    sys.exit(1)

stop_event = threading.Event()

def wait_for_enter():
    input()
    stop_event.set()

def record_audio(label):
    stop_event.clear()
    p=pyaudio.PyAudio()
    stream=p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    frames = []
    print(f"\n🎤 Recording {label}... Press Enter to stop.")
    threading.Thread(target=wait_for_enter, daemon=True).start()
    while not stop_event.is_set():
        data=stream.read(1024, exception_on_overflow=False)
        frames.append(data)
        print(".", end='', flush=True)
    print("Compleated")
    stream.stop_stream()
    stream.close()
    width = p.get_sample_size(pyaudio.paInt16)
    p.terminate()
    return b''.join(frames), 16000, width

def analyze_audio(data,rate):
    samples = np.frombuffer(data, dtype=np.int16)
    return {"duration": len(samples)/rate,
            "avg_volume": np.mean(np.abs(samples)), 
            "max_volume": np.max(np.abs(samples)),
            "samples": samples}

def transcribe(data, rate, width):
    recognizer = sr.Recognizer()
    try:
        audio = AudioData(data, rate, width)
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "❌ Could not understand audio"
    
def display_stats(stats, text, label):
    print("\n"+"-"*40)
    print(f"📊 {label}")
    print("-"*40)
    print(f"Duration:       {stats['duration']:.2f} seconds")
    print(f"Average Volume: {stats['avg_volume']:.2f}")
    print(f"Max Volume:     {stats['max_volume']:.2f}")
    print(f"Transcription:  {text}")

def compare(stats1, stats2):
    print("\n"+"="*40)
    print("📈 Comparison")
    print("="*40)
    if stats1['duration'] > stats2['duration']:
        longer = "Audio 1"
        if stats2["duration"] != 0:
            diff = (stats1['duration'] - stats2['duration']) / stats2['duration'] * 100
        else:
            diff=0
    else:
        longer = "Audio 2"
        if stats1["duration"] != 0:
            diff = (stats2['duration'] - stats1['duration']) / stats1['duration'] * 100
        else:
            diff=0
    print(f"Longer Duration: {longer} ({diff:.1f}% longer)")
    if stats1['avg_volume'] > stats2['avg_volume']:
        louder = "Audio 1"
        if stats2["avg_volume"] != 0:
            diff = (stats1['avg_volume'] - stats2['avg_volume']) / stats2['avg_volume'] * 100
        else:
            diff=0
    else:
        louder = "Audio 2"
        if stats1["avg_volume"] != 0:
            diff = (stats2['avg_volume'] - stats1['avg_volume']) / stats1['avg_volume'] * 100
        else:
            diff=0
    print(f"Louder Average Volume: {louder} ({diff:.1f}% louder)")

def plot_both(stats1,stats2,rate):
    fig, (ax1,ax2) = plt.subplots(2,1, figsize=(12,6))
    t1=np.linspace(0, len(stats1["samples"])/rate, len(stats1["samples"]))
    ax1.plot(t1, stats1["samples"], linewidth=0.5)
    ax1.set_title(f"Recording 1 (Normal)- Duration: {stats1['duration']:.2f}s, Avg Vol: {stats1['avg_volume']:.0f}")
    ax1.set_ylabel("Amplitude")
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(-35000, 35000)

    t2=np.linspace(0, len(stats2["samples"])/rate, len(stats2["samples"]))
    ax2.plot(t2, stats2["samples"], color='orange', linewidth=0.5)
    ax2.set_title(f"Recording 2 (Loud) - Duration: {stats2['duration']:.2f}s, Avg Vol: {stats2['avg_volume']:.0f}")
    ax2.set_xlabel("Time (seconds)")
    ax2.set_ylabel("Amplitude")  
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim(-35000, 35000)
    plt.tight_layout()
    plt.show()

def main():
    print("="*40)
    print("🎧 Audio Comparison Tool")
    
    print("="*40)
    print("Record twice and compare your voice")
    data1, rate1, width1 = record_audio("Normal")
    stats1 = analyze_audio(data1, rate1)
    text1 = transcribe(data1, rate1, width1)
    display_stats(stats1, text1, "Recording 1 (Normal)")

    input("\n Press Enter then speak louder or faster")
    data2, rate2, width2 = record_audio("Loud")
    stats2 = analyze_audio(data2, rate2)
    text2 = transcribe(data2, rate2, width2)
    display_stats(stats2, text2, "Recording 2 (Loud)")

    compare(stats1, stats2)
    plot_both(stats1, stats2, rate1)

if __name__ == "__main__":
    main()