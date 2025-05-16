import pathlib

ROOT = pathlib.Path(__file__).absolute().parent

assert (ROOT / "dist/package1-1.0.msix").exists()
