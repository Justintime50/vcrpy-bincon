<div align="center">

# VCRPY Binary Converter

Convert binary Python VCR cassette responses to human-readable strings.

[![Build Status](https://github.com/Justintime50/vcrpy-bincon/workflows/build/badge.svg)](https://github.com/Justintime50/vcrpy-bincon/actions)
[![Coverage Status](https://img.shields.io/codecov/c/github/justintime50/vcrpy-bincon)](https://app.codecov.io/github/Justintime50/vcrpy-bincon)
[![PyPi](https://img.shields.io/pypi/v/vcrpy-bincon)](https://pypi.org/project/vcrpy-bincon)
[![Licence](https://img.shields.io/github/license/Justintime50/vcrpy-bincon)](LICENSE)

<img src="https://raw.githubusercontent.com/justintime50/assets/main/src/vcrpy-bincon/showcase.png" alt="Showcase">

</div>

VCR cassette responses often get saved as binary instead of a human-readable string. This makes inspecting the content difficult and depending on the VCR configuration, cassette matching impossible. This tool takes in a cassette directory and converts all binary response interactions to a human-readable string before dumping the yaml back to the cassette file. This allows for devs to properly inspect their cassette content while retaining all the original data - super useful if switching your VCR config from binary to strings.

```yaml
# Takes something like the following from a vcrpy cassette:
interactions:
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAAA4yRT0vEMBDFv0rJ1RaS/rc3xYJCVxZ3XfBUps0UI21a0lTUZb+7k0ovnvY4j997
        byY5MyVZwUCaOm8kZEkEaZwJIRChyXIedk2eAEb8VjCfjc0Htpb4OykNzjNJrUGwKGtwcsjDKBA8
        4OlRZEWSFFF0w3nBOYHLJK8DNQxISFmdng6uYBwm0N+s0Evf+2y2BtEKAqIsjb2V8vYv5aEq37z7
        6vTANiYkxvmVJTPblbv94xo4W9qDlOMzDT9qclG5EGkQC56uhYu2xnleHT69jxq3dhxA9dswjNLl
        TGaUS2vVqJ0ZjFFo6g5a1a/Nfyy9lpKorQKyW7OgzzqUaKCvLXzV7hO2+2i7f9onGtWpFlzHzIrz
        5fILAAD//wMAxbg+BbcBAAA=

# And turns it into this:
interactions:
  response:
    body:
      string: '{"id": "adr_8bda753a647111eeab7802fb85ae3091", "object": "Address",
        "created_at": "2023-10-06T17:55:33+00:00", "updated_at": "2023-10-06T17:55:33+00:00",
        "name": "ELVIS", "company": null, "street1": "3764 ELVIS PRESLEY BLVD", "street2":
        "", "city": "MEMPHIS", "state": "TN", "zip": "38116-4106", "country": "US",
        "phone": null, "email": null, "mode": "production", "carrier_facility": null,
        "residential": true, "federal_tax_id": null, "state_tax_id": null, "verifications":
        {}}'
```

## Install

```bash
# Homebrew install
brew tap justintime50/formulas
brew install vcrpy-bincon

# Pip install
pip3 install vcrpy-bincon

# Install locally
just install
```

## Usage

```bash
# Specify the directory where your cassette files live as the first param
vcrpy-bincon tests/cassettes
```

### Known Side Effects

Using this tool has a couple of known (low-impact) side effects:

1. `null` fields in cassettes may get replaced with nothing and become empty
2. Some already human-readable strings may get re-encoded as escaped JSON strings if VCRPY had odd line breaks such as the ending quote on a newline with no other content
3. Long URL and other field values may get bumped down a line from its key pair due to the default line length of 80

## Development

```bash
# Get a comprehensive list of development tools
just --list
```
