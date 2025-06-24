# 🧙 Mark's Pixel RPG

A top-down 2D RPG game built with Python and Pygame. Explore a small pixel-art village with buildings, walls, and a controllable character. This is a foundational step in creating a full RPG adventure.

---

## 🎮 Features

- Pixel-art player character with directional movement (WASD / Arrow Keys)
- Grass, wall, and building tiles drawn from real pixel assets
- Basic collision detection for walls and large buildings
- Buildings placed manually to form a village layout
- Scalable tile system using a grid-based map

---

## 🗺️ Map System

The map is a 2D list grid of tile types:
- `0` = Grass  
- `1` = Wall  
- Buildings are drawn as image objects, not bound to tile data directly.

---

## 🧑‍💻 How to Run

1. **Install Python** (preferably Python 3.11+)
2. **Install Pygame**:
   ```bash
   pip install pygame

## Folder Structure

rpg-game/
├── main.py
├── map.py
├── player.py
├── assets/
│   ├── grass.png
│   ├── wall.png
│   ├── player.png
│   ├── building1.png
│   ├── building2.png
│   ├── building3.png
├── README.md
