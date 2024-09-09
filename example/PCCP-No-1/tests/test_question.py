import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from src import q

def inc(x):
    return x + 1

def test_answer_1():
    assert inc(3) == 5
