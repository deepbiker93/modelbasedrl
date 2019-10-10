
import gym

from stable_baselines import A2C
from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv


import os

#GPU isolation
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="3"
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# Create and wrap the environment
env = gym.make('LunarLander-v2')
env = DummyVecEnv([lambda: env])

#model = A2C(MlpPolicy, env, ent_coef=0.1, verbose=1,learning_starts=1000 )
## Train the agent
#model.learn(total_timesteps=1000, log_interval=10)
## Save the agent
#model.save("a2c_lunar")
#del model  # delete trained model to demonstrate loading

# Load the trained agent

for i in range(100):
  print("experiment id:", i)
  model = A2C.load("a2c_lunar",env=env, tensorboard_log="./a2c_lunar_lander_sto/")
  print("loaded")
  model.learn(total_timesteps=500000, log_interval=50, stochastic_reward=True)
# Enjoy trained agent
obs = env.reset()
#for i in range(1000):
#    action, _states = model.predict(obs)
#    obs, rewards, dones, info = env.step(action)
#    env.render()