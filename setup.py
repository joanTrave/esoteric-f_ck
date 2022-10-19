import pathlib

from setuptools import setup

README = (pathlib.Path(__file__).resolve().parent / "README.md").read_text()

setup(
    name="esoteric-f_ck",
    version="1.0.0",
    description="Interpreter for brainf*uck like esoteric programming languages",
    python_requires=">=3.10",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Joan Travé",
    author_email="joantrave@proton.me",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["esoteric-f_ck"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "esoteric=interpreter.__main__:main",
        ],
    },
    project_urls={
        "Source": "https://github.com/joanTrave/esoteric-f_ck",
    },
)
