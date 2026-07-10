import subprocess

# Path to ControlMyMonitor.exe
CMM_PATH = r"\PATH\TO\ControlMyMonitor.exe"

def set_monitor_input(monitor_identifier, input_value):
    """Set a monitor's input using ControlMyMonitor CLI (VCP code 60)."""
    cmd = [
        CMM_PATH,
        "/SetValue",
        monitor_identifier,
        "60",
        str(input_value)
    ]

    subprocess.run(cmd, check=True)
    print(f"Monitor {monitor_identifier} set to input {input_value}")


if __name__ == "__main__":
    # Example usage
    set_monitor_input(
        monitor_identifier="Primary",  # or "\\.\DISPLAY1\Monitor0"
        input_value=17                 # DisplayPort or HDMI Input (Check the values for your monitor in the ControlMyMonitor GUI.
    )
