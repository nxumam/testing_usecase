"""mypackage — a simple example module for import in notebooks."""

__version__ = "0.1.0"

def greet(name: str = "world") -> str:
    return f"Hello, {name}!"

def add(a: float, b: float) -> float:
    return a + b
