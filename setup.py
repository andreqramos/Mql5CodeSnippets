import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='Mql5CodeSnippets',
    version='0.0.1',
    description='Mql5CodeSnippets',
    install_requires=[],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)

