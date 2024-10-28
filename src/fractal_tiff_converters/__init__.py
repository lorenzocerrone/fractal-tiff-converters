"""
A basic TIFF to OME-Zarr converter
"""
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("fractal-tiff-converters")
except PackageNotFoundError:
    __version__ = "uninstalled"