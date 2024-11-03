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