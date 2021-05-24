# -*- coding: utf-8 -*-

import pytest

from votelib import irv


class TestIRV():
    def test_irv(self):
        results = irv()
        assert results['winner'] == 'cat'
        assert len(results) == 2
        assert type(results) is dict
        assert type(results['winner']) is str
        assert type(results['votes']) is int
        assert results['votes'] == 360
