from utils import Number


def test_convert_from_dec():
    assert Number(10, 10).convert(2) == '1010'
    assert Number(10, 10).convert(8) == '12'
    assert Number(10, 10).convert(16) == 'A'
    assert Number(10, 10).convert(32) == 'A'


def test_convert_from_bin():
    assert Number('1010', 2).convert(10) == '10'
    assert Number('1010', 2).convert(8) == '12'
    assert Number('1010', 2).convert(16) == 'A'
    assert Number('1010', 2).convert(32) == 'A'


def test_convert_from_oct():
    assert Number('12', 8).convert(10) == '10'
    assert Number('12', 8).convert(2) == '1010'
    assert Number('12', 8).convert(16) == 'A'
    assert Number('12', 8).convert(32) == 'A'


def test_convert_from_hex():
    assert Number('A', 16).convert(10) == '10'
    assert Number('A', 16).convert(2) == '1010'
    assert Number('A', 16).convert(8) == '12'
    assert Number('A', 16).convert(32) == 'A'


def test_convert_from_32():
    assert Number('10', 32).convert(10) == '32'
    assert Number('10', 32).convert(2) == '100000'
    assert Number('10', 32).convert(8) == '40'
    assert Number('10', 32).convert(16) == '20'


def test_convert_frac_from():
    assert Number('1010,10', 10).convert(2) == "1111110010.000110011"
    assert Number("5476,69", 10).convert(2) == "1010101100100.101100001"
    assert Number("5476,69", 10).convert(8) == "12544.5412172702"
    assert Number("67,65374", 10).convert(16) == "43.A75B813016"
    assert Number("67,65374", 10).convert(32) == "23.KTDO2C0M91"


def test_convert_frac_to_dec():
    assert Number("1111110010.000110011", 2).convert(10) == '1010.099609375'
    assert Number("5476,69", 10).convert(2) == "1010101100100.101100001"
    assert Number("5476,69", 10).convert(8) == "12544.5412172702"
    assert Number("67,65374", 10).convert(16) == "43.A75B813016"
    assert Number("67,65374", 10).convert(32) == "23.KTDO2C0M91"