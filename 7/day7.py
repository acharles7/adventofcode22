from pathlib import Path
from pprint import pprint

DATA = Path(__file__).parent / "data.txt"


def recursive_get(obj: dict, key: str):
    if key in obj and isinstance(obj[key], dict):
        return obj[key]

    for k, v in obj.items():
        if isinstance(v, dict) and v:
            item = recursive_get(v, key)
            if item is not None:
                return recursive_get(v, key)


def find_total_sizes() -> int:
    outputs = DATA.read_text().splitlines()
    file_system: dict = {"/": {}}

    n: int = 0
    current_dir = None
    pwd: list[str] = []
    while n < len(outputs):
        output = outputs[n]

        if output.startswith("$"):
            command = output.split("$")[1].strip()

            if command.startswith("cd"):
                cmd, directory = command.split()
                if directory == "..":
                    pwd.pop()
                    current_dir = recursive_get(file_system, pwd[-1])
                    n += 1
                    continue
                if directory == "/":
                    current_dir = file_system[directory]
                    pwd.append(directory)
                    n += 1
                    continue

                current_dir = recursive_get(file_system, directory)
                pwd.append(directory)
                n += 1
            if command.startswith("ls"):
                n += 1
                while n < len(outputs):
                    output = outputs[n]
                    n += 1
                    if output.startswith("$"):
                        n -= 1
                        break
                    if output.startswith("dir"):
                        _, name = output.split()
                        current_dir[name.strip()] = {}
                    else:
                        size, filename = output.split()
                        if filename not in current_dir:
                            current_dir[filename] = int(size)

    directory_sizes = {}

    def dir_sizes(d: dict) -> int:
        sz = 0
        for _k, _v in d.items():
            type_ = "dir"
            if isinstance(_v, int):
                type_ = "file"
                sz += _v
            else:
                sz += dir_sizes(_v)
            directory_sizes[_k] = {"size": sz, "type": type_}
        return sz
    dir_sizes(file_system)

    total = 0
    for k, v in directory_sizes.items():
        if v.get("type") == "dir" and v["size"] <= 100000:
            total += v["size"]
    return total


if __name__ == '__main__':
    print(find_total_sizes())
