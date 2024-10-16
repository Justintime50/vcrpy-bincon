import re

import setuptools


with open('README.md', 'r') as readme_file:
    long_description = readme_file.read()

# Inspiration: https://stackoverflow.com/a/7071358/6064135
with open('vcrpy_bincon/_version.py', 'r') as version_file:
    version_groups = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
    if version_groups:
        version = version_groups.group(1)
    else:
        raise RuntimeError('Unable to find version string!')

REQUIREMENTS = [
    'ruamel.yaml == 0.18.*',
]

DEV_REQUIREMENTS = [
    'bandit == 1.7.*',
    'black == 24.*',
    'build == 1.1.*',
    'flake8 == 7.*',
    'isort == 5.*',
    'mypy == 1.12.*',
    'pytest == 8.*',
    'pytest-cov == 5.*',
]

setuptools.setup(
    name='vcrpy-bincon',
    version=version,
    description='Convert binary Python VCR cassette responses to human-readable strings.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/Justintime50/vcrpy-bincon',
    author='Justintime50',
    license='MIT',
    packages=setuptools.find_packages(
        exclude=[
            'examples',
            'test',
        ]
    ),
    package_data={
        'vcrpy_bincon': [
            'py.typed',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIREMENTS,
    extras_require={
        'dev': DEV_REQUIREMENTS,
    },
    entry_points={
        'console_scripts': [
            'vcrpy-bincon=vcrpy_bincon.converter:_cli',
        ]
    },
    python_requires='>=3.8, <4',
)
