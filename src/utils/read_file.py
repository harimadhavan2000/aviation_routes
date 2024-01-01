import csv


def read_file(path):
    """
    Read a file and return its contents as a list of strings.
    """
    with open(path, "r") as file:
        data = file.readlines()
    # this is a list of tsv strings with newlines handle this.
    data = [line.strip().split("\t") for line in data]
    return data[1:]
