import os
from enum import Enum


PLAYER1_ROCK = 'A'
PLAYER1_PAPER = 'B'
PLAYER1_SCISSORS = 'C'
PLAYER2_ROCK = 'X'
PLAYER2_PAPER = 'Y'
PLAYER2_SCISSORS = 'Z'


class RoundOutcome(Enum):
    WIN = 0
    LOSE = 1
    DRAW = 2


class RockPaperScissorsChoice:
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


def interpret_player1_choice(choice_code: str) -> RockPaperScissorsChoice:
    if choice_code == PLAYER1_ROCK:
        return RockPaperScissorsChoice.ROCK
    elif choice_code == PLAYER1_PAPER:
        return RockPaperScissorsChoice.PAPER
    elif choice_code == PLAYER1_SCISSORS:
        return RockPaperScissorsChoice.SCISSORS
    else:
        raise Exception(f'Unknown player 1 option: {choice_code}')

def interpret_player2_choice(choice_code: str) -> RockPaperScissorsChoice:
    if choice_code == PLAYER2_ROCK:
        return RockPaperScissorsChoice.ROCK
    elif choice_code == PLAYER2_PAPER:
        return RockPaperScissorsChoice.PAPER
    elif choice_code == PLAYER2_SCISSORS:
        return RockPaperScissorsChoice.SCISSORS
    else:
        raise Exception(f'Unknown player 2 option: {choice_code}')

def calculate_player2_round_outcome(player1: RockPaperScissorsChoice, player2: RockPaperScissorsChoice) -> RoundOutcome:
    if player1 == player2:
        return RoundOutcome.DRAW
    elif player1 == RockPaperScissorsChoice.ROCK:
        if player2 == RockPaperScissorsChoice.PAPER:
            return RoundOutcome.WIN
        elif player2 == RockPaperScissorsChoice.SCISSORS:
            return RoundOutcome.LOSE
    elif player1 == RockPaperScissorsChoice.PAPER:
        if player2 == RockPaperScissorsChoice.ROCK:
            return RoundOutcome.LOSE
        elif player2 == RockPaperScissorsChoice.SCISSORS:
            return RoundOutcome.WIN
    elif player1 == RockPaperScissorsChoice.SCISSORS:
        if player2 == RockPaperScissorsChoice.ROCK:
            return RoundOutcome.WIN
        elif player2 == RockPaperScissorsChoice.PAPER:
            return RoundOutcome.LOSE

def interpret_round(round_code: str) -> tuple[RockPaperScissorsChoice, RockPaperScissorsChoice]:
    # TODO: check format
    player1 = interpret_player1_choice(round_code[0])
    player2 = interpret_player2_choice(round_code[2])
    return [player1, player2]

def calculate_choice_score(choice: RockPaperScissorsChoice) -> int:
    if choice == RockPaperScissorsChoice.ROCK:
        return 1
    elif choice == RockPaperScissorsChoice.PAPER:
        return 2
    elif choice == RockPaperScissorsChoice.SCISSORS:
        return 3
    else:
        raise Exception(f'choice unknown: {choice_code}')

def calculate_win_lose_score(outcome: RoundOutcome) -> int:
    if outcome == RoundOutcome.WIN:
        return 6
    elif outcome == RoundOutcome.DRAW:
        return 3
    elif outcome == RoundOutcome.LOSE:
        return 0
    else:
        raise Exception(f'Unknown round outcome: {outcome}')



def calculate_round_score(round: tuple[RockPaperScissorsChoice, RockPaperScissorsChoice]) -> int:
    score = 0
    round_outcome = calculate_round_outcome(round_code)
    score = calculate_choice_score(round_code[0])
    score += calculate_win_lose_score(round_outcome)
    return score

def read_input(path: str):
    rounds = []
    with open(path, 'r') as file:
        line_number = 1
        for line in file.readlines():
            rounds.append(line.strip())
    return rounds

def evaluate_game(path: str) -> int:
    total_score = 0
    for round_code in read_input(input_path):
        round_score = calculate_round_score(round_code)
        total_score += round_score
    return total_score


if __name__ == '__main__':
    input_path = os.path.dirname(os.path.realpath(__file__))
    input_path = os.path.join(input_path, 'day02_input1.txt')
    total_score = evaluate_game(input_path)
    print(f'Total score: {total_score}')
