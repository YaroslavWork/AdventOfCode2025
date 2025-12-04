from main import find_the_highest_combination

def test_example():
    assert find_the_highest_combination("987654321111111") == 98
    assert find_the_highest_combination("811111111111119") == 89
    assert find_the_highest_combination("234234234234278") == 78
    assert find_the_highest_combination("818181911112111") == 92