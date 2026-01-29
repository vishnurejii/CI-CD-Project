from travel_cost import calculate_trip_cost

def test_no_discount():
    assert calculate_trip_cost(5, 1000, 0) == 5000

def test_with_discount():
    assert calculate_trip_cost(4, 2000, 10) == 7200

def test_single_day_trip():
    assert calculate_trip_cost(1, 3000, 5) == 2850
