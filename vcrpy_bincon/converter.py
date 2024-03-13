import base64
import gzip
import json
import os
import re
import sys

import ruamel.yaml

CASSETTE_DIR = sys.argv[1]


def main():
    for filename in os.listdir(CASSETTE_DIR):
        if filename.endswith(".yaml") or filename.endswith(".yml"):
            yaml = ruamel.yaml.YAML()
            filepath = os.path.join(CASSETTE_DIR, filename)

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


if __name__ == "__main__":
    main()
