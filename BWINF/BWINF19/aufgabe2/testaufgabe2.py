import solution
from solution import *
# Test function is2bit_string_similar
def test_is2bit_string_similar():
    assert is2bit_string_similar("0000", "0001") == True
    assert is2bit_string_similar("0000", "1000") == True
    assert is2bit_string_similar("0000", "0100") == True
    assert is2bit_string_similar("0000", "0010") == True
    assert is2bit_string_similar("0000", "0000") == True
    assert is2bit_string_similar("0?00", "1001") == False
#   True Cases
    assert is2bit_string_similar("0?00", "0000") == True
    assert is2bit_string_similar("0?00", "1000") == False
    assert is2bit_string_similar("0?00", "0100") == True
    assert is2bit_string_similar("0?00", "0010") == False
    assert is2bit_string_similar("0?00", "0001") == False
test_is2bit_string_similar()

#Test function search_bit_string
def test_search_bit_string():
    assert search_bit_string("0?00") == ['pic1.png', 'pic5.png']

test_search_bit_string()

#Test function complete_bit_string
def test_complete_bit_string():
    assert complete_bit_string(["0011", "0110"]) != ['pic4.png', 'pic4.png', 'pic14.png', 'pic7.png']
    assert complete_bit_string(["0011", "0110"]) == ['pic4.png', 'pic8.png', 'pic10.png', 'pic7.png']