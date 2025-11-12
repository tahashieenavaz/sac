# Bipedal Walker (Soft Actor Critic)

## Results

### Rewards

<p align="center">
    <img src="./media/rewards.png" width="600" />
</p>

### Alpha

<p align="center">
    <img src="./media/alpha-log.png" width="600" />
</p>

<p align="center">
    <img src="./media/alpha-cropped.png" width="600" />
</p>

## Videos

<p align="center">
    <img src="./media/episode-1.gif" width="600" />
</p>

The first try in which agent chooses actions uniformly at random to enhance the starting point of the buffer. This is done using `action = env.action_space.sample()`.

<p align="center">
    <img src="./media/episode-2925.gif" width="600" />
</p>

Episode 2925, which has clearly shown that the agent has learned how to walk and doge some edge cases like getting stuck on a small obstacle.

<p align="center">
    <img src="./media/episode-3000.gif" width="600" />
</p>

Finally, the last episode (not necessarily the best performance) shows that the agent has "learnt" something but needs to be trained in the environment more to get better over time.
