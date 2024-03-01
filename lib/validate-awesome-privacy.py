import json
import os
import sys
import logging
import yaml
from termcolor import colored
from jsonschema import Draft7Validator

# Configure Logging
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()
logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(__name__)


# Determine the project root based on the script's location
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
awesome_privacy_path = os.path.join(project_root, 'awesome-privacy.yml')
schema_path = os.path.join(project_root, 'lib/schema.json')


# Log method, accepts a message and optional log level
# and prints the output to the terminal in right color
def loggy(message: str, level: str = 'debug'):
    if level == "info":
        logger.info(colored(message, 'blue'))
    elif level == "warning":
        logger.warning(colored(message, 'yellow'))
    elif level == "error":
        logger.error(colored(message, 'red'))
    elif level == "success":
        logger.info(colored(message, 'green'))
    elif level == "debug":
        logger.debug(colored(message, 'grey'))


# Loads a given YAML file and returns the data
def load_yaml(yaml_path: str):
    loggy(f"Loading YAML from {yaml_path}", "info")
    try:
        with open(yaml_path, 'r') as file:
            return yaml.safe_load(file)
    except yaml.YAMLError as e:
        loggy(f"Failed to load YAML: {e}", "error")
        sys.exit(1)


# Loads a given JSON Schema file and returns the data
def load_schema(schema_path: str):
    loggy(f"Loading JSON Schema from {schema_path}", "info")
    try:
        with open(schema_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        loggy(f"Failed to load JSON Schema: {e}", "error")
        sys.exit(1)


# Validates the given YAML data against the given JSON Schema
def validate_yaml(data, schema):
    loggy("Beginning validation", "info")
    validator = Draft7Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
    if errors:
        for error in errors:
            error_location = "->".join(map(str, error.path))
            loggy(f"Validation error: {error.message} (at {error_location})", "warning")
        return False
    return True


# Main method
def main():
    loggy("Starting...", "info")
    yaml_data = load_yaml(awesome_privacy_path)
    schema = load_schema(schema_path)

    if validate_yaml(yaml_data, schema):
        loggy("Validation successful!", "success")
        sys.exit(0)
    else:
        loggy("Validation failed.", "error")
        sys.exit(1)


if __name__ == "__main__":
    main()
