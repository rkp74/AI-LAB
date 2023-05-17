# N-Arm Bandit using Epsilon Greedy Algorithm
This is a simple implementation of the n-arm bandit problem using epsilon greedy algorithm. The problem is a classic reinforcement learning problem that involves finding the best action to take in a given situation to maximize the cumulative reward. In the n-arm bandit problem, there are n arms (or levers) that can be pulled, and each arm has an unknown reward associated with it. The goal is to find the arm with the highest reward.

# Usage
To use the program, simply run the main.py file in your Python environment. The program will prompt you to enter the number of arms and the number of iterations (or pulls) to perform. It will then simulate the n-arm bandit problem and output the results to the console.

# Algorithm
The epsilon greedy algorithm is a simple algorithm for exploration-exploitation tradeoff in the reinforcement learning setting. At each step, the algorithm chooses the action with the highest estimated value (exploitation) with probability (1-epsilon) and a random action (exploration) with probability epsilon. The value estimates are updated after each action using the sample average method.

# Conclusion
The n-arm bandit problem is a simple but important problem in reinforcement learning. The epsilon greedy algorithm is an effective method for solving this problem and balancing exploration and exploitation. This implementation provides a basic framework for solving the n-arm bandit problem using the epsilon greedy algorithm.
