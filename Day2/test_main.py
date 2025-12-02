from main import find_pattern_between_ranges

def test_example():
    assert find_pattern_between_ranges(begin=11, end=22) == [11, 22]
    assert find_pattern_between_ranges(begin=95, end=115) == [99]
    assert find_pattern_between_ranges(begin=998, end=1012) == [1010]
    assert find_pattern_between_ranges(
        begin=1188511880,
        end=1188511890
    ) == [1188511885]
    assert find_pattern_between_ranges(
        begin=222220, 
        end=222224
    ) == [222222]
    assert find_pattern_between_ranges(begin=1698522, end=1698528) == []
    assert find_pattern_between_ranges(
        begin=446443,
        end=446449
    ) == [446446]
    assert find_pattern_between_ranges(
        begin=38593856,
        end=38593862
    ) == [38593859]
    assert find_pattern_between_ranges(begin=565653, end=565659) == []
    assert find_pattern_between_ranges(
        begin=824824821,
        end=824824827
    ) == []
    assert find_pattern_between_ranges(
        begin=2121212118,
        end=2121212124
    ) == []