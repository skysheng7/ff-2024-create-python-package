"""this script tests the functionationty of add_numbers.py"""


def test_import():
    """Test that the package can be imported."""
    import my_python_package  # noqa: F401


from my_python_package.add_numbers import add_numbers


def test_add_numbers():
    """Test that add numbers adds n umbers together correctly."""
    assert add_numbers(1, 2) == 3
