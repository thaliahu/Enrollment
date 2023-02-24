"""Enrollment analysis:  Summary report of majors enrolled in a class.
CS 210 project, Fall 2022.
Author: Thalia Hundt
Credits: TBD
"""
import doctest
import csv

def read_csv_column(path: str, field: str) -> list[str]:
    """Read one column from a CSV file with headers into a list of strings.

    >>> read_csv_column("data/test_roster.csv", "Major")
    ['DSCI', 'CIS', 'BADM', 'BIC', 'CIS', 'GSS']
    """
    column = []
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for x in reader:
            column.append(x[field])
    return column


def counts(column: list[str]) -> dict[str, int]:
    """Returns a dict with counts of elements in column.

    >>> counts(["dog", "cat", "cat", "rabbit", "dog"])
    {'dog': 2, 'cat': 2, 'rabbit': 1}
    """
    count_list = column
    dictionary = {}
    for y in count_list:
        if y in dictionary:
            dictionary[y] += 1
        else:
            dictionary[y] = 1
    return dictionary

def read_csv_dict(path: str, key_field: str, value_field: str) -> dict[str, dict]:
    """Read a CSV with column headers into a dict with selected
    key and value fields.

    >>> read_csv_dict("data/test_programs.csv", key_field="Code", value_field="Program Name")
    {'ABAO': 'Applied Behavior Analysis', 'ACTG': 'Accounting', 'ADBR': 'Advertising and Brand Responsibility'}
    """
    k_v = {}
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            key = row[key_field]
            value = row[value_field]
            k_v[key] = value
    return k_v

def items_v_k (d:dict) -> list[tuple]:
    '''
    Like d.items() but (value, key) pairs instead of (key, value)
​
    >>> items_v_k({'z': 2, 'a': 3, 'm': 4, 'q': 5})
    [(2, 'z'), (3, 'a'), (4, 'm'), (5, 'q')]
    
    '''
    empty_list = []
    for code, count in d.items():
        pair = (count, code)
        empty_list.append(pair)
    return empty_list

def main():
    doctest.testmod()
    majors = read_csv_column("data/roster_selected.csv", "Major")
    counts_by_major = counts(majors)
    program_names = read_csv_dict("data/programs.csv", "Code", "Program Name")
    by_count = items_v_k(counts_by_major)
    by_count.sort(reverse=True)  # From largest to smallest
    for count, code in by_count:
        program = program_names[code]
        print(count, program)

main()



#if __name__ == "__main__":
   # main()
