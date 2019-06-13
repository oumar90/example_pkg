import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    


setuptools.setup(
    name="example_pkg",
    version="0.0.1",
    author="Example Athor",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oumar90/example_pkg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Progrmming Language :: Python :: 3",
        "License :: OSI Approuved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

