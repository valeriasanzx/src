"""
Artificial Intelligence responsible for playing the game of T3!
Implements the alpha-beta-pruning mini-max search algorithm
"""
from dataclasses import *
from typing import *
from t3_state import *

def choose(state: "T3State") -> Optional["T3Action"]:
    """
    Main workhorse of the T3Player that makes the optimal decision from the max node
    state given by the parameter to play the game of Tic-Tac-Total.
    
    [!] Remember the tie-breaking criteria! Moves should be selected in order of:
    1. Best utility
    2. Smallest depth of terminal
    3. Earliest move (i.e., lowest col, then row, then move number)
    
    You can view tiebreaking as something of an if-ladder: i.e., only continue to
    evaluate the depth if two candidates have the same utility, only continue to
    evaluate the earliest move if two candidates have the same utility and depth.
    
    Parameters:
        state (T3State):
            The board state from which the agent is making a choice. The board
            state will be either the odds or evens player's turn, and the agent
            should use the T3State methods to simplify its logic to work in
            either case.
    
    Returns:
        Optional[T3Action]:
            If the given state is a terminal (i.e., a win or tie), returns None.
            Otherwise, returns the best T3Action the current player could take
            from the given state by the criteria stated above.
    """
    # [!] TODO! Implement alpha-beta-pruning minimax search!
    return None

# [Optional / Suggested] TODO! Add any helper methods or dataclasses needed to
# manage the alpha-beta-pruning minimax operation

def alphabeta(state: "T3State", alpha: float, beta: float, is_max: bool) -> float:
    if state.is_tie(): return 0
    if state.is_win():
        print("--", state._odd_turn, "--")
        print(state)
        return 1 if state._odd_turn else -1

    if is_max:
        max_util: float = float('-inf')
        for act, child in state.get_transitions():
            print(act)
            util = alphabeta(child, alpha, beta, False)
            max_util = max(max_util, util)
            alpha = max(alpha, util)
            if beta <= alpha:
                print("---------")
                break
        return max_util

    else:
        min_util: float = float('inf')
        for act, child in state.get_transitions():
            print(act)
            util = alphabeta(child, alpha, beta, True)
            min_util = min(min_util, util)
            beta = min(beta, util)
            if beta <= alpha:
                print("---------")
                break
        return min_util

state = T3State(False,
         [
            [0, 0, 1],
            [2, 0, 4],
            [5, 1, 0]
        ])
# print(state.is_win())
print(alphabeta(state, float("-inf"), float("inf"), not state._odd_turn))