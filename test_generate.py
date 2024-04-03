"""Test Suite for the generate module."""

from typing import List

def test_generate_random_number():
    """Test that the generate_random_number function correctly generates a random number either within the maximum or over the maximum"""
    result = generate.generate_random_number()
    result_big = generate.generate_random_number(0, 0) + 1
    assert result is not None
    assert result_big is not None
    assert isinstance(result, int)
    assert isinstance(result_big, int)
    assert result >=0
    assert result_big == 1

def test_generate_random_list():
    """Test that the generate_random_list function correctly generates a list based on specifications"""
    empty_list = generate.generate_random_list(0, 0)
    list_result = generate.generate_random_list(2, 100)
    assert list_result is not None
    assert empty_list is not None
    assert isinstance(list_result, list)
    assert isinstance(empty_list, list)
    assert len(list_result) == 2
    assert len(empty_list) == 0
