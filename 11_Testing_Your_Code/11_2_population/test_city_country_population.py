from city_functions import city_country


def test_city_country():
    """Test a single string of the form such as Santiago, Chile"""
    formatted = city_country('santiago', 'chile')
    assert formatted == 'Santiago, Chile'


def test_city_country_population():
    """Test a single string of the form such as Santiago, Chile – population 5000000"""
    formatted = city_country('santiago', 'chile', population=5000000)
    assert formatted == 'Santiago, Chile - population 5000000'