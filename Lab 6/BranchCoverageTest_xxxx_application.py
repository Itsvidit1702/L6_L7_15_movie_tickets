import pytest
from movie_tickets import ticket_price, group_discount, snack_combo


def test_ticket_price_valid_seats():
    assert ticket_price("regular", 25, 15, False) == 150
    assert ticket_price("premium", 25, 10, False) == 200
    assert ticket_price("recliner", 25, 20, True) == 470


def test_ticket_price_time_rules():
    assert ticket_price("regular", 25, 9, False) == 100
    assert ticket_price("regular", 25, 18, False) == 180
    assert ticket_price("regular", 25, 15, False) == 150


def test_ticket_price_weekend():
    assert ticket_price("regular", 25, 15, True) == 190


def test_ticket_price_age_rules():
    assert ticket_price("regular", 2, 15, False) == 0
    assert ticket_price("regular", 10, 15, False) == 75
    assert ticket_price("regular", 65, 15, False) == 75
    assert ticket_price("regular", 25, 15, False) == 150


def test_ticket_price_invalid_seat():
    with pytest.raises(ValueError, match="unknown seat"):
        ticket_price("vip", 25, 15, False)


@pytest.mark.parametrize("hour", [-1, 24])
def test_ticket_price_invalid_time(hour):
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, hour, False)


def test_group_discount_no_tickets():
    with pytest.raises(ValueError, match="no tickets"):
        group_discount(0, False)


def test_group_discount_ranges():
    assert group_discount(2, False) == 0
    assert group_discount(5, False) == 10
    assert group_discount(10, False) == 15


def test_group_discount_student_bonus():
    assert group_discount(5, True) == 15
    assert group_discount(10, True) == 20
    assert group_discount(2, True) == 0


def test_snack_combo_sizes():
    assert snack_combo("small", False) == 120
    assert snack_combo("medium", False) == 180
    assert snack_combo("large", False) == 250


def test_snack_combo_coupon():
    assert snack_combo("small", True) == 70
    assert snack_combo("medium", True) == 130
    assert snack_combo("large", True) == 200