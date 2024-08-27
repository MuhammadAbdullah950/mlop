import pytest
from app import add
from app import divide

def test_add():
    assert add(2, 3) == 5

def test_divode():
    assert divide(6,3)==2
