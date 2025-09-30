"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""
import pytest
from src.calculator import add, subtract, multiply, divide, power

class TestBasicOperations:
    """Test basic arithmetic operations"""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

    def test_add_negative_numbers(self):
        assert add(-1, -1) == -2
        assert add(-5, 3) == -2

    def test_subtract_negative_numbers(self):
        assert subtract(-1, -1) == 0
        assert subtract(-5, -3) == -2

class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""
    
    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")
    
    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)

# TODO: Students will add TestMultiplyDivide class

class TestPower:
    def test_power_basic(self):
        assert power(2, 3) == 8
        assert power(5, 0) == 1
        assert power(9, 0.5) == 3  # square root

    def test_power_negative_exponent(self):
        assert power(2, -2) == 0.25

    def test_power_invalid_inputs(self):
        import pytest
        with pytest.raises(TypeError, match="Power requires numeric inputs"):
            power("2", 3)
        with pytest.raises(TypeError, match="Power requires numeric inputs"):
            power(2, "3")

class TestMultiplyDivide:

    def test_multiply_basic(self):
        assert multiply(3, 4) == 12
        assert multiply(-2, 5) == -10
        assert multiply(2.5, 2) == 5.0

    def test_divide_basic(self):
        assert divide(8, 2) == 4
        assert divide(-9, 3) == -3
        assert divide(7.5, 2.5) == 3.0

    def test_divide_by_zero(self):
        import pytest
        with pytest.raises(ValueError, match="divide .* by zero"):
            divide(5, 0)
