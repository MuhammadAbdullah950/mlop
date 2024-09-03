import pytest
from app import add
from app import divide
from app import multiplication

def test_add():
    assert add(2, 3) == 5

def test_divode():
    assert divide(6,3)==2

def test_multiply():
    assert multiplication(2,2)==4

def test_multiply2():
    assert multiplication(2,4)==8