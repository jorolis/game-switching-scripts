import socket

TESMART_IP = "192.168.1.10"
TESMART_PORT = 5000

def switch_tesmart_input(input_num):
    """Switch TESmart HDMI input."""
    if not (1 <= input_num <= 8):
        raise ValueError("TESmart input must be between 1 and 8")

    cmd = bytes([
        0xAA, 0xBB,
        0x03, 0x01,
        input_num,
        0xEE
    ])

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((TESMART_IP, TESMART_PORT))
        s.sendall(cmd)

    print(f"TESmart switched to input {input_num}")


if __name__ == "__main__":
    switch_tesmart_input(1)  # Change input number as needed
