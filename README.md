# 🎮 Pong Game

A modern, polished two-player Pong implementation with smooth gameplay, scoring system, and clean UI. Built with Python and PyGame.


## ✨ Features

- 🎯 **Two-player competitive gameplay** - Perfect for local multiplayer
- 📊 **Real-time scoring** - Track scores with visual indicators
- 🎨 **Modern UI** - Clean visuals with color-coded players
- ⚡ **Smooth physics** - Ball speed increases with hits for escalating tension
- 🎮 **Complete game flow** - Start screen → Gameplay → Victory screen
- 🛠️ **Easy customization** - Modify game parameters in one place

## 🚀 Installation & Setup

### Prerequisites
```bash
# Install Python 3.7 or higher from python.org
# Verify installation
python --version
```

### Install Dependencies
```bash
# Install PyGame
pip install pygame


### Run the Game
```bash
python pong.py
```

## 🎮 Gameplay

### Controls
| Player | Up | Down | Action |
|--------|----|------|--------|
| **Player 1** (Blue) | `W` Key | `S` Key | Left paddle |
| **Player 2** (Red) | `↑` Arrow | `↓` Arrow | Right paddle |
| **Game Controls** | `SPACE` Start | `R` Restart | `Q` Quit |

### Rules
- **Objective**: Deflect the ball past your opponent
- **Scoring**: Ball passing left/right side = point for opponent
- **Victory**: First to reach 5 points wins
- **Physics**: Ball speed increases slightly with each paddle hit

## 🛠️ Configuration

Easily customize game settings by modifying these constants in `pong.py`:

```python
# Display
SCREEN_WIDTH = 960    # Window width
SCREEN_HEIGHT = 720   # Window height

# Gameplay
winning_score = 5     # Points to win (increase for longer matches)
paddle_speed = 0.5    # Paddle movement speed
initial_ball_speed = 0.3  # Starting ball speed

# Visuals
PADDLE_COLORS = {
    "player1": (50, 150, 255),   # Blue
    "player2": (255, 50, 50)     # Red
}
```

## 🎨 Features Breakdown

### **Game States**
1. **Start Screen** - Instructions and controls
2. **Active Gameplay** - Real-time paddle and ball movement
3. **Game Over** - Winner announcement with restart options

### **Physics & Logic**
- Frame-rate independent movement (60 FPS)
- Collision detection with paddle edges
- Ball angle variation based on hit position
- Boundary checking with bounce physics

### **Visual Polish**
- Dashed center line for court separation
- Large, clear score display
- Color-coded player identification
- Smooth animations and transitions

