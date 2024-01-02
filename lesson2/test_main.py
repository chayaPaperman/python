import main
import pytest


def test_find_primes():
    assert main.find_primes(15) == [2, 3, 5, 7, 11, 13]


def test_find_primes():
    assert main.find_primes(5) == [2, 3]


@pytest.mark.parametrize('mylist,result', [([4, 2, 6, 3, 1, ], [1, 2, 3, 4, 6]), ([2, 4, 6, 8, 2, ], [2, 2, 4, 6, 8])])
def test_sort_list(mylist, result):
    assert main.sort_list(mylist) == result


@pytest.mark.skip(reason="don't computed")
def test_find_primes():
    assert main.find_primes(100) == []


@pytest.mark.sort
def test_sort_list():
    assert main.sort_list([2, 8, 6, 4], [2, 4, 6, 8])


@pytest.mark.sort
def test_sort_list():
    assert main.sort_list([2, 9, 6, 3], [2, 3, 6, 9])
