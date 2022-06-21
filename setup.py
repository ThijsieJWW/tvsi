import json
import os
from setuptools import setup


def get_version(file="tvsi/version") -> str:
    with open(os.path.join(os.path.dirname(__file__), file), "r+") as f:
        version = json.load(f)
        version["build"] += 1
        json.dump(version, f)

    return f"{version['major']}.{version['minor']}.{version['patch']} build {version['build']}"


setup(
    name="tvsi",
    version=get_version(),
    author="Thijs van Straaten",
    description="tvs Interpreter",
    include_package_data=True,
    entry_points={"console_scripts": ["tvsi=tvsi.command_line:main"]},
)
