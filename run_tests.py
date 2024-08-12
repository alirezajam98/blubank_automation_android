import subprocess
import json


def run_tests(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)

    devices = config['devices']
    test_groups = config['testGroups']

    for device_name, device_info in devices.items():
        groups = device_info['testGroups']

        for group in groups:
            test_files = test_groups[group]

            for test_file in test_files:
                command = [
                    "pytest",
                    test_file,
                    f"--device={device_name}"
                ]
                print(f"Running {test_file} on {device_name}...")
                subprocess.run(command)


if __name__ == "__main__":
    run_tests('test_config.json')
