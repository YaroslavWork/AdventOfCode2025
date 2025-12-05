from main import is_this_number_inside_of_ranges

def test_example():
    ranges = [[3, 5], [10, 14], [16, 20], [12, 18]]
    
    assert is_this_number_inside_of_ranges(ranges, 1) == False
    assert is_this_number_inside_of_ranges(ranges, 5) == True
    assert is_this_number_inside_of_ranges(ranges, 8) == False
    assert is_this_number_inside_of_ranges(ranges, 11) == True
    assert is_this_number_inside_of_ranges(ranges, 17) == True
    assert is_this_number_inside_of_ranges(ranges, 32) == False