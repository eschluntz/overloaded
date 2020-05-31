#!/usr/bin/env python3
"""
enum class that supports string comparison and assignment
# OR: State = Senum(["begin", "middle", "end"])
class State(Senum):
    begin = 1
    middle = 2
    end = 3

state = State.begin

if state == "begin":
    state = "middle"
elif state == State.middle:
    state = State.end
elif state == "edn":  # this will throw an exception
    state = "beginning"  # this will throw an exception
"""

from enum import Enum


class Senum(Enum):
    """If someone subclasses this in the same way as Enum, the attribs
    will be name, value, and all the possible values."""

    def __eq__(self, other):

        # compare to other string
        if isinstance(other, str):

            # do we have this attribute?
            if hasattr(self, other):
                return self.name == other
            else:
                raise Exception("tried to compare {} into Enum({})".format(other, self))

        # compare to Enum / Senum
        else:  # todo make sure this actually an enum class
            return self.value == other.value

    def __iadd__(self, other):

        # set to other string
        if isinstance(other, str):
            # do we have this attribute?
            if hasattr(self, other):
                # create a new enum with this value
                return getattr(self, other)
            else:
                raise Exception("tried to set {} into Enum({})".format(other, self))

        # take the other value
        else:
            return other


def using_senum():
    class State(Senum):
        begin = 1
        middle = 2
        end = 3

    state = State.begin
    for _ in range(6):
        if state == State.begin:
            state = State.middle
        elif state == "middle":
            state += "end"
        elif state == "end":  # throws error
            state += "begin"  # throws error
        print(state)
    return state


if __name__ == "__main__":
    using_senum()
