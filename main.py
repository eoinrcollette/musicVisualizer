from audio_processor import AudioProcessor
from ai_model import VisualizerAI
from visualizer import Visualizer
import pygame

def main():
    # Create the three parts
    audio_processor = AudioProcessor()
    ai_model = VisualizerAI()
    visualizer = Visualizer()
    
    # Settings
    audio_file = "sample_song.wav"#enter song file here 
    chunk_size = 1024
    
    try:
        # Load song and teach AI
        audio_processor.load_audio(audio_file)
        ai_model.train(audio_processor)
        
        # Start playing music
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        
        # Main loop
        running = True
        audio_pos = 0
        
        while running:
            
            # Check if user wants to quit
            running = visualizer.handle_events()
            
            # Get current audio
            current_chunk = audio_processor.get_audio_chunk(audio_pos, chunk_size)
            
            features = audio_processor.extract_simple_features(current_chunk)
            
            if current_chunk is not None:
                visual_params = ai_model.predict_visuals(features)
                
                # Update sphere
                visualizer.update_visuals(visual_params)
                audio_pos += chunk_size // 4
            else:
                # Song ended, start over
                audio_pos = 0
                pygame.mixer.music.play()
            
            # Draw sphere
            visualizer.draw_frame()
            visualizer.clock.tick(30)  # 30 FPS
            
    except FileNotFoundError:
        print(f"Audio file '{audio_file}' not found!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        visualizer.cleanup()

if __name__ == "__main__":
    main()