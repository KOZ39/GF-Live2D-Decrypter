from setuptools import setup

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gflive2d',
    version='0.1.2',
    description="Girls' Frontline Live2D Decrypter",
    url='https://github.com/KOZ39/GF-Live2D-Decrypter',
    author='KOZ39',
    license='MIT',
    long_description=long_description,
    py_modules=['gflive2d']
)
