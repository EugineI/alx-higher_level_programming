import importlib.util
import sys

def print_names():
    spec = importlib.util.spec_from_file_location("hidden_4", "hidden_4.pyc")
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)
    name = dir(hidden_4)
    filtered_names = [name for name in names if not name.startswith('__')]
    filtered_names.sort()
    for name in filtered_names:
        print(name)


if __name__ == "__main__":
    print_names()
