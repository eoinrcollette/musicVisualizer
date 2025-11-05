import numpy as np
import librosa

class AudioProcessor:
    def __init__(self):
        self.audio_data = None
        self.sr = None
    
    def load_audio(self, file_path, duration=30):
        # Load song into memory
        print(f"Loading audio: {file_path}")
        self.audio_data, self.sr = librosa.load(file_path, duration=duration)
        print(f"Audio loaded: {len(self.audio_data)} samples at {self.sr} Hz")
        return self.audio_data, self.sr
    
    def extract_simple_features(self, audio_chunk):
    # Get bass, mid, treble from audio
        if len(audio_chunk) < 1024:
         return np.array([0.5, 0.5, 0.5])
        
    # Convert audio to frequencies
        fft = np.fft.fft(audio_chunk)
        magnitude = np.abs(fft[:len(fft)//2])
    
    # Split into 3 parts: low, mid, high frequencies
        third = len(magnitude) // 3
        bass = np.mean(magnitude[:third])
        mid = np.mean(magnitude[third:2*third])  
        treble = np.mean(magnitude[2*third:])
    
    # Normalize to 0-1 range using the raw values
    # These raw values look good: bass~9, mid~1.7, treble~0.36
        bass = min(bass / 20, 1.0)
        mid = min(mid / 5, 1.0) 
        treble = min(treble / 2, 1.0)
    
    
        return np.array([bass, mid, treble])


    def get_audio_chunk(self, position, chunk_size=1024):
        # Get a small piece of the song
        if self.audio_data is None or position + chunk_size >= len(self.audio_data):
            return None
        return self.audio_data[position:position + chunk_size]