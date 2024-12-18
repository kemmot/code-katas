import unittest
from unittest import mock

import day02_part02_rednosedreports as rnr


class IsReportSafeTests(unittest.TestCase):
    def test_increasing_is_safe(self):
        self.assertTrue(rnr.is_report_safe([1,2,3,4,5]))
        self.assertTrue(rnr.is_report_safe([1,4,7,10,13]))

    def test_decreasing_is_safe(self):
        self.assertTrue(rnr.is_report_safe([5,4,3,2,1]))
        self.assertTrue(rnr.is_report_safe([13,10,7,4,1]))

    def test_one_big_increasing_jump_is_unsafe(self):
        self.assertFalse(rnr.is_report_safe([1,5,3,4,5]))

    def test_one_big_decreasing_jump_is_unsafe(self):
        self.assertFalse(rnr.is_report_safe([5,1,3,2,1]))

    def test_one_duplicate_is_unsafe(self):
        self.assertFalse(rnr.is_report_safe([1,1,3,4,5]))

class IsReportSafeWithDampenerTests(unittest.TestCase):
    def test_one_duplicate_is_safe(self):
        self.assertTrue(rnr.is_report_safe_with_dampener([1,1,3,4,5]))

    def test_mulitple_duplicates_is_not_safe(self):
        self.assertFalse(rnr.is_report_safe_with_dampener([1,1,2,2,5]))

    def test_one_big_increasing_jump_is_safe(self):
        self.assertTrue(rnr.is_report_safe_with_dampener([1,5,3,4,5]))

    def test_one_big_decreasing_jump_is_safe(self):
        self.assertTrue(rnr.is_report_safe_with_dampener([5,1,3,2,1]))

    def test_multiple_big_increasing_jumps_is_not_safe(self):
        self.assertFalse(rnr.is_report_safe_with_dampener([1,5,9,13,17]))

    def test_multiple_big_decreasing_jumps_is_not_safe(self):
        self.assertFalse(rnr.is_report_safe_with_dampener([17,13,9,5,1]))

    def test_second_level_confusing_direction_is_safe(self):
        self.assertTrue(rnr.is_report_safe_with_dampener([5,4,6,7,8]))

