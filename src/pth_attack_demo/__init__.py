from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("pth_attack_demo")
except PackageNotFoundError:
    __version__ = "0.0.0"