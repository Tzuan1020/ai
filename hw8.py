# 參考111010529顏瑋成同學，經理解所完成
import gymnasium as gym
env = gym.make("CartPole-v1", render_mode="human") # 若改用這個，會畫圖
# env = gym.make("CartPole-v1", render_mode="rgb_array")
observation, info = env.reset(seed=42)
score = 0
#當竿子的角速度大於0的時候向右，反之向左
def action(observation):
    if observation[3]>0:
        action = 1
    else:
        action = 0
    return action
for _ in range(1000):
   env.render()
   observation, reward, terminated, truncated, info = env.step(action(observation))
   #print('observation=', observation)
   score += reward
   if terminated or truncated:
      observation, info = env.reset()
      print('done, score=', score)
      score = 0
env.close()
