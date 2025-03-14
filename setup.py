from setuptools import setup, find_packages
from pathlib import Path
# Read the README file for the long description
long_description = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")

setup(
    name='uniquedatavalidatortool',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    author='Khadijat Agboola',
    author_email='khadijahagboola12@gmail.com',
    description='A simple data validation package',
    long_description=long_description,
    long_description_content_type="text/markdown",
)