import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

const ROWS = 6;
const COLUMNS = 7;

function App() {
  const [board, setBoard] = useState(Array.from({ length: ROWS }, () => Array(COLUMNS).fill(0)));
  const [message, setMessage] = useState('');
  const [gameStarted, setGameStarted] = useState(false);
  const [playerTurn, setPlayerTurn] = useState(true);
  const [aiFirstMove, setAiFirstMove] = useState(false);

  const makeMove = async (col) => {
    if (!gameStarted || !playerTurn || message.includes('wins!')) {
      return;
    }

    try {
      const response = await axios.post('http://127.0.0.1:5000/move', { column: col, piece: 1 });
      if (response.data.status === 'success') {
        const newBoard = [...board];
        for (let row = ROWS - 1; row >= 0; row--) {
          if (newBoard[row][col] === 0) {
            newBoard[row][col] = 1;
            break;
          }
        }
        setBoard(newBoard);

        // Check for winning condition
        const winResponse = await axios.post('http://127.0.0.1:5000/check-win', { piece: 1 });
        if (winResponse.data.status === 'win') {
          setMessage('Player wins!');
          setGameStarted(false);
        } else {
          setPlayerTurn(false);
          setTimeout(aiMove, 500);
        }
      } else {
        setMessage('Invalid move, try again.');
      }
    } catch (error) {
      console.error('Error making move:', error);
    }
  };

  const aiMove = async () => {
    if (!gameStarted) {
      return;
    }

    try {
      const response = await axios.post('http://127.0.0.1:5000/ai-move', { piece: 2 });
      if (response.data.status === 'success') {
        const newBoard = [...board];
        const col = response.data.column;
        for (let row = ROWS - 1; row >= 0; row--) {
          if (newBoard[row][col] === 0) {
            newBoard[row][col] = 2;
            break;
          }
        }
        setBoard(newBoard);

        // Check for winning condition
        const winResponse = await axios.post('http://127.0.0.1:5000/check-win', { piece: 2 });
        if (winResponse.data.status === 'win') {
          setMessage('AI wins!');
          setGameStarted(false);
        } else {
          setPlayerTurn(true);
        }
      } else {
        setMessage('Invalid move, try again.');
      }
    } catch (error) {
      console.error('Error making AI move:', error);
    }
  };

  const startGame = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/reset');
      if (response.data.status === 'success') {
        setBoard(Array.from({ length: ROWS }, () => Array(COLUMNS).fill(0)));
        setMessage('');
        setGameStarted(true);
        setPlayerTurn(!aiFirstMove);

        if (aiFirstMove) {
          setTimeout(aiMove, 500);
        }
      } else {
        setMessage('Failed to reset the game.');
      }
    } catch (error) {
      console.error('Error resetting the game:', error);
    }
  };

  const endGame = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/reset');
      if (response.data.status === 'success') {
        setBoard(Array.from({ length: ROWS }, () => Array(COLUMNS).fill(0)));
        setMessage('');
        setGameStarted(false);
        setPlayerTurn(true);
      } else {
        setMessage('Failed to reset the game.');
      }
    } catch (error) {
      console.error('Error resetting the game:', error);
    }
  };

  return (
    <div className="app">
      <header className="header">
        <h1 className="title">Connect 4</h1>
      </header>
      <div className="message">{message}</div>
      {!gameStarted && (
        <div className="controls">
          <button className="start-btn" onClick={startGame}>
            Start Game
          </button>
          <div className="ai-first-move">
            <label>
              <input
                type="checkbox"
                checked={aiFirstMove}
                onChange={(e) => setAiFirstMove(e.target.checked)}
              />
              AI First Move
            </label>
          </div>
        </div>
      )}
      {gameStarted && (
        <div className="controls">
          <button className="end-btn" onClick={endGame}>
            End Game
          </button>
        </div>
      )}
      <div className="board">
        {board.map((row, rowIndex) => (
          <div key={rowIndex} className="row">
            {row.map((cell, colIndex) => (
              <div
                key={colIndex}
                className={`cell player${cell}`}
                onClick={() => makeMove(colIndex)}
              />
            ))}
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;