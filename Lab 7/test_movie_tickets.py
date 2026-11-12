
from hypothesis import given, strategies as st
from movie_tickets import parse_seat, total_price, average_rating


@given(st.one_of(st.text(), st.none()))
def test_parse_seat_no_crash(s):
    parse_seat(s)


@given(st.one_of(st.text(), st.none()))
def test_total_price_no_crash(s):
    total_price(s)


@given(st.one_of(st.text(), st.none()))
def test_average_rating_no_crash(s):
    average_rating(s)
