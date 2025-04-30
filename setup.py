from setuptools import setup, find_packages

setup(
    name='theta',
    year='2025',
    version='0.3',
    packages=find_packages(exclude=['tests*']),
    license='GPL-3.0',
    description='A collection of sequences and sequence operations',
    long_description=open('README.txt').read(),
    install_requires=[],
    url='https://github.com/Y108/theta',
    author='Y108',
    author_email='',
    python_requires='>=3.8',
)
