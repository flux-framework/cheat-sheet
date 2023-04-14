# Read in data, ensure formatted correctly.
# Copyright @vsoch, 2023

import os
import shutil
import yaml
import jsonschema
import sys

here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
schema_url = "http://json-schema.org/draft-07/schema"


commandSchema = {
    "type": "object",
    "required": ["title", "command"],
    "additionalProperties": False,
    "properties": {
        "title": {"type": "string"},
        "command": {"type": "string"},
        "last": {"type": "boolean"},
    },
}

groupSchema = {
    "type": "object",
    "required": ["name", "items"],
    "properites": {
        "name": {"type": "string"},
        "items": {"type": "array", "items": commandSchema},
    },
}

schemaProperties = {
    "commands": {
        "type": "array",
        "items": {
            "type": "object",
            "required": [
                "name",
                "groups",
            ],
            "additionalProperties": False,
            "properties": {
                "name": {"type": "string"},
                "groups": {"type": "array", "items": groupSchema},
            },
        },
    },
}

schema = {
    "$schema": schema_url,
    "title": "Jobs Commands Schema",
    "type": "object",
    "required": [
        "commands",
    ],
    "properties": schemaProperties,
    "additionalProperties": False,
}


def get_filepath(filename):
    """
    load the jobs file.
    """
    filepath = os.path.join(os.path.dirname(here), "_data", filename)

    # Exit on error if we cannot find file
    if not os.path.exists(filepath):
        sys.exit("Cannot find %s" % filepath)

    return filepath


def read_commands(filepath):
    """
    read in the flux commands data.
    """
    with open(filepath, "r") as fd:
        data = yaml.load(fd.read(), Loader=yaml.SafeLoader)
    return data


def validate(filename):
    """
    clean out expired job postings from a file
    """
    filepath = get_filepath(filename)
    print("filepath is: %s" % filepath)

    # Read in the jobs
    commands = read_commands(filepath)

    # Validate structure (raises an error if not OK)
    jsonschema.validate(commands, schema=schema)

    # Ensure the last item is labeled as such
    last = commands["commands"][-1]["groups"][-1]["items"][-1]
    assert "last" in last
    assert last["last"] is True

    # Ensure last isn't anywhere else!
    for group in commands["commands"]:
        for subgroup in group["groups"]:
            for item in subgroup["items"]:

                # Only allowed for the last item!
                if (
                    item["title"] == last["title"]
                    and item["command"] == last["command"]
                ):
                    continue
                if "last" in item:
                    sys.exit("Item {last['title']} has the last key, and should not.")


def main():
    validate("flux-commands.yaml")


if __name__ == "__main__":
    main()
