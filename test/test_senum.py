#!/usr/bin/env python3

import pytest
from overloaded.senum import Senum, using_senum

class State(Senum):
    begin = 1
    middle = 2
    end = 3


def test_string_compare():
    state = State.begin
    assert state == "begin"
    assert "begin" == state


def test_string_set():
    state = State.begin
    state += "end"
    assert state == State.end


def test_bad_compare():
    state = State.begin
    with pytest.raises(Exception):
        state == "ending"

def test_example():
    result = using_senum()
    assert result == "begin"
