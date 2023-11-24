"""
uu_py_test_app setup
"""
from setuptools import setup

requirements = [
]

dev_requirements = [
    "pytest",
    "pytest-cov",
]

setup(
    name="uu_py_test_app",
    packages=["uu_py_test_app"],
    package_dir={"uu_py_test_app": "src"},
    # Dependencies
    install_requires=requirements,
    extras_require={
        "dev": dev_requirements
    },
)
