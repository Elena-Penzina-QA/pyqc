
from pyqc.math_utils import add, multiply, power

def test_add():
    assert add(2, 3) == 5
def test_multiply():
    assert multiply(2, 3) == 6

def test_power():
    assert power(2, 3) == 8
