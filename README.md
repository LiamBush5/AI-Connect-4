# Connect 4 Game with AI

## Overview

This project is a web-based implementation of the classic Connect 4 game, featuring an AI opponent. The game allows two players to take turns dropping pieces into a vertical grid, with the objective of connecting four pieces in a row, either horizontally, vertically, or diagonally. The AI opponent uses the negamax algorithm with alpha-beta pruning for efficient move selection.

## Features

- Play against an AI opponent
- Option for AI to make the first move
- Real-time game status updates
- Simple and intuitive user interface

## Technologies Used

- **Frontend**: React, Axios
- **Backend**: Flask, Flask-CORS
- **AI**: Python, NumPy

## Setup Instructions

### Prerequisites

- Python 3.x
- Node.js and npm

### Backend Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/connect4.git
    cd connect4/backend
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask server:

    ```bash
    python app.py
    ```

### Frontend Setup

1. Navigate to the `frontend` directory:

    ```bash
    cd ../frontend
    ```

2. Install the required packages:

    ```bash
    npm install
    ```

3. Start the React development server:

    ```bash
    npm start
    ```

## File Structure

```
connect4/
├── backend/
│   ├── ai.py
│   ├── app.py
│   ├── connect4.py
│   └── requirements.txt
└── frontend/
    ├── public/
    │   ├── favicon.ico
    │   ├── index.html
    │   ├── logo192.png
    │   ├── logo512.png
    │   ├── manifest.json
    │   └── robots.txt
    ├── src/
    │   ├── App.css
    │   ├── App.js
    │   ├── App.test.js
    │   ├── index.css
    │   ├── index.js
    │   ├── logo.svg
    │   ├── reportWebVitals.js
    │   └── setupTests.js
    ├── package.json
    ├── package-lock.json
    └── README.md
```

## Usage

### Starting the Game

1. Open your browser and navigate to `http://localhost:3000`.
2. Click the "Start Game" button to begin a new game.
3. Optionally, check the "AI First Move" checkbox if you want the AI to make the first move.
4. Click on a column to drop your piece. The game will alternate turns between you and the AI.

### Ending the Game

1. Click the "End Game" button to reset the game at any time.

## Troubleshooting

If you encounter issues with the AI not making a move when the "AI First Move" option is selected, ensure that the `startGame` function in `App.js` is correctly implemented to handle the AI's first move.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
