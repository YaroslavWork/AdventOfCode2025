from main import move_dial, is_pointing_to_zero

def test_example():
    assert move_dial(is_left=True, to=68, start_position=50) == 82
    assert is_pointing_to_zero(dial_position=82) == False
    assert move_dial(is_left=True, to=30, start_position=82) == 52
    assert is_pointing_to_zero(dial_position=52) == False
    assert move_dial(is_left=False, to=48, start_position=52) == 0
    assert is_pointing_to_zero(dial_position=0) == True
    assert move_dial(is_left=True, to=5, start_position=0) == 95
    assert is_pointing_to_zero(dial_position=95) == False
    assert move_dial(is_left=False, to=60, start_position=95) == 55
    assert is_pointing_to_zero(dial_position=55) == False
    assert move_dial(is_left=True, to=55, start_position=55) == 0
    assert is_pointing_to_zero(dial_position=0) == True
    assert move_dial(is_left=True, to=1, start_position=0) == 99
    assert is_pointing_to_zero(dial_position=99) == False
    assert move_dial(is_left=True, to=99, start_position=99) == 0
    assert is_pointing_to_zero(dial_position=0) == True
    assert move_dial(is_left=False, to=14, start_position=0) == 14
    assert is_pointing_to_zero(dial_position=14) == False
    assert move_dial(is_left=True, to=82, start_position=14) == 32
    assert is_pointing_to_zero(dial_position=32) == False