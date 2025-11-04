# ...existing code...
# System Modules
import sys
import os
import math

# Installed Modules
import pytest

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402


def test_area_of_circle_positive_radius():
    """Test with a positive radius."""
    # Arrange
    radius = 1

    # Act
    result = area_of_circle(radius)

    # Assert
    assert math.isclose(result, math.pi * 1 ** 2, rel_tol=1e-12)


def test_area_of_circle_zero_radius():
    """Test with a radius of zero."""
    # Arrange
    radius = 0

    # Act
    result = area_of_circle(radius)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    # Arrange
    n = 0

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_one():
    """Test with n=1."""
    # Arrange
    n = 1

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 1


def test_get_nth_fibonacci_ten():
    """Test with n=10."""
    # Arrange
    n = 10

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 55

# ...existing code...
# Added tests for better coverage

@pytest.mark.parametrize("radius", [0, 0.5, 2, 2.5, 10])
def test_area_of_circle_various_radii(radius):
    """Parametrized area_of_circle tests for ints and floats."""
    expected = math.pi * (radius ** 2)
    result = area_of_circle(radius)
    assert math.isclose(result, expected, rel_tol=1e-12)


def test_area_of_circle_negative_radius_raises():
    """area_of_circle should raise for negative radius."""
    with pytest.raises(ValueError):
        area_of_circle(-1)


def test_get_nth_fibonacci_parametrized_small():
    """Parametrized Fibonacci checks for small indices."""
    cases = [
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
        (15, 610),
    ]
    for n, expected in cases:
        assert get_nth_fibonacci(n) == expected


def test_get_nth_fibonacci_negative_raises():
    """get_nth_fibonacci should raise for negative n."""
    with pytest.raises(ValueError):
        get_nth_fibonacci(-5)


def test_get_nth_fibonacci_non_int_raises_typeerror():
    """Non-integer n should raise TypeError (range requires int)."""
    with pytest.raises(TypeError):
        get_nth_fibonacci(3.5)


def test_get_nth_fibonacci_larger_index():
    """Check a larger Fibonacci index for correctness/performance."""
    assert get_nth_fibonacci(20) == 6765
    assert get_nth_fibonacci(30) == 832040
# ...existing code...