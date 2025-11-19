import argparse
import base64
import gzip
import json
import os
import re

from ruamel.yaml import YAML

from vcrpy_bincon._version import __version__


def convert_binary(cassette_dir: str) -> None:
    """Converts compressed, binary VCR responses into human-readable strings."""
    for filename in os.listdir(cassette_dir):
        if filename.endswith(".yaml") or filename.endswith(".yml"):
            yaml = YAML()
            filepath = os.path.join(cassette_dir, filename)

            with open(filepath, "r") as file:
                file_contents = file.read()
                if "!!binary |" not in file_contents:
                    continue
                data = re.sub(r"!!binary \|", "", file_contents)  # pre-process the yaml to get the original binary
                yaml_content = yaml.load(data)
                interactions = yaml_content.get("interactions", [])

                for index, interaction in enumerate(interactions):
                    response = interaction.get("response", {})
                    body = response.get("body", {})
                    string_key = body.get("string")

                    if string_key:
                        try:
                            # If we cannot decode the JSON, it needs conversion
                            json.loads(string_key)
                        except json.decoder.JSONDecodeError:
                            # Remove spaces to ensure we put the binary strings together completely
                            decoded_data = base64.b64decode(string_key.replace(" ", "").strip())
                            decompressed_data = gzip.decompress(decoded_data)
                            converted_string = json.dumps(json.loads(decompressed_data.decode()))
                            yaml_content["interactions"][index]["response"]["body"]["string"] = converted_string
                            print(f"Converted binary string for {filepath}")

            with open(filepath, "w") as file:
                yaml.dump(yaml_content, file)


def _cli():
    """Runs the tool from the CLI."""
    parser = argparse.ArgumentParser(
        description="Convert binary Python VCR cassette responses to human-readable strings."
    )
    parser.add_argument(
        "cassette_path",
        type=str,
        help="The path to the VCR cassette directory.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    args = parser.parse_args()
    convert_binary(args.cassette_path)


if __name__ == "__main__":
    _cli()
