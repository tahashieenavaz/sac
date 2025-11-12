# Bipedal Walker (Soft Actor Critic)

## Videos

<p align="center">
    <video width="400" controls>
    <source src="media/epsisode-0.gif" type="video/mp4">
    </video>
</p>

The first try in which agent chooses actions uniformly at random to enhance the starting point of the buffer. This is done using `action = env.action_space.sample()`.

<p align="center">
    <video width="400" controls>
    <source src="media/epsisode-2925.gif" type="video/mp4">
    </video>
</p>

Episode 2925, which has clearly shown that the agent has learned how to walk and doge some edge cases like getting stuck on a small obstacle.
