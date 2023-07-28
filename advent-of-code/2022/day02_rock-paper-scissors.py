from enum import Enum


ROCK = 'X'
PAPER = 'Y'
SCISSORS = 'Z'


class RoundOutcome(Enum):
    WIN = 0
    LOSE = 1
    DRAW = 2


def read_input(path: str):
    rounds = []
    with open(path, 'r') as file:
        line_number = 1
        for line in file.readlines():
            rounds.append(line.strip())
    return rounds

def calculate_choice_score(choice_code: str) -> int:
    if choice_code == ROCK:
        return 1
    elif choice_code == PAPER:
        return 2
    elif choice_code == SCISSORS:
        return 3
    else:
        raise Exception(f'choice unknown: {choice_code}')

def calculate_win_lose_score(outcome: RoundOutcome) -> int:
    pass

def calculate_round_outcome(round_code: str) -> RoundOutcome:
    pass

def calculate_round_score(round_code: str) -> int:
    # TODO: add validation for line format
    score = 0
    round_outcome = calculate_round_outcome(round_code)
    score = calculate_choice_score(round_code[0])
    score += calculate_win_lose_score(round_outcome)
    return score

def evaluate_game(path: str) -> int:
    total_score = 0
    for round_code in read_input(input_path):
        round_score = calculate_round_score(round_code)
        total_score += round_score
    return total_score


if __name__ == '__main__':
    input_path = 'C:\\Users\\karl80355\\source\\repos\\kemmot\\code-katas\\advent-of-code\\2022\\day02_input1.txt'
    total_score = evaluate_game(input_path)
    print(f'Total score: {total_score}')
