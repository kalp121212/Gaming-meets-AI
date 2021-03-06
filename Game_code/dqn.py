#Code to implement DQN network to play 2048
#Author: Kalp Vyas

import game_2048
import gym
import random
import numpy as np
import tensorflow as tf
from collections import deque
import matplotlib.pyplot as plt

env = game_2048.Game2048Env()

class QNetwork():
    def __init__(self, state_dim, action_size):
        self.state_in = tf.placeholder(tf.float32, shape=[None, *state_dim])
        self.action_in = tf.placeholder(tf.int32, shape=[None])
        self.q_target_in = tf.placeholder(tf.float32, shape=[None])
        action_one_hot = tf.one_hot(self.action_in, depth=action_size)

        self.hidden1 = tf.layers.dense(self.state_in, 128, activation=tf.nn.relu)
        self.hidden2 = tf.layers.dense(self.hidden1, 128, activation=tf.nn.relu)
        self.hidden3 = tf.layers.dense(self.hidden2, 128, activation=tf.nn.relu)
        self.q_state = tf.layers.dense(self.hidden3, action_size, activation=None)
        self.q_state_action = tf.reduce_sum(tf.multiply(self.q_state, action_one_hot), axis=1)

        self.loss = tf.reduce_mean(tf.square(self.q_state_action - self.q_target_in))
        self.optimizer = tf.train.AdamOptimizer(learning_rate=0.0001).minimize(self.loss)

    def update_model(self, session, state, action, q_target):
        feed = {self.state_in: state, self.action_in: action, self.q_target_in: q_target}
        session.run(self.optimizer, feed_dict=feed)

    def get_q_state(self, session, state):
        q_state = session.run(self.q_state, feed_dict={self.state_in: state})
        return q_state

class ReplayBuffer():
    def __init__(self, maxlen):
        self.buffer = deque(maxlen=maxlen)
        
    def add(self, experience):
        self.buffer.append(experience)
        
    def sample(self, batch_size):
        sample_size = min(len(self.buffer), batch_size)
        samples = random.choices(self.buffer, k=sample_size)
        return map(list, zip(*samples))

class DQNAgent():
    def __init__(self, env):
        self.state_dim = env.observation_space.shape
        self.action_size = env.action_space.n
        self.q_network = QNetwork(self.state_dim, self.action_size)
        self.replay_buffer = ReplayBuffer(maxlen=1000000)
        self.gamma = 0.96
        self.eps = 1.0
        
        self.sess = tf.Session()
        self.sess.run(tf.global_variables_initializer())
        
    def get_action(self, state):
        q_state = self.q_network.get_q_state(self.sess, [state])
        action_greedy = np.argmax(q_state)
        action_random = np.random.randint(self.action_size)
        action = action_random if random.random() < self.eps else action_greedy
        return action
    
    def train(self, state, action, next_state, reward, done):
        self.replay_buffer.add((state, action, next_state, reward, done))
        states, actions, next_states, rewards, dones = self.replay_buffer.sample(64)
        q_next_states = self.q_network.get_q_state(self.sess, next_states)
        q_next_states[dones] = np.zeros([self.action_size])
        q_targets = rewards + self.gamma * np.max(q_next_states, axis=1)
        self.q_network.update_model(self.sess, states, actions, q_targets)
        
        if done: self.eps = max(0.1, 0.99*self.eps)
    
    def __del__(self):
        self.sess.close()

#Training 
agent = DQNAgent(env)
num_episodes = 10000000
episodes=[]
scores=[]
rewards=[]

for ep in range(1,num_episodes+1):
    state = env.reset()
    state = tf.reshape(state,[16])
    state=state.eval(session=tf.Session())

    total_reward = 0
    done = False
    while not done:
        action = agent.get_action(state)
        next_state, reward, done, info = env.step(action)
        agent.train(state, action, next_state, reward, done)
        final_score=env.final_score()
        total_reward += reward
        state = next_state
    env.render()    
    print("Episode: {}, total_reward: {:.2f}".format(ep, total_reward))
    episodes.append(ep+1)
    scores.append(final_score)
    rewards.append(total_reward)
    if ep%100==0:
        episodes_x=np.array(episodes)
        scores_x=np.array(scores)
        plot1=plt.figure(1)
        plt.scatter(episodes_x,scores_x)
        plot2=plt.figure(2)
        plt.plot(episodes,rewards)
        plt.show()
        plt.close()
        plot1.savefig('graph.png')


