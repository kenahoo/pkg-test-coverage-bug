from setuptools import setup, find_packages


setup(
    name="test_pkg",
    python_requires='>=3.7',
    version='0.1',
    author="A. U. Thor <a.u.thor@a.galaxy.far.far.away>",
    description="My Pack",
    packages=find_packages(),
    install_requires=['more_itertools >= 8.10'],
    include_package_data=True
)
