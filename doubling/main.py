"""Conduct experiments to evaluate performance of list concatenation."""

# ruff: noqa: PLR0913

import typer
from rich.console import Console

from doubling import sortingfunctions
from doubling import benchmark

# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a console for display of rich text
console = Console()


# file_name: str,function_name: str,starting_size: int,runs: int,sorting_algorithm: str,):
@cli.command()
def main(
    starting_size: int = typer.Option(1000),
    runs: int = typer.Option(10),
    file_path: str = typer.Option(..., "--file_path", "-f", help="Path to the file containing sorting functions"),
    sorting_algorithm: str = typer.Option("bubblesort"),
) -> None:
    """Evaluate the performance of list operations."""
    # display details about the configuration of the benchmarking tool
    # typer.echo(f"File path: {file_path}")
    # typer.echo(f"Function name: {function_name}")
    typer.echo(f"Starting size: {starting_size}")
    typer.echo(f"Number of runs: {runs}")
    typer.echo(f"File Path: {file_path}")
    typer.echo(f"Sorting algorithm: {sorting_algorithm}")
    # perform the benchmarking operation
    benchmark_data = benchmark.doublingfunction(starting_size, runs, file_path, sorting_algorithm)
    # display the results concerning the minimum execution time


if __name__ == "__main__":
    cli()
