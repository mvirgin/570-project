Project for cos570 - A.I.

Uses openAI Gym to train a flappy bird bot

more details to come.

visual studio 2019 - need at least Microsoft Visual C++ for the flappy-bird-gym environment (2019 works, unsure about 2022 but here's a link: https://visualstudio.microsoft.com/visual-cpp-build-tools/ )
Need python 3.6-3.9 (3.9.11 confirmed works on two machines)
pip install --upgrade setuptools
pip install gym
pip install flappy-bird-gym
if you want to be able to play the game yourself and not just watch the computer do it, you'll need to
navigate to the lib\site-packages folder that pip installed flappy-bird-gym to and change original_game.py
from 

ASSETS_DIR = "./flappy_bird_gym/assets"

to

import os
from pathlib import Path
_BASE_DIR = Path(os.path.dirname(os.path.realpath(__file__))).parent
ASSETS_DIR = str(_BASE_DIR / "flappy_bird_gym/assets")

(above solution provided in issues section of https://github.com/Talendar/flappy-bird-gym/issues/3 by prabathbr)

Type flappy_bird_gym into the command prompt to play

NN assignment changed numpy to a newer version - pip warns me of incompatability but everything still seems to work
fine

Bird in randTest.py should flap up and down randomly, with a preference for not
flapping to prevent flying off the screen immediately

Added a requirements.txt file to make installing dependencies easy