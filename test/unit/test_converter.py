import os
import shutil

import pytest

from vcrpy_bincon.converter import convert_binary


CASSETTE_DIR = "test/cassettes"
YAML_CONTENT = """interactions:
- request:
    body: '{"city": "MEMPHIS", "company": null, "country": "US", "email": null, "mode":
      "production", "name": "ELVIS", "phone": null, "residential": true, "state":
      "TN", "street1": "3764 ELVIS PRESLEY BLVD", "street2": "", "zip": "38116-4106"}'
    headers: {}
    method: POST
    uri: http://127.0.0.0:5000/some/endpoint
  response:
    body:
      string: !!binary |
        H4sIAAAAAAAAA4yRT0vEMBDFv0rJ1RaS/rc3xYJCVxZ3XfBUps0UI21a0lTUZb+7k0ovnvY4j997
        byY5MyVZwUCaOm8kZEkEaZwJIRChyXIedk2eAEb8VjCfjc0Htpb4OykNzjNJrUGwKGtwcsjDKBA8
        4OlRZEWSFFF0w3nBOYHLJK8DNQxISFmdng6uYBwm0N+s0Evf+2y2BtEKAqIsjb2V8vYv5aEq37z7
        6vTANiYkxvmVJTPblbv94xo4W9qDlOMzDT9qclG5EGkQC56uhYu2xnleHT69jxq3dhxA9dswjNLl
        TGaUS2vVqJ0ZjFFo6g5a1a/Nfyy9lpKorQKyW7OgzzqUaKCvLXzV7hO2+2i7f9onGtWpFlzHzIrz
        5fILAAD//wMAxbg+BbcBAAA=
    headers:
      Cache-Control:
      - private, no-cache, no-store
      Connection:
      - close
      Content-Encoding:
      - gzip
      Content-Type:
      - application/json; charset=utf-8
      ETag:
      - W/"123"
      Expires:
      - '0'
      Location:
      - /some/endpoint/123
      Pragma:
      - no-cache
      Referrer-Policy:
      - strict-origin-when-cross-origin
      Transfer-Encoding:
      - chunked
      X-Content-Type-Options:
      - nosniff
      X-Download-Options:
      - noopen
      X-Frame-Options:
      - SAMEORIGIN
      X-Node:
      - dev
      X-Permitted-Cross-Domain-Policies:
      - none
      X-Runtime:
      - '0.049858'
      X-XSS-Protection:
      - 1; mode=block
    status:
      code: 201
      message: Created
version: 1
"""
NO_BINARY_YAML_CONTENT = """interactions:
- request:
    body: null
    headers: {}
    method: POST
    uri: http://127.0.0.0:5000/some/endpoint
  response:
    body:
      string: '{"hello": "world"}'
"""


@pytest.fixture(autouse=True)
def setup_test():
    """Setup test by creating dirs, adding various kinds of files, and cleaning up after."""
    os.makedirs(CASSETTE_DIR, exist_ok=True)

    # Create our valid test subject
    with open(f"{CASSETTE_DIR}/test.yaml", "w") as yaml_file:
        yaml_file.write(YAML_CONTENT)

    # Setup a yaml file without binary
    with open(f"{CASSETTE_DIR}/no_binary.yaml", "w") as yaml_file:
        yaml_file.write(NO_BINARY_YAML_CONTENT)

    # Add non-yaml files
    with open(f"{CASSETTE_DIR}/random.txt", "w") as text_file:
        text_file.write("random text that should get skipped since this is not a yaml file")

    yield
    shutil.rmtree(CASSETTE_DIR)


def test_convert_binary():
    """Ensure we find content that only exists in a human-readable response and no binary yaml tags."""
    convert_binary(CASSETTE_DIR)

    with open(f"{CASSETTE_DIR}/test.yaml", "r") as yaml_file:
        yaml_content = yaml_file.read()

    assert "adr_8bda753a647111eeab7802fb85ae3091" in yaml_content
    assert "!!binary |" not in yaml_content
