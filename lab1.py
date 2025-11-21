"""
Please open file "lab1_file.txt" to see the file structure.
The first line of the file indicates how many data lines in the file, say n.
The following n lines are the data lines, each line has a number.

The program reads the file "lab1_file.txt", and calculate average number of all those data line.
"""

def computer_average(filename):
    # create a file object called "file_obj" in read mode
    file_obj = open(filename, "r")

    # read first line, which is number of data lines
    first_line = file_obj.readline()
    nums_line = int(first_line.strip())

    # create a list to wrap all following numbers
    numbers = []

    for i in range(nums_line):
        # read one line in each iteration, convert to float
        line = file_obj.readline()
        number = float(line.strip())
        numbers.append(number)

    # close the file object
    file_obj.close()

    # calculate the average
    avg = sum(numbers) / len(numbers) if numbers else 0.0
    return avg


if __name__ == "__main__":
    average = computer_average("lab1_file.txt")
    print(average)
