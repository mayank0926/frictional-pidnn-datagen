from gym.envs.registration import register

register(
    id='mujoco-slide-v0',
    entry_point='frictional_pidnn_datagen.envs:MujocoSlideEnv',
)
