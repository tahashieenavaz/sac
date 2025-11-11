from utils import make_environment
from homa.rl import SoftActorCritic
from homa import settings


env = make_environment(settings("environment"))
algorithm = SoftActorCritic(
    state_dimension=24, action_dimension=4, buffer_capacity=1_000_000
)

for episode in range(settings("episodes")):
    done = False
    episode_reward = 0.0
    state, _ = env.reset()

    while not done:
        if algorithm.is_warmup():
            action = env.action_space.sample()
        else:
            action, _ = algorithm.actor.sample(state)

        next_state, reward, truncated, terminated, _ = env.step(
            action.squeeze(0).detach().cpu().numpy()
        )
        reward *= settings("reward_scale")
        done = truncated or terminated
        algorithm.buffer.record(
            state=state,
            next_state=next_state,
            action=action.squeeze(0).detach().cpu().numpy(),
            reward=reward,
            termination=done,
        )
        state = next_state
        episode_reward += reward
        algorithm.train()
        algorithm.tick()

    print(
        f"episode: {episode}, reward: {episode_reward}, t: {algorithm.t}",
        flush=True,
    )

env.close()
