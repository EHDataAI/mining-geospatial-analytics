"""Quality checks for the public LAB04 executed notebook."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

NOTEBOOK = (
    ROOT
    / "labs"
    / "lab04_geochemical_coda"
    / "04_geochemical_coda.ipynb"
)


def load_notebook() -> dict:
    """Load the public notebook as UTF-8 JSON."""
    text = NOTEBOOK.read_text(encoding="utf-8")
    return json.loads(text)


def test_lab04_notebook_exists() -> None:
    """The recruiter-facing LAB04 notebook must exist."""
    assert NOTEBOOK.is_file()


def test_lab04_notebook_structure() -> None:
    """The public notebook must retain its validated cell structure."""
    notebook = load_notebook()

    cells = notebook["cells"]

    assert len(cells) == 45

    markdown_cells = [
        cell
        for cell in cells
        if cell["cell_type"] == "markdown"
    ]

    code_cells = [
        cell
        for cell in cells
        if cell["cell_type"] == "code"
    ]

    assert len(markdown_cells) == 21
    assert len(code_cells) == 24


def test_lab04_notebook_has_no_error_outputs() -> None:
    """The executed public notebook must contain no error outputs."""
    notebook = load_notebook()

    errors = []

    for cell in notebook["cells"]:
        if cell["cell_type"] != "code":
            continue

        for output in cell.get("outputs", []):
            if output.get("output_type") == "error":
                errors.append(output)

    assert errors == []


def test_lab04_all_code_cells_are_executed() -> None:
    """Every non-empty public code cell must have an execution count."""
    notebook = load_notebook()

    unexecuted = []

    for index, cell in enumerate(notebook["cells"]):
        if cell["cell_type"] != "code":
            continue

        source = cell.get("source", [])

        if isinstance(source, list):
            source = "".join(source)

        if not source.strip():
            continue

        if cell.get("execution_count") is None:
            unexecuted.append(index)

    assert unexecuted == []


def test_lab04_notebook_contains_graphics() -> None:
    """The public notebook must retain its graphical evidence."""
    notebook = load_notebook()

    png_outputs = 0

    for cell in notebook["cells"]:
        if cell["cell_type"] != "code":
            continue

        for output in cell.get("outputs", []):
            data = output.get("data", {})

            if isinstance(data, dict) and "image/png" in data:
                png_outputs += 1

    assert png_outputs >= 10


def test_lab04_notebook_unicode_integrity() -> None:
    """The public notebook must remain UTF-8 clean."""
    raw = NOTEBOOK.read_bytes()

    assert not raw.startswith(b"\xef\xbb\xbf")

    text = raw.decode("utf-8")

    assert "\ufffd" not in text

    notebook = json.loads(text)

    for cell in notebook["cells"]:
        source = cell.get("source", [])

        if isinstance(source, list):
            source = "".join(source)

        assert "?" not in source
