# ATBD (Adaptive tit-for-tat with betrayal detection)


## Algorithm Logic Overview

### Part 1: Basic Strategy

My algorithm implements a balanced approach to the Iterated Prisoner's Dilemma with the following key features:

1. **Adaptive Behavior**: The strategy adapts to the opponent's playing style by tracking their cooperation rate and recent behavior patterns.

2. **Pattern Recognition**: The algorithm can detect if the opponent is playing tit-for-tat or using betrayal patterns (cooperating to build trust before defecting).

3. **Forgiveness Mechanism**: To avoid being stuck in mutual defection cycles, the algorithm occasionally forgives defections.

4. **Dynamic Cooperation**: The strategy adjusts its cooperation level based on the opponent's trustworthiness.

5. **Endgame Awareness**: When the number of rounds is known, the algorithm becomes more strategic in the final rounds.

The core philosophy is to be neither completely naive nor overly aggressive - the algorithm aims to establish cooperation when possible, but protects itself against exploitation.

### Part 2: Opponent Selection Strategy

1. **Opponent Evaluation**: Carefully tracks performance against each opponent and calculates an expected value score.

2. **Exploration vs. Exploitation**: Balances between trying new opponents and continuing with profitable relationships.

3. **Maximizing Points**: Focuses on playing more rounds with opponents that yield higher average points per round.

4. **Adaptation**: Uses the same core decision-making logic as part 1, but with additional opponent selection intelligence.

## Implementation Details

The algorithm uses several factors to make decisions:
- Overall cooperation rate of opponents
- Recent behavior patterns
- Detection of specific strategies
- Round count awareness
- Pattern recognition for detecting betrayal cycles

This balanced approach aims to perform well against a wide variety of opponent strategies while maximizing total points earned.