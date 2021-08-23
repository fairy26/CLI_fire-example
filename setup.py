from setuptools import setup

setup(
    name='fire-example-cli',
    install_requires = [
        'fire',
    ],
    entry_points={
        'console_scripts': [
            'zd = src:run'
        ]
    }
)