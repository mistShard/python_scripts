from fitness import *
from pytest import approx
import pytest

def test_in_cm():
    incm = in_cm(1)
    assert incm == approx(2.54)


pytest.main(["-v", "--tb=no", "test_fitness.py"])