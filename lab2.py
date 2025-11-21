"""
Please open the file "lab2_file.txt" to see its structure.
It has the following structure:
    Pink,85
    Red,44
    Maroon,80

File "lab2_file.txt" records the number of paint bottles bought within a year,
every line has two fields: the color of the paint, and the number of bottles,
and they are separated by a comma (,)

This program is used to count the number of bottles for each color,
and write the final result into a new file.
"""


def count_paint_bottles(input_file, output_file):
    # create an empty dictionary called `totals` to count all bottles
    totals = {}

    # open the file (argument `input_file`) with mode "r"
    file_obj = open(input_file, "r")

    # use for loop to iterate the file object and get every line
    for line in file_obj:
        # use split() function to separate each line into a list
        fields = line.strip().split(",")
        color = fields[0]
        num = int(fields[1])  # second item converted to integer

        if color not in totals:
            # add a new entry if color not recorded yet
            totals[color] = num
        else:
            # add num to existing total
            totals[color] += num

    # close the file object
    file_obj.close()

    # open the output file with mode "w"
    file_obj2 = open(output_file, "w")

    for color in totals.keys():
        # get the num of each color, convert it to a string `num_str`
        num_str = str(totals[color])
        string_to_write = color + ":" + num_str  # combine the string

        # write the string and a new line
        file_obj2.write(string_to_write)
        file_obj2.write("\n")

    file_obj2.close()


if __name__ == "__main__":
    count_paint_bottles("lab2_file.txt", "lab2_result.txt")
