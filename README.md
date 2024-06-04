# fprintclear

This script interacts with fingerprint readers to list or delete enrolled fingerprints. It leverages the FPrint library and requires root privileges to access the devices.

## Installation

First, install the necessary system-level dependencies.

### Fedora

```sh
sudo dnf install gobject-introspection-devel cairo-gobject-devel
```

### Python dependencies

After installing the system-level dependencies, use Poetry to install the Python dependencies.

```sh
poetry install
```

## Usage

To use the script, activate the Poetry shell and run the script with root privileges.

```sh
poetry shell
sudo python fprintclear.py
```

### Options

- `-d` or `--delete`: Deletes enrolled fingerprints.

Example:

```sh
sudo python fprintclear.py -d
```

## Script Explanation

This script is designed to interact with fingerprint readers using the FPrint library. Fingerprint readers store images of your fingerprints, usually at a resolution of 256x288 pixels. These images are taken from various angles to ensure reliable matching. Each enrolled fingerprint takes up around 750kB of storage, with the device typically having around 11MB of total storage capacity.

The script performs the following tasks:
1. **Check for Root Privileges:** Ensures the script is run with root privileges.
2. **Initialize FPrint Context:** Sets up the context for interacting with fingerprint devices.
3. **List Fingerprint Devices:** Enumerates connected fingerprint devices.
4. **List Enrolled Fingerprints:** For each device, lists the fingerprints currently enrolled.
5. **Delete Fingerprints (optional):** If the `-d` flag is set, deletes the enrolled fingerprints.

### Detailed Workflow

1. **Root Privilege Check:**
   - The script checks if it's run with root privileges using `geteuid()`.
   - If not, it prompts the user to rerun the script with `sudo`.

2. **Context Initialization:**
   - The FPrint context is initialized to interact with the fingerprint devices.

3. **Device Enumeration:**
   - The script loops through each connected fingerprint device and prints device information such as the driver and device ID.

4. **Enrolled Fingerprints:**
   - For each device, the script lists the enrolled fingerprints, printing information such as the enrollment date, finger, username, and description.

5. **Fingerprint Deletion:**
   - If the `-d` flag is specified, the script deletes the enrolled fingerprints from the device.
