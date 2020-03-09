from setuptools import setup, find_packages

setup(
    name='BokehStructGraph',
    py_modules = ['BokehStructGraph'],
    version="0.2",
    author="Jeremy Teitelbaum",
    author_email="jeremy.teitelbaum@uconn.edu",
    description="Create the structure graph of a bokeh model",
    url="https://github.com/jeremy9959/BokehStructureGraph",
    packages=find_packages(),
    python_requires='>=3.6',
)
