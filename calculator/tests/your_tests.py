#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE

### Jordan's Tests
# Checks that the program outputs "20" for an input of "10 + 10"
assert run("1 + 2").output == "3"

#checks that the program outputs "44" for an input of "124 - 80" 
assert run("124 - 80").output == "44"

###

print("All tests passed!")
