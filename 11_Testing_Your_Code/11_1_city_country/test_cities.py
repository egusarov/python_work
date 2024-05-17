from city_functions import city_country


def test_city_country():
    """Test a single string of the form City, Country, such as Santiago, Chile"""
    formatted = city_country('santiago', 'chile')
    assert formatted == 'Santiago, Chile'