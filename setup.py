from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='tracardi-python-sdk',
    version='0.6.2',
    description='Tracardi Customer Data Platform SDK',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Risto Kowaczewski',
    author_email='risto.kowaczewski@gmail.com',
    packages=['tracardi'],
    install_requires=[
        'pydantic',
        'aiohttp',
        'aiohttp[speedups]',
        'requests'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=['tracardi'],
    include_package_data=True,
    python_requires=">=3.8",
)
