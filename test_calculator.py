from calculator import ssum, subtract, multiply, power, modulus, floor_divide, divide
import pytest

def test_sum():
    assert (2+3)==5

def test_subtract():
    assert (3-5)==-2

def test_multiply():
    assert (3*5)==15

def test_power():
    assert (2**3)==8

def test_modulus():
    assert (10%3)==1

def test_floor_divide():
    assert (10//3)==3

def test_divide():
    with pytest.raises(ZeroDivisionError):
        divide(5,0)
        
def test_floor_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        floor_divide(5,0)



