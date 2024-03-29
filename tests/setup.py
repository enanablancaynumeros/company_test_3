from setuptools import setup, find_packages

setup(
    name='test_package',
    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.1.0',
    author='Yeray Alvarez Romero',
    author_email='yeray.alvarez.romero@gmail.com',
    include_package_data=True,
    packages=find_packages(exclude=['docs', 'tests*']),
)
