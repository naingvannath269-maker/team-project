from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return the difference of two numbers."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return the product of two numbers."""
    return a * b


def divide(a: Number, b: Number) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


class Statistics:
    """Calculate basic statistics for a list of numbers."""

    def __init__(self, data: list[Number]) -> None:
        if not data:
            raise ValueError("Data list cannot be empty.")
        self.data = data

    def maximum(self) -> Number:
        return max(self.data)

    def minimum(self) -> Number:
        return min(self.data)

    def mean(self) -> float:
        return sum(self.data) / len(self.data)

    def range(self) -> Number:
        return self.maximum() - self.minimum()

    def __repr__(self) -> str:
        return f"Statistics(n={len(self.data)}, mean={self.mean():.2f})"
