# -*- coding: utf-8 -*-

import pytest

from votelib.fptp import fptp

class TestFPTP():
    def test_fptp(self):
        with open("tests/data/fptp.csv") as f:
            ballots = f.read()

        results = fptp(ballots)
        assert results["winner"] == "Woof Woofington"
        assert results["tallies"]["Woof Woofington"] == 4
        assert results["tallies"]["Meow Meowington"] == 3
