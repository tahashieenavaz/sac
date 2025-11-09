import warnings
from utils import make_environment
from homa.rl import SoftActorCritic
from homa import settings

warnings.filterwarnings("ignore")

env = make_environment(settings("environment"))
algorithm = SoftActorCritic(state_dimension=24, action_dimension=4)

for episode in range(settings("episodes")):
    done = False
    episode_reward = 0.0
    state, _ = env.reset()

    while not done:
        action, probability = algorithm.actor.sample(state)
        next_state, reward, truncated, terminated, _ = env.step(
            action.squeeze(0).detach().cpu().numpy()
        )
        algorithm.buffer.record(
            state=state,
            next_state=next_state,
            action=action.squeeze(0).detach().cpu().numpy(),
            reward=reward,
            termination=done,
            probability=probability.squeeze(0).detach().cpu().numpy(),
        )
        done = truncated or terminated
        state = next_state
        episode_reward += reward

    algorithm.train()
    print(f"episode: {episode}, reward: {episode_reward}", flush=True)

env.close()
