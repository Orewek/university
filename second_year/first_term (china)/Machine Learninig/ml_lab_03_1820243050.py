import numpy as np

observations = ['T', 'A', 'G', 'A']

A = np.array([
    [0.0, 0.5, 0.5, 0.0, 0.0, 0.0],
    [0.0, 0.2, 0.0, 0.8, 0.0, 0.0],
    [0.0, 0.0, 0.8, 0.0, 0.2, 0.0],
    [0.0, 0.0, 0.0, 0.4, 0.0, 0.6],
    [0.0, 0.0, 0.0, 0.0, 0.1, 0.9],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])

M = np.array([
    {'A': 0.0, 'C': 0.0, 'G': 0.0, 'T': 0.0},
    {'A': 0.4, 'C': 0.1, 'G': 0.2, 'T': 0.3},
    {'A': 0.4, 'C': 0.1, 'G': 0.1, 'T': 0.4},
    {'A': 0.2, 'C': 0.3, 'G': 0.3, 'T': 0.2},
    {'A': 0.1, 'C': 0.4, 'G': 0.4, 'T': 0.1},
    {'A': 0.0, 'C': 0.0, 'G': 0.0, 'T': 0.0}])


def forward(A: list[float], M: list[str, float], observations: list[str]) -> float:
    states: int = len(A)
    obs: int = len(observations)
    forward_matrix: list[float] = [[0.0] * states for _ in range(obs + 1)]
    for state in states:
        forward_matrix[0][state] = 1.0 if state == 0 else 0.0
    probability: int = 0
    for t in range(1, obs + 1):
        for j in range(states):
            prob_sum: float = sum(forward_matrix[t - 1][i] * A[i][j] for i in range(states))
            forward_matrix[t][j]: float = prob_sum * M[j][observations[t - 1]]
            if t == 4 and j == 5:
                probability: float = sum(forward_matrix[t][i] * A[i][j] for i in range(states))

    return probability



prob: float = forward(A, M, observations)
print(f'Probability of the observed sequence is: {prob}')
