import gymnasium


def episode_trigger(episode: int):
    return episode == 0 or (episode + 1) % 25 == 0


def make_environment(name: str):
    env = gymnasium.make(name, render_mode="rgb_array", hardcore=True)
    env = gymnasium.wrappers.RecordVideo(env, "./videos", episode_trigger)
    return env
