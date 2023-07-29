import unittest
from unittest import mock

import day02_rockpaperscissors as rps


class InterpretPlayer1ChoiceTests(unittest.TestCase):
    def test_rock(self):
        result = rps.interpret_player1_choice('A')
        self.assertEqual(result, rps.RockPaperScissorsChoice.ROCK)
    def test_paper(self):
        result = rps.interpret_player1_choice('B')
        self.assertEqual(result, rps.RockPaperScissorsChoice.PAPER)
    def test_scissors(self):
        result = rps.interpret_player1_choice('C')
        self.assertEqual(result, rps.RockPaperScissorsChoice.SCISSORS)
    def test_unknown(self):
        with self.assertRaises(Exception):
            rps.interpret_player1_choice('X')


class InterpretPlayer2ChoiceTests(unittest.TestCase):
    def test_rock(self):
        result = rps.interpret_player2_choice('X')
        self.assertEqual(result, rps.RockPaperScissorsChoice.ROCK)
    def test_paper(self):
        result = rps.interpret_player2_choice('Y')
        self.assertEqual(result, rps.RockPaperScissorsChoice.PAPER)
    def test_scissors(self):
        result = rps.interpret_player2_choice('Z')
        self.assertEqual(result, rps.RockPaperScissorsChoice.SCISSORS)
    def test_unknown(self):
        with self.assertRaises(Exception):
            rps.interpret_player2_choice('A')


class CalculateRoundOutcomeTests(unittest.TestCase):
    def test_rock_rock(self):
        self.run_test(rps.RockPaperScissorsChoice.ROCK, rps.RockPaperScissorsChoice.ROCK, rps.RoundOutcome.DRAW)
    def test_rock_paper(self):
        self.run_test(rps.RockPaperScissorsChoice.ROCK, rps.RockPaperScissorsChoice.PAPER, rps.RoundOutcome.WIN)
    def test_rock_scissors(self):
        self.run_test(rps.RockPaperScissorsChoice.ROCK, rps.RockPaperScissorsChoice.SCISSORS, rps.RoundOutcome.LOSE)
    def test_paper_rock(self):
        self.run_test(rps.RockPaperScissorsChoice.PAPER, rps.RockPaperScissorsChoice.ROCK, rps.RoundOutcome.LOSE)
    def test_paper_paper(self):
        self.run_test(rps.RockPaperScissorsChoice.PAPER, rps.RockPaperScissorsChoice.PAPER, rps.RoundOutcome.DRAW)
    def test_paper_scissors(self):
        self.run_test(rps.RockPaperScissorsChoice.PAPER, rps.RockPaperScissorsChoice.SCISSORS, rps.RoundOutcome.WIN)
    def test_scissors_rock(self):
        self.run_test(rps.RockPaperScissorsChoice.SCISSORS, rps.RockPaperScissorsChoice.ROCK, rps.RoundOutcome.WIN)
    def test_scissors_paper(self):
        self.run_test(rps.RockPaperScissorsChoice.SCISSORS, rps.RockPaperScissorsChoice.PAPER, rps.RoundOutcome.LOSE)
    def test_scissors_scissors(self):
        self.run_test(rps.RockPaperScissorsChoice.SCISSORS, rps.RockPaperScissorsChoice.SCISSORS, rps.RoundOutcome.DRAW)
    def run_test(self, player1, player2, expected_result):
        result = rps.calculate_player2_round_outcome(player1, player2)
        self.assertEqual(result, expected_result)


class InterpretRoundTests(unittest.TestCase):
    def test_rock_rock(self):
        self.run_test('A X', rps.RockPaperScissorsChoice.ROCK, rps.RockPaperScissorsChoice.ROCK)

    def test_rock_paper(self):
        self.run_test('A Y', rps.RockPaperScissorsChoice.ROCK, rps.RockPaperScissorsChoice.PAPER)

    def test_rock_scissors(self):
        self.run_test('A Z', rps.RockPaperScissorsChoice.ROCK, rps.RockPaperScissorsChoice.SCISSORS)

    def test_paper_rock(self):
        self.run_test('B X', rps.RockPaperScissorsChoice.PAPER, rps.RockPaperScissorsChoice.ROCK)

    def test_paper_paper(self):
        self.run_test('B Y', rps.RockPaperScissorsChoice.PAPER, rps.RockPaperScissorsChoice.PAPER)

    def test_paper_scissors(self):
        self.run_test('B Z', rps.RockPaperScissorsChoice.PAPER, rps.RockPaperScissorsChoice.SCISSORS)

    def test_scissors_rock(self):
        self.run_test('C X', rps.RockPaperScissorsChoice.SCISSORS, rps.RockPaperScissorsChoice.ROCK)

    def test_scissors_paper(self):
        self.run_test('C Y', rps.RockPaperScissorsChoice.SCISSORS, rps.RockPaperScissorsChoice.PAPER)

    def test_scissors_scissors(self):
        self.run_test('C Z', rps.RockPaperScissorsChoice.SCISSORS, rps.RockPaperScissorsChoice.SCISSORS)

    def run_test(self, round_code, player1, player2):
        result = rps.interpret_round(round_code)
        self.assertEqual(result[0], player1)
        self.assertEqual(result[1], player2)


class CalculateChoiceScoreTests(unittest.TestCase):
    def test_rock(self):
        self.run_test(rps.RockPaperScissorsChoice.ROCK, 1)

    def test_paper(self):
        self.run_test(rps.RockPaperScissorsChoice.PAPER, 2)

    def test_scissors(self):
        self.run_test(rps.RockPaperScissorsChoice.SCISSORS, 3)

    def run_test(self, choice, expected_result):
        result = rps.calculate_choice_score(choice)
        self.assertEqual(result, expected_result)


class CalculateWinLoseScoreTests(unittest.TestCase):
    def test_win(self):
        self.run_test(rps.RoundOutcome.WIN, 6)
    def test_draw(self):
        self.run_test(rps.RoundOutcome.DRAW, 3)
    def test_lose(self):
        self.run_test(rps.RoundOutcome.LOSE, 0)
    def run_test(self, outcome, expected_result):
        result = rps.calculate_win_lose_score(outcome)
        self.assertEqual(result, expected_result)
