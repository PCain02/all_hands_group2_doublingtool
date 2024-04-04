"""Conduct experiments to evaluate performance of list concatenation."""

# ruff: noqa: PLR0913

import typer
from rich.console import Console

from algorithims import approach, functioncall, sortingfunctions
import doubling

# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a console for display of rich text
console = Console()


# file_name: str,function_name: str,starting_size: int,runs: int,sorting_algorithm: str,):
@cli.command()
def main(
    file_path: str = typer.Option(...),
    function_name: str = typer.Option(...),
    starting_size: int = typer.Option(1000),
    runs: int = typer.Option(10),
    sorting_algorithm: approach.Sortingapproach = typer.Option(...),
):
    """Function for main"""
    """Evaluate the performance of list operations."""
    # display details about the configuration of the benchmarking tool
    typer.echo(f"File path: {file_path}")
    typer.echo(f"Function name: {function_name}")
    typer.echo(f"Starting size: {starting_size}")
    typer.echo(f"Number of runs: {runs}")
    typer.echo(f"Sorting algorithm: {sorting_algorithm}")
    # perform the benchmarking operation
    benchmark_data = doubling.doubling(
        file_path, function_name, starting_size, runs, sorting_algorithm
    )
    console.print()
    # display the results concerning the minimum execution time
