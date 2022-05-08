from setuptools import setup

with open('README.md', 'r') as f:
    long_desc = f.read()


setup(
    name='convertable',
    version='0.0.1',
    description='A package for converting data in images to pandas DataFrames',
    long_description=long_desc,
    license='MIT',
    author='Gibril Gaye, Modou Lamin Manjang',
    author_email='g.gibril97@gmail.com, manjangmodoulamin190@gmail.com'
)
