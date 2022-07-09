from importlib_metadata import entry_points
from setuptools import find_packages, setup

setup(
    name = "gitbees II",
    version = "1.0",
    author = "Marcello B.",
    packages = find_packages(),
    entry_points = """
    [console_scripts]
    gitbees=gitbees:runGitBees
    """
)