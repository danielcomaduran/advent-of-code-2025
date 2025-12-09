#%% Import file
with open("input.txt") as file:
    math_worksheet = file.read()
numbers = math_worksheet.split("\n")[0:-1]
operations = math_worksheet.split("\n")[-1].split()

#%% Part 1: Sum all the operations per column
n_operations = len(operations)

numbers_for_current_operation = []
final_sum = 0
for op, operation in enumerate(operations):
    # Extract the numbers of the current operation
    for line in numbers:
        line_numbers = line.split()
        numbers_for_current_operation.append(int(line_numbers[op]))

    # Perform the operation
    if operation == "+":
        result = sum(numbers_for_current_operation)
    elif operation == "*":
        result = 1
        for number in numbers_for_current_operation:
            result *= number

    final_sum += result
    numbers_for_current_operation = []

print(f"Part 1: Final sum of all operations: {final_sum}")
# %% Part 2: Read the numbers vertically as well
# Find column positions by looking at the operations line
# Each operation marks where a column of digits is
with open("input.txt") as file:
    math_lines = file.readlines()

operator_positions = []
numbers_lines = math_lines[:-1]
ops_line = math_lines[-1]
for i, char in enumerate(ops_line):
    if char in ['+', '*']:
        operator_positions.append(i)

# Store numbers read vertically
vertical_numbers = [[] for _ in range(len(operator_positions))]
for op_idx, op_pos in enumerate(operator_positions):
    # Determine end column for the current number
    if op_idx + 1 < len(operator_positions):
        end_col = operator_positions[op_idx + 1] - 1
    else:
        end_col = len(ops_line)

    for i in range(op_pos, end_col):
        digits = []
        
        for line in numbers_lines:
            if line[i].isdigit():
                digits.append(line[i])
        # Join digits to form the number (top to bottom)
        vertical_numbers[op_idx].append(int(''.join(digits)))

# Perform operations
final_sum = 0
for idx, operation in enumerate(operations):
    if operation == "+":
        columns_sum = sum(vertical_numbers[idx])
        final_sum += columns_sum
    elif operation == "*":
        product = 1
        for number in vertical_numbers[idx]:
            product *= number
        final_sum += product

print(f"Part 2: Final sum: {final_sum}")# %%