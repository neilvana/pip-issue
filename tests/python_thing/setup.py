from setuptools import find_packages
from setuptools import setup


def get_global(file_name, global_name):
    """Read global_name from file."""
    import os
    globals = {}
    exec(open(os.path.join(os.path.dirname(__file__), "python_thing", file_name)).read(), globals)
    return globals[global_name]


setup(
    name=get_global("version.py", "__title__"),
    description=get_global("version.py", "__description__"),
    version=get_global("version.py", "__version__"),
    author=get_global("version.py", "__author__"),
    author_email=get_global("version.py", "__author_email__"),
    url=get_global("version.py", "__url__"),
    install_requires=[
    ],
    packages=find_packages(
        exclude=[
            "docs",
            "tests*"
        ]),
    package_data={
        "": [
        ],
    },
    entry_points={
        'console_scripts': [
            'python_thing=python_thing.mocks:main'
        ],
    },
)
