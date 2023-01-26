
with open("laba3.txt", "r") as input_file:
    size = int(input_file.readline())
    if size <= 0:
        raise ValueError
    count = 0
    result = 0
    for row in range(size):
        array = [int(x) for x in input_file.readline().split()]
        for col in range(size):
            if col <= row:
                continue
            if array[col] < 0:
                continue
            result += array[col]
            count += 1
with open("laba3.txt", "w") as output_file:
    output_file.write(f"Found {count} positive items above main diagonal;\n")
    output_file.write(f"Sum of all positive items: {result}.")
