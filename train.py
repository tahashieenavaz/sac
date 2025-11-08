import warnings
from utils import make_environment
from homa.rl import SoftActorCritic

warnings.filterwarnings("ignore")

env = make_environment("BipedalWalker-v3")
algorithm = SoftActorCritic(state_dimension=24, action_dimension=4)

for episode in range(1000):
    done = False
    state, _ = env.reset()

    while not done:
        action, probability = algorithm.actor.sample(state)
        next_state, reward, truncated, terminated, _ = env.step(
            action.squeeze(0).detach().cpu().numpy()
        )
        algorithm.buffer.record(
            state=state,
            next_state=next_state,
            action=action,
            reward=reward,
            termination=done,
            probability=probability,
        )
        state = next_state

    algorithm.train()

env.close()
