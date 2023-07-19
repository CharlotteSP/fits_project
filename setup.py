from setuptools import setup, find_packages

setup(
    name="cmdfits",
    version="1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "cmdfits = cmdfits.cmdfits:run_cli_script",
        ]
    },
)
