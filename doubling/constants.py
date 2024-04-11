"""Define constants with dataclasses."""

from dataclasses import dataclass
from enum import Enum


# Benchmark values constant
@dataclass(frozen=True)
class DoublingBenchmarkValues:
    """Define the BenchmarkValues dataclass for constant(s)."""

    num_runs: int
    start_size: int
    max_size: int
    min_size: int
    max_value: int
    min_value: int


doubling_benchmark_values = DoublingBenchmarkValues(
    num_runs=10,
    start_size=1000,
    max_size=1000000,
    min_size=100,
    max_value=10000,
    min_value=0,
)