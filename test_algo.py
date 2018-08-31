import pytest
import find_array

def test_offset():
    offset = [8,8,8,8,8,8,8,8]
    test_data =[1, 2 ,3, 4, 5, 6, 7]

    assert (offset == find_array.calculate_offset(test_data))


def test_boyer():
    offset = [8, 8, 8, 8, 8, 8, 8, 8]
    test_data = [1, 2, 3, 4, 5, 6, 7]

    assert (4 == 2 + 2)

def test_max_matcher():
    fragm = [1,2,3,4,5]
    data = [1,2,3,4,5,6]
    find_array.max_matcher(data,fragm)
    assert (fragm == data)
