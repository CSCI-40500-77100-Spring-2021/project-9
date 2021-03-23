# -*- coding: utf-8 -*-

import pytest

from votelib import fptp

class TestFPTP():
    def test_fptp(self):
        with open("tests/data/fptp.csv") as f:
            ballots = f.read()

        results = fptp(ballots)
        assert results["winners"] == {"Woof Woofington"}
        assert results["tallies"]["Woof Woofington"] == 4
        assert results["tallies"]["Meow Meowington"] == 3

    def test_fptp_tie(self):
        with open("tests/data/fptp_tie.csv") as f:
            ballots = f.read()

        results = fptp(ballots)
        assert results["winners"] == {"Woof Woofington", "Meow Meowington"}
        assert results["tallies"]["Woof Woofington"] == 2
        assert results["tallies"]["Meow Meowington"] == 2
        assert results["tallies"]["Boaty McBoatface"] == 1
