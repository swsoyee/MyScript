"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    index = 0
    compare = 0
    if len(line1) < len(line2):
        line1 = line1 + " " * (len(line2) - len(line1))
    else:
        line2 = line2 + " " * (len(line1) - len(line2))
    try:
        while line1[index] == line2[index]:
            compare += 1
            if compare == len(line1):
                break
            index += 1
        if compare == 0:
            return 0
        elif compare == len(line1):
            return IDENTICAL
        else:
            return index
    except IndexError:
        return -1

def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index of first difference between the lines
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    result = ""
    if not (line1.find("\n") > -1 or \
            line2.find("\n") > -1 or \
            line1.find("\r") > -1 or \
            line2.find("\r") > -1):
        length =  len(line1) if len(line1) < len(line2) else len(line2)
        if idx > -1 and (idx <= length):
            result = line1 + "\n" + "=" * idx + "^\n" + line2 + "\n"
    return result


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    line_index = 0
    append_lines1 = list(lines1)
    append_lines2 = list(lines2)
    if(len(append_lines1) == 0 and len(append_lines2) == 0):
        return (-1, -1)
    if len(lines1) < len(lines2):
        append_lines1.append([""] * (len(append_lines2) - len(append_lines1)))
    else:
        append_lines2.append([""] * (len(append_lines1) - len(append_lines2)))
        
    # shorter_lines_length = len(lines1) if len(lines1) < len(lines2) else len(lines2)
    identical = -1
    while(identical == -1):
        identical = singleline_diff(str(append_lines1[line_index]), str(append_lines2[line_index]))
        # if line_index + 1 == shorter_lines_length:
        if identical != -1:
            return(line_index, identical)
        if line_index + 1 == len(append_lines1):
            return(-1, -1)
        line_index += 1
    return (line_index, identical)

def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    input_file = open(filename, 'rt')
    text = []
    for line in input_file:
        line = line.strip('\n\r')
        text.append(line)
    return text

def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)
    line_number, idx = multiline_diff(lines1, lines2)
    if line_number == -1 :
        output = "No differences\n"
    else:
        new_line1 = "" if len(lines1) == 0 else lines1[line_number]
        new_line2 = "" if len(lines2) == 0 else lines2[line_number]
        output = "Line " + str(line_number) + ":\n" + \
                 singleline_diff_format(new_line1, new_line2, idx)
    return output
