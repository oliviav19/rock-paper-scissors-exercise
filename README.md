# rock-paper-scissors-exercise

This repo contains a basic command-line game of rock-paper-scissors-shoot! 

## Installation
Clone or download this repo onto your local computer.
Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

cd rock-paper-scissors-exercise

## Setup
Setup a virtual environment (if you like that kind of thing):

conda create -n my-game-env python=3.8
conda activate my-game-env

Install the required packages:

pip install -r requirements.txt

## Configuring Environment Variables
Add a new ".env" file to the root directory of this repo, and place contents, such as your desired user name inside, like the following inside:

PLAYER_NAME="Olivia"

## Usage
Run the game:

python game.py
