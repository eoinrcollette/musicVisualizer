import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler

class VisualizerAI:
    def __init__(self):
        self.model = MLPRegressor(hidden_layer_sizes=(20, 10), max_iter=500, learning_rate_init= .01, activation= 'relu')
        self.scaler = StandardScaler()
        self.is_trained = False
    
    def create_training_data(self, audio_processor):
        # Teach AI using the whole song
        if audio_processor.audio_data is None:
            raise ValueError("No audio data loaded!")
        
        audio_length = len(audio_processor.audio_data)
        
        chunk_size = 1024
        features_list = []
        targets_list = []
        
        print("Creating training data...")
        
        # Go through entire song
        for i in range(0, len(audio_processor.audio_data) - chunk_size, chunk_size):
            chunk = audio_processor.audio_data[i:i+chunk_size]
            features = audio_processor.extract_simple_features(chunk)
            
            # Tell AI what visuals should look like
            bass, mid, treble = features
            
            # Rules: bass=red, mid=green, treble=blue
            red = 200+ int(bass * 255)      
            green = 200 +int(mid * 255)      
            blue = 200 + int(treble * 255)    
            bass_size = 20 + int(bass * 60) 
            mid_size = 20 + int(mid * 60) 
            treble_size = 20 + int(treble * 60) 
            bass_x_pos = 200 
            mid_x_pos = 400
            treble_x_pos = 600
            bass_y_pos = 200 + int(bass * 350)
            mid_y_pos = 200 + int(mid * 200)
            treble_y_pos = 200 + int(treble * 500)
            
            targets = [red, green, blue, bass_size, mid_size, treble_size, bass_x_pos, mid_x_pos, treble_x_pos, bass_y_pos, mid_y_pos, treble_y_pos]
            
            features_list.append(features)
            targets_list.append(targets)
            print(f"Bass: {bass:.3f}, Mid: {mid:.3f}, Treble: {treble:.3f}")
        return np.array(features_list), np.array(targets_list)
    
    def train(self, audio_processor):
        # Train the AI
        X, y = self.create_training_data(audio_processor)
        
        print("Training AI model...")
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)
        self.is_trained = True
        print("Model trained successfully!")
    
    def predict_visuals(self, features):
        # Ask AI what the sphere should look like
        if not self.is_trained:
            raise ValueError("Model not trained yet!")
        
        features_scaled = self.scaler.transform([features])
        prediction = self.model.predict(features_scaled)[0]
        
        # Return sphere properties
        return {
            
            'bass_size': max(10, min(100, int(prediction[3]))),
            'mid_size': max(10, min(100, int(prediction[4]))),
            'treble_size': max(10, min(100, int(prediction[5]))),
            'bass_color': [
                max(100, min(255, int(prediction[0]))),  # Red
                max(0, min(255, 0)),
                max(0, min(255, 0))
            ],
            
            'mid_color':[
                 max(0, min(255, 0)), #Red
                 max(0, min(255, int(prediction[1]))), # Green
                 max(0, min(255, 0)) #Blue
            ] ,
            
            'treble_color': [
                max(0, min(255, 0)),
                max(0, min(255, 0)),
                max(100, min(255, int(prediction[2])))   
            ],
            
            'bass_position': [
                200,  # X
                max(50, min(550, int(prediction[9])))   # Y
            ],
            'mid_position': [
                400,  # X
                max(50, min(550, int(prediction[10])))   # Y
            ],
            'treble_position': [
                600,  # X
                max(50, min(550, int(prediction[11])))   # Y
            ]
        }