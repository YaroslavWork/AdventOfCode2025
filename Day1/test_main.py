from main import move_dial, check_how_many_times_dial_pointing_at_zero

def test_example():
    assert move_dial(is_left=True, to=68, start_position=50) == 82
    assert check_how_many_times_dial_pointing_at_zero(is_left=True, to=68, start_position=50) == 1
    assert move_dial(is_left=True, to=30, start_position=82) == 52
    assert check_how_many_times_dial_pointing_at_zero(is_left=True, to=30, start_position=82) == 0
    assert move_dial(is_left=False, to=48, start_position=52) == 0
    assert check_how_many_times_dial_pointing_at_zero(is_left=False, to=48, start_position=52) == 1
    assert move_dial(is_left=True, to=5, start_position=0) == 95
    assert check_how_many_times_dial_pointing_at_zero(is_left=True, to=5, start_position=0) == 0
    assert move_dial(is_left=False, to=60, start_position=95) == 55
    assert check_how_many_times_dial_pointing_at_zero(is_left=False, to=60, start_position=95) == 1
    assert move_dial(is_left=True, to=55, start_position=55) == 0
    assert check_how_many_times_dial_pointing_at_zero(is_left=True, to=55, start_position=55) == 1
    assert move_dial(is_left=True, to=1, start_position=0) == 99
    assert check_how_many_times_dial_pointing_at_zero(is_left=True, to=1, start_position=0) == 0
    assert move_dial(is_left=True, to=99, start_position=99) == 0
    assert check_how_many_times_dial_pointing_at_zero(is_left=True, to=99, start_position=99) == 1
    assert move_dial(is_left=False, to=14, start_position=0) == 14
    assert check_how_many_times_dial_pointing_at_zero(is_left=False, to=14, start_position=0) == 0
    assert move_dial(is_left=True, to=82, start_position=14) == 32
    assert check_how_many_times_dial_pointing_at_zero(is_left=True, to=82, start_position=14) == 1

def test_additional():
    assert check_how_many_times_dial_pointing_at_zero(is_left=False, to=100, start_position=0) == 1
    assert check_how_many_times_dial_pointing_at_zero(is_left=True, to=1, start_position=0) == 0
    assert check_how_many_times_dial_pointing_at_zero(is_left=True, to=1, start_position=2) == 0
    assert check_how_many_times_dial_pointing_at_zero(is_left=True, to=1, start_position=1) == 1
    assert check_how_many_times_dial_pointing_at_zero(is_left=False, to=1, start_position=99) == 1
    assert check_how_many_times_dial_pointing_at_zero(is_left=False, to=1, start_position=98) == 0
    assert check_how_many_times_dial_pointing_at_zero(is_left=True, to=100, start_position=1) == 1
    assert move_dial(is_left=False, to=100, start_position=0) == 0
    assert move_dial(is_left=True, to=1, start_position=0) == 99