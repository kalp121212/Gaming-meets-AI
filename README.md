# SoC_Gaming_meets_AI_Kalp

## Project Description:

I have made an intelligent agent using tensorflow(tensorflow 1 is used, not tensorflow 2) to play the game 2048. I have used RL (Reinforcement Learning) method of **Q Learning** with different types of neural deep networks to form an efficient model called **DQN (Deep Q Network)**. More can be read about this method from this [paper.](https://deepmind.com/research/publications/deep-reinforcement-learning-double-q-learning)

## Description of Files:

- **Assignments**:- This consists of the Python assignments alloted to us by our mentors.

- **game_2048.py**:- This file consists of the environment of the game 2048, it has all the important definitions required such as states, state space, action space, observation space etc. The system of giving rewards is also defined here.

- **dqn.py**:- This file consists of a simple DQN network made using tensorflow with 3 hidden layers. It also has the agent class. The aim of this code is to train this network and update its results every 100 episodes in the graphs.

- **graph.png**- Consists of the graph of Biggest tile in the 2048 game vs no of episodes

- **report.md**- SoC report

## Running the code:

-**Requirements**:- Make sure you have python libraries such as numpy, matplotlib, gym and tensorflow installed on your system.
If u dont have any of these packages installed, you can install them using this simple command:
- pip install (package name)

Now, for training the model, you can directly run the dqn.py file using python dqn.py command on CMD(For windows user) or on terminal(For linux and MacOs users).
This will display the reward, board and final score reached after each episode and will display and store graph as graph.png after every 100 episodes.

## My Work Period:

1. **30th March - 14th April**:- Learnt the basic technical knowledge required for the project such as git, Python libraries like numpy, matplotlib. This helped in setting up the base required for the project.

### Resource links:

- [Python Tutorial Website](learnpython.org)
- [CS229 Stanford Lecture Videos](https://www.youtube.com/watch?v=jGwO_UgTS7I&list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU)

2. **14th April - 12th May**:- We were provided books and lectures on ML and DL. This was required to get understanding about how neural networks work and hence how deep learning is to be implemented.

### Resource links-
- [Basic ML and DL course by AndrewNg on coursera](https://www.coursera.org/learn/machine-learning)
- [Book provided for DL](http://faculty.neu.edu.cn/yury/AAI/Textbook/DeepLearningBook.pdf)
- [3b1b Video for Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)

3. **12th May - 8th June**:- We were given books, lectures and papers on RL. This was to ensure a good foundation in the topic of RL so that we can understand the theory behind the code.

### Resource links-
- [RL book by Richard S. Sutton and Andrew G. Barto](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf)
- [Stanford lectures for RL](https://www.youtube.com/watch?v=FgzM3zpZ55o&list=PLoROMvodv4rOSOPzutgyCTapiGlY2Nd8u)

4. **12th June-1st July**:- Now we were given tutorials on PyTorch and TensorFlow to understand how a neural network is coded in practice. This helped in understanding how exactly the code should be structured.

### Resource links-
- [PyTorch tutorials](https://pytorch.org/tutorials/)
- [TensorFlow tutorials](https://www.tensorflow.org/tutorials)

5. **1st July - 17th July**:- This was the main coding period where we were expected to implement all the theory learnt into practice. First, I made a simple general DQN network to train network for the cartpole problem on OpenAI Gym. This was very helpful to learn the basic way of how the code worked. Later, I extended this implementation to work for 2048 game and then trained its performance for 2048 too.
