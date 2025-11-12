# Bipedal Walker (Soft Actor Critic)

## Videos

<p align="center">
    <img src="./media/episode-0.gif" width="400" />
</p>

The first try in which agent chooses actions uniformly at random to enhance the starting point of the buffer. This is done using `action = env.action_space.sample()`.

<p align="center">
    <img src="./media/episode-2924.gif" width="400" />
</p>

Episode 2925, which has clearly shown that the agent has learned how to walk and doge some edge cases like getting stuck on a small obstacle.
