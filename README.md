# ⚽ Football Manager Simulation Game ⚽

## 📋 Overview 📋

This is a simple Python-based simulation of a football (soccer) manager game. The focus is on simulating matches between two teams, where player skills, positions, and random events all contribute to the match outcome.

🌟 Key Features:

- 👥 Simple player attributes for goalkeepers, forwards, midfielders, and defenders.
- 🏟 Simulated match events including successful passes, shots, saves, and tackles.
- 🌠 Inclusion of star players like Messi and Ronaldo with manually set high skill levels.
- 🎲 Randomization for unpredictable outcomes.

## 💻 How to Run 💻

1️⃣ Clone this repository to your local machine.  
2️⃣ Open a terminal and navigate to the project directory.  
3️⃣ Run `python main.py`.

## 📚 Code Structure 📚

- `Player`: A class to represent individual players. Each player has a `name`, `position`, and `skill` level.
- `Team`: A class to represent a football team, consisting of different players in various positions.
- `battle`: The main function that simulates the match between two teams.

## 🛠 Dependencies 🛠

- Python 3.x

## 🎮 Examples 🎮

```
Match: Barcelona vs Juventus

Minute 1:
Messi from Barcelona shoots! 🥅
Ter Stegen from Barcelona makes a save! 🧤

... (snip) ...

Minute 90:
Ronaldo from Juventus shoots! 🥅
Goal!!! 🎉

Final Score: Barcelona 2 - 3 Juventus 🏆
```

## 🔧 Customization 🔧

You can modify player skills and team compositions to simulate different types of matches.

## 🤝 Contributing 🤝

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License 📄

This project is licensed under the MIT License.