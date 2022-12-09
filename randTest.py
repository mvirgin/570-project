import time
import numpy as np
import flappy_bird_gym

env = flappy_bird_gym.make("FlappyBird-v0")
obs = env.reset()

while True:
    # Next action:
    action = np.random.choice([0,1], p=[.92, .08]) 

    print("Horizontal distance to next pipe:", obs[0], 
    ",difference between bird's y and pipe gap's y:", obs[1])
    
    # Processing:
    obs, reward, done, info = env.step(action)
    
    print(info)
  
    # Rendering the game:
    env.render()
    time.sleep(1 / 30)  # frames per second

    # Check if player is still alive
    if done:
        break # otherwise, end loop

env.close()

