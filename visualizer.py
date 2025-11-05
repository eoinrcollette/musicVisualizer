import pygame
import sys

class Visualizer:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("AI Music Visualizer")
        self.clock = pygame.time.Clock()
        self.width = width
        self.height = height
        
        # Colors
        self.BLACK = (0, 0, 0)
        
        # Default sphere
        self.bass_visuals = {
            'color': [255, 0, 0],
            'size': 50,
            'position': [200, 300]
        }
        
        self.mid_visuals = {
            'color': [0, 255, 0],
            'size': 50,
            'position': [400, 300]
        }
        
        self.treble_visuals = {
            'color': [0, 0, 255],
            'size': 50,
            'position': [600, 300]
        }
    
    def update_visuals(self, visual_params):
        self.bass_visuals = {
        'color': visual_params['bass_color'],
        'size': visual_params['bass_size'],
        'position': visual_params['bass_position']
        }
        
        self.mid_visuals = {
        'color': visual_params['mid_color'],
        'size': visual_params['mid_size'],
        'position': visual_params['mid_position']
        }
        
        self.treble_visuals = {
        'color': visual_params['treble_color'],
        'size': visual_params['treble_size'],
        'position': visual_params['treble_position']
        }
    def draw_frame(self):

        self.screen.fill(self.BLACK)
    
        bass_color = self.bass_visuals['color']
        bass_size = self.bass_visuals['size']
        bass_pos = self.bass_visuals['position']
        
        mid_color = self.mid_visuals['color']
        mid_size = self.mid_visuals['size']
        mid_pos = self.mid_visuals['position']
        
        treble_color = self.treble_visuals['color']
        treble_size = self.treble_visuals['size']
        treble_pos = self.treble_visuals['position']
    
        # Draw the AI-controlled sphere
        pygame.draw.circle(self.screen, bass_color, bass_pos, bass_size)
        pygame.draw.circle(self.screen, mid_color, mid_pos, mid_size)
        pygame.draw.circle(self.screen, treble_color, treble_pos, treble_size)
    
        # Show it
        pygame.display.flip()
        
    def handle_events(self):
        # Check if user wants to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        return True
    
    def cleanup(self):
        # Close everything
        pygame.quit()
        sys.exit()