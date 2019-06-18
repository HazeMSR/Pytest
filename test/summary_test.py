import pytest

"""
    Run with: pytest -ra
    
    The -r options accepts a number of characters after it, with a used above meaning “all except passes”.
    Here is the full list of available characters that can be used:

        f - failed
        E - error
        s - skipped
        x - xfailed
        X - xpassed
        p - passed
        P - passed with output
        a - all except pP
        A - all

    Using p lists the passing tests, whilst P adds an extra section “PASSES” with those tests that passed but had captured output:
        pytest -rpP
"""
@pytest.fixture
def error_fixture():
    assert 0


def test_ok():
    print("ok")


def test_fail():
    assert 0


def test_error(error_fixture):
    pass


def test_skip():
    pytest.skip("skipping this test")


def test_xfail():
    pytest.xfail("xfailing this test")


@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    pass
