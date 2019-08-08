import gym
import numpy as np

from stable_baselines.sac.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import SAC


import os

#GPU isolation
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="3"
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'


env = gym.make('BipedalWalker-v2')
#env = DummyVecEnv([lambda: env])

model = SAC(MlpPolicy, env, verbose=1,learning_starts=1000 )
#model = SAC(MlpPolicy, env, verbose=1)
model.learn(total_timesteps=1000, log_interval=10)
model.save("sac_bipedalwalker")
print("Model saved to sac_bipedalwalkwer")

del model # remove to demonstrate saving and loading

for i in range(100):
   print("experiment id: ", i)
   model = SAC.load("sac_bipedalwalker", env=env, tensorboard_log="./sac_bipedalwalker_tensorboard/")
   print("loaded")
   model.learn(total_timesteps=500000, log_interval=50)
   print("learned again")
obs = env.reset()

#while True:
#    action, _states = model.predict(obs)
#    obs, rewards, dones, info = env.step(action)
#    env.render()