import pytest
from soma_subtrai import soma, subtrai

def test_soma():
  assert soma(3, 2) == 5 
  assert soma(8, 5) == 13
  assert soma(12, 21) == 33
def test_subtrai():
  assert subtrai(9, 3) == 6
  assert subtrai(18, 6) == 12
  assert subtrai(10, 5) == 5
