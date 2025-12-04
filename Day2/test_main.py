from main import find_pattern_between_ranges, has_pattern

def test_example():
    assert find_pattern_between_ranges(begin=11, end=22) == [11, 22]
    assert find_pattern_between_ranges(begin=95, end=115) == [99, 111]
    assert find_pattern_between_ranges(begin=998, end=1012) == [999, 1010]
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
    assert find_pattern_between_ranges(
        begin=565653,
        end=565659
    ) == [565656]
    assert find_pattern_between_ranges(
        begin=824824821,
        end=824824827
    ) == [824824824]
    assert find_pattern_between_ranges(
        begin=2121212118,
        end=2121212124
    ) == [2121212121]
    

def test_additional():
    assert find_pattern_between_ranges(begin=3, end=20) == [11]
    assert find_pattern_between_ranges(begin=62668, end=105646) == [
        66666,
        77777,
        88888,
        99999,
        100100,
        101010, 
        101101,
        102102,
        103103,
        104104,
        105105
    ]
    assert has_pattern(3) == False
    assert has_pattern(99) == True
    assert has_pattern(83398339) == True
    assert has_pattern(446443) == False
    assert has_pattern(446446) == True
    assert has_pattern(77777777) == True