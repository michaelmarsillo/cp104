"""
-------------------------------------------------------
[Assignment 9]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-11-29"
-------------------------------------------------------
"""
# Imports


def file_top(file_handle, count):
    """
    -------------------------------------------------------
    Prints first count lines of file_handle. Line numbering starts at 0.
    If length of file is shorter than count, stops printing after
    last line of file.
    Use: file_top(file_handle, count)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
        count - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    lines = file_handle.readlines()
    print(''.join(lines[:count]), end='')
    return


def read_integers(file_handle):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: number_list = read_integers(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        number_list - a list of integers from file_handle (list of int)
    -------------------------------------------------------
    """
    numbers = []

    for line in file_handle:
        values = line.strip().split(',')

        for value in values[1:]:
            try:
                number = int(value)
                if number > 0:
                    numbers.append(number)
            except ValueError:
                continue

    return numbers


def file_statistics(file_handle):
    """
    -------------------------------------------------------
    Evaluates the contents of a file by counting upper-case letters,
    lower-case letters, digits, white-spaces (including end-of-line
    characters), and remaining characters.
    Use: ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        ucount - The number of upper-case letters in the file (int)
        lcount - The number of lower-case letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of white-space characters in the file (int)
        rcount - The number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    ucount = lcount = dcount = wcount = rcount = 0

    for line in file_handle:
        for char in line:
            if char.isupper():
                ucount += 1
            elif char.islower():
                lcount += 1
            elif char.isdigit():
                dcount += 1
            elif char.isspace():
                wcount += 1
            else:
                rcount += 1

    return ucount, lcount, dcount, wcount, rcount


def line_numbering(fh_read, fh_write):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_write contain contents
    of fh_read where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: line_numbering(fh_read, fh_write)
    -------------------------------------------------------
    Parameters:
        fh_read - file to read (file - open for reading)
        fh_write - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    # read lines from the input file
    lines = fh_read.readlines()

    # write numbered lines to the output file
    for i, line in enumerate(lines):
        fh_write.write(f"[{i}] {line}")
    return


def student_stats(file_handle):
    """
    -------------------------------------------------------
    Get information from a file of file_handle and grades.
    Use: l_id, h_id, avg = student_stats(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    # read lines from the file
    lines = file_handle.readlines()
    total_marks = 0
    num_students = 0
    min_mark = float('inf')
    max_mark = float('-inf')
    l_id = ''
    h_id = ''

    # process each line to find the lowest, highest marks, and calculate the total marks
    for line in lines:
        parts = line.strip().split(',')
        mark = int(parts[-1])
        total_marks += mark
        num_students += 1

        if mark < min_mark:
            min_mark = mark
            l_id = parts[2]

        if mark > max_mark:
            max_mark = mark
            h_id = parts[2]

    # calculate the average mark
    avg = total_marks / num_students if num_students > 0 else 0

    return l_id, h_id, avg
