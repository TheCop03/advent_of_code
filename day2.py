# Constants
add_opcode = 1;
mult_opcode = 2;
stop_opcode = 99;
required_out = 19690720;

# Read data from text file
with open('day2_data.txt') as file:
    memory = file.read().split(',')

data = [int(x) for x in memory]

# Starting instruction_ptr
instruction_ptr = 0;

# Two for loops to go through the input values
for noun in range(0, 100):
    for verb in range(0, 100):
        # Change the data values at address 1 and 2 with noun and verb respectively
        data[1] = noun
        data[2] = verb;

        # do the Intcode program
        while (data[instruction_ptr] != stop_opcode):
            # Add the two if 1
            if (data[instruction_ptr] == add_opcode):
                data[data[instruction_ptr + 3]] = data[data[instruction_ptr + 1]] + data[data[instruction_ptr + 2]];
            # Multiply the two if 2
            elif (data[instruction_ptr] == mult_opcode):
                data[data[instruction_ptr + 3]] = data[data[instruction_ptr + 1]] * data[data[instruction_ptr + 2]];

            # Move forward
            instruction_ptr += 4;

        # Check if we got the required output
        if (data[0] == required_out):
            break
        else:
            data = [int(x) for x in memory]
            instruction_ptr = 0;

    # Result is found. Just print
    if (data[0] == required_out):
        print('Result: ' + str(100 * noun + verb))
        break


print(data)
