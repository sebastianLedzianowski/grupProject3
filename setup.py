from setuptools import setup, find_namespace_packages

setup(
    name='grupProject3',
    version='0.1.0',
    packages=find_namespace_packages(),
    py_modules=['main'],
    install_requires=[
        'pymongo ',
        'faker',
        'secure-smtplib',
        'python-dotenv',
        'requests',

    ],
    entry_points={
        'console_scripts': [
            'grupProject3=main:main',
        ],
    },
)