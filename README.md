<div align="center">

# VCRPY Binary Converter

Convert binary Python VCR cassette responses to human-readable strings.

[![Build Status](https://github.com/Justintime50/vcrpy-bincon/workflows/build/badge.svg)](https://github.com/Justintime50/vcrpy-bincon/actions)
[![Coverage Status](https://coveralls.io/repos/github/Justintime50/vcrpy-bincon/badge.svg?branch=main)](https://coveralls.io/github/Justintime50/vcrpy-bincon?branch=main)
[![PyPi](https://img.shields.io/pypi/v/vcrpy-bincon)](https://pypi.org/project/vcrpy-bincon)
[![Licence](https://img.shields.io/github/license/Justintime50/vcrpy-bincon)](LICENSE)

<img src="https://raw.githubusercontent.com/justintime50/assets/main/src/vcrpy-bincon/showcase.png" alt="Showcase">

</div>

VCR cassette responses often get saved as binary instead of a human-readable string. This makes inspecting the content difficult and depending on the VCR configuration, cassette matching impossible. This tool takes in a cassette directory and converts all binary response interactions to a human-readable string before dumping the yaml back to the cassette file. This allows for devs to properly inspect their cassette content while retaining all the original data - super useful if switching your VCR config from binary to strings.

## Install

```bash
# Install tool
pip3 install vcrpy_bincon

# Install locally
just install
```

## Usage

```bash
CASSETTE_DIR=tests/cassettes venv/bin/python vcrpy_bincon/converter.py
```

## Development

```bash
# Get a comprehensive list of development tools
just --list
```
