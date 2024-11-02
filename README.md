# Chess Engine

## Overview

Chess - Play with other Python Chess Engine in Playing against AI. This is full-featured chess game with levels of difficulty governed by different algorithms and a custom UI created through Pygame.

## Features

- **Pygame**: A dynamic visual interface built using a train environment for interactive UI.
- **AI Opponent**: Select between several AI algorithms, ranging from basic to sophisticated.
- **Flexible Code**: The modular system lends itself well to the addition of new features or enhancement of current functionality.


## File Structure

### 1. `chessMain.py`

**Type**: Driver - main file that initializes and connects all components of the chess game

**Core Responsibilities**:
- **Init Game**: Initiates the chessboard with a Pygame display window, loads all images, initiates player settings (black or white play by yourself)
- **Input**: Handle user input (mouse clicks) on which pieces to get selected and where to move to It records what positions have been clicked, it highlights the selected piece, and it displays legal moves.
- **Display Management**: The Component that Refreshes the board, pieces and other UI components after every move It utilizes Pygame double buffering so that it refreshes the screen very smoothly and provides a seamless experience between frames.
- **Multithreading for AI Moves**: To avoid lag in gameplay by AI calculating its move on an independent thread/process. The asynchronous way of doing this makes sure that the player does not have to wait for the AI move to be computed before they can interact with the board.
- **Managing Event Loop**: It is the way how it maintains an infinite loop which looks for user actions, game status and calculations from AI.
- **Handling of Errors**: The system address or notifies with a filling red or an alert if any of the players do the moved illegally.
- **AI and Engine Interface**: Invokes the functions in chessEngine. Using chessAI to validate player moves and in chessAI. This has led to the input of a prompt responding to the text you wrote in some conversation script, as well as a Python script, ai. It enables the core script to play the role of a main orchestrator.


### 2. `chessEngine.py`

**Purpose**: An empty implementation for the main logic module which enforces the laws of chess, making sure that each piece's move adheres to the laws of chess, transitioning the board state from one to another.

**Core Responsibilities**:
- **Implementation Move Validation**: Holds function for every type of move for each chess piece (pawns, knights, bishops, etc.), to confirm that moves can be made, as well as confirming that a piece is not being moved into an invalid position according to chess rules.
- **Game State Management**: Keeps track of such game states as check, checkmate and stalemate and updates the state when a move causes one of these states. The keeping of track of these states are important in allowing the game to end when required conditions have been met.
- **Board Update and Undo**: Manages board updates following a move and tracks move history; Undoing a move (to a previous state of the board), is called using the undo function in the game by the players.
- **Special Move Handling**:
  - **Castling**: Checks and performs a castling if possible (moves both the king and rook).
  - **En Passant**: Enables pawns to capture en passant according to their most recent moves.
  - **Pawn Promotion**: Determine if a pawn has reached the opposite end of the board and enable it to be promoted to a queen, rook, bishop, or knight.

**Highlights**:
- **Optimized Data Structures**: It uses either an array or matrix for board representation, which replaces functions of direct access to the position of the pieces and allows efficient tests of validity.
- **Main File Connectivity**: Integrates well with chessMain.py to provide feedback for the current state of a game with possible moves, while keeping the continuity and real-time feel in gameplay.

### 3. `chessAI.py`

**Goal**: This module, which is supposed to generate moves through computer opponents by using different kinds of algorithms, offers a challenging experience in several levels of difficulty.

**Algorithms**:
- **Naive Algorithm**: It randomly selects one of the available moves. This would be appropriate for a naive player.
- **Greedy Algorithm**: It chooses the move with the most valuable piece at hand. It enables it to have a little more strategic gameplay but still simple.
- **Min-Max Algorithm**:
  - **Principle**: Uses a decision tree to evaluate all the possible moves-and-responses for a given level of depth, scoring it with outcomes that could happen.
  - **Evaluation**: There is an evaluation function that, depending on the piece value, center control, king safety, etc., gives a score for any given board position.
- **Alpha-Beta Pruning**: 
  - **Optimization of Min-Max**: This minimizes the number of nodes under consideration. That is, the moves need to be assessed. As such, it accelerates the algorithm by "pruning" moves that will not have any impact on the final decision.
  - **Depth**: This allows the tuning of depth to a higher or lower difficulty setting of AI to tailor a challenge according to a player's preference.

**Presentations**:
- **Modular Structure**: Allows adding or adjusting each AI strategy easily; thus, the scalable AI opponent.
- **Async Processing**: AI computations are designed to run concurrently with chessMain.py, keeping the game smooth while the AI is processing its moves.

### 4. `images/`

**Purpose**: House the game graphics, including high-resolution images for each chess piece. Have files in an orderly manner in a way that promotes easy access.

**Contents**:
- **Piece Images**: PNG files for each type of piece in both black and white, e.g. wp.png for white pawn, bQ.png for black queen.
- **Chessboard Background**: This is for any textures or background images for the board; this will make the game more visually attractive.

**Usage**:
- **Dynamic Loading**: These images are dynamically loaded by chessMain.py, which then places them according to the coordinates of each piece on the board.
- **Scaled and positioned pictures**: cite all graphics scaled according to the grid cells on the Pygame board so that pieces are sharp and visually matched against the board.
  
**Overview**:
- **Customizability**: The folder herein includes the images that can be replaced to provide the look for pieces or the board in terms of creating themes in chess.
- **Centralized Asset Management**: Store all images here. A separation, which makes sense in the project structure, means all visual materials are easy to reach for editing or improvement.

### 5. `requirements.txt`

**Purpose**: Enumerates the dependencies required for the project; this makes it compatible and easy to install for newbies. Specifies versions for libraries, which in this case are Pygame; hence, it is going to be very easy for one to install all that is needed to run everything smoothly.
**Highlights**: Helps create a consistent environment for development.

### 6. `README.md`

**Purpose**: Documenting the project file. Overview Description Installation Usage Contribute to this project. 
**Highlights**: This is fundamental for new users or contributors in understanding what it is all about and how to get started with the project.

## How to Play

1. Kicks off the process, launching chessMain.py and thereby initiating a game of chess.
2. The pieces in the game will be moved on the board through mouse clicks.
3. It is even possible to play against an artificial intelligence whose moves depend on the algorithm chosen.

## Pending Features

- Introduction to advanced AI techniques, Monte Carlo Tree Search and/or others.
- Multi-Player Mode: A mode where users can play against locals or online with their friends.
- UI Improvements: This will involve improved graphical design with a view to ensuring it is even more interactive.
