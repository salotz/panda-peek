from setuptools import setup, find_packages

setup(
    name='panda-peek',
    version='0.1',
    py_modules=['peek'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'Pandas',
    ],
    entry_points={
        'console_scripts' : [
            "peek = peek.cli:peek"]}

)
