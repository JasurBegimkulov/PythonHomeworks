import math

class Vector:
    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f"Vector{self.components}"

    def __add__(self, other):
        self._check_dimension(other)
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        self._check_dimension(other)
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        if isinstance(other, Vector):
            self._check_dimension(other)
            return sum(a * b for a, b in zip(self.components, other.components))  # Dot product
        return Vector(*(a * other for a in self.components))  # Scalar multiplication

    def __rmul__(self, other):
        return self * other  # Scalar multiplication from left side

    def magnitude(self):
        return math.sqrt(sum(a**2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*(a / mag for a in self.components))

    def _check_dimension(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions.")