import subprocess
import json
import multiprocessing


def run_test_on_device(device_name, test_files):
    for test_file in test_files:
        command = [
            "pytest",
            test_file,
            f"--device={device_name}"
        ]
        print(f"Running {test_file} on {device_name}...")
        subprocess.run(command)


def run_tests(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)

    devices = config['devices']
    test_groups = config['testGroups']

    processes = []

    for device_name, device_info in devices.items():
        groups = device_info['testGroups']
        test_files = []

        for group in groups:
            test_files.extend(test_groups[group])

        p = multiprocessing.Process(target=run_test_on_device, args=(device_name, test_files))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


if __name__ == "__main__":
    run_tests('test_config.json')
