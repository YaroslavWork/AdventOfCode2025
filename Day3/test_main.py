from main import find_the_highest_combination

def test_example():
    assert find_the_highest_combination("987654321111111") == 98
    assert find_the_highest_combination("811111111111119") == 89
    assert find_the_highest_combination("234234234234278") == 78
    assert find_the_highest_combination("818181911112111") == 92

    assert find_the_highest_combination("987654321111111", max_digit=12)\
        == 987654321111
    assert find_the_highest_combination("811111111111119", max_digit=12)\
        == 811111111119
    assert find_the_highest_combination("234234234234278", max_digit=12)\
        == 434234234278
    assert find_the_highest_combination("818181911112111", max_digit=12)\
        == 888911112111