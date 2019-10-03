import importlib
import numpy.testing as npt

country = importlib.import_module('.03_country-subset', 'notebooks')

# you might need to change the date so that it matches today's date
processed_data = "../data/processed/2019-10-03-winemag_Chile.csv"

def test_get_mean_price():
    mean_price = country.get_mean_price(processed_data)
    assert mean_price == 20.7865
    #gives us an option to see what happens here aswell
    npt.assert_allclose(country.get_mean_price(processed_data), 20.787, rtol = 0.01)
    