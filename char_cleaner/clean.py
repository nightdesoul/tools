import sys
import os


def clean_file(folder, name):
    with open(f'{folder}{name}', mode='rb') as f:
        data = f.read()

    result = bytearray()
    for i in range(len(data)):
        if data[i] < 32:
            result.append(32)
            continue
        result.append(data[i])
    try:
        s = bytes(result).decode()
    except UnicodeDecodeError:
        print(f'File {name} - can\'t decode.')
        return

    with open(f'{folder}cleaned-{name}', mode='w') as f:
        f.write(s)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python clean.py folder")
        exit(1)
    folder = sys.argv[1]
    if folder[-1] != '/':
        folder += '/'

    try:
        files = os.scandir(folder)
    except FileNotFoundError:
        print("No such directory")
        exit(1)

    for f in files:
        if f.name[:8] == 'cleaned-':
            continue
        clean_file(folder, f.name)
