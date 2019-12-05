# Constants
add_opcode = 1;
mult_opcode = 2;
in_opcode = 3;
out_opcode = 4;
true_jump_opcode = 5;
false_jump_upcode = 6;
less_than_opcode = 7;
equals_opcode = 8;
stop_opcode = 99;

pos_mode = 0
imm_mode = 1

# Read data from text file
with open('day5_data.txt') as file:
    memory = file.read().split(',')

data = [int(x) for x in memory]

# Starting instruction_ptr
instruction_ptr = 0;
opcode = int(str(data[instruction_ptr])[-2:])

# do the Intcode program
while (opcode != stop_opcode):
    opcode = int(str(data[instruction_ptr])[-2:])

    try:
        first_param_mode = int(str(data[instruction_ptr])[-3])
    except IndexError as e:
        first_param_mode = pos_mode
    try:
        second_param_mode = int(str(data[instruction_ptr])[-4])
    except IndexError as e:
        second_param_mode = pos_mode
    try:
        third_param_mode = int(str(data[instruction_ptr])[-5])
    except IndexError as e:
        third_param_mode = pos_mode

    # Add the two if 1
    if (opcode == add_opcode):
        if (first_param_mode == pos_mode and second_param_mode == pos_mode):
            data[data[instruction_ptr + 3]] = data[data[instruction_ptr + 1]] + data[data[instruction_ptr + 2]];
        elif (first_param_mode == pos_mode and second_param_mode == imm_mode):
            data[data[instruction_ptr + 3]] = data[data[instruction_ptr + 1]] + data[instruction_ptr + 2];
        elif (first_param_mode == imm_mode and second_param_mode == pos_mode):
            data[data[instruction_ptr + 3]] = data[instruction_ptr + 1] + data[data[instruction_ptr + 2]];
        elif (first_param_mode == imm_mode and second_param_mode == imm_mode):
            data[data[instruction_ptr + 3]] = data[instruction_ptr + 1] + data[instruction_ptr + 2];

        instruction_ptr += 4

    # Multiply the two if 2
    elif (opcode == mult_opcode):
        if (first_param_mode == pos_mode and second_param_mode == pos_mode):
            data[data[instruction_ptr + 3]] = data[data[instruction_ptr + 1]] * data[data[instruction_ptr + 2]];
        elif (first_param_mode == pos_mode and second_param_mode == imm_mode):
            data[data[instruction_ptr + 3]] = data[data[instruction_ptr + 1]] * data[instruction_ptr + 2];
        elif (first_param_mode == imm_mode and second_param_mode == pos_mode):
            data[data[instruction_ptr + 3]] = data[instruction_ptr + 1] * data[data[instruction_ptr + 2]];
        elif (first_param_mode == imm_mode and second_param_mode == imm_mode):
            data[data[instruction_ptr + 3]] = data[instruction_ptr + 1] * data[instruction_ptr + 2];

        instruction_ptr += 4

    elif (opcode == in_opcode):
        # Set 1 for part 1 OR 5 for part 2 as the input value for the position given by the single parameter
        #data[data[instruction_ptr + 1]] = 1
        data[data[instruction_ptr + 1]] = 5
        instruction_ptr += 2

    elif (opcode == out_opcode):
        if (first_param_mode == pos_mode):
            # Output the value at the position given by the single parameter
            print(data[data[instruction_ptr + 1]])
        elif (first_param_mode == imm_mode):
            # Output the value given by the parameter itself
            print(data[instruction_ptr + 1])
        instruction_ptr += 2

    elif (opcode == true_jump_opcode):
        if (first_param_mode == pos_mode):
            # Set the instruction_ptr to the value of second parameter
            if (data[data[instruction_ptr + 1]] != 0):
                if (second_param_mode == pos_mode):
                    instruction_ptr = data[data[instruction_ptr + 2]]
                elif (second_param_mode == imm_mode):
                    instruction_ptr = data[instruction_ptr + 2]
            # Move the instruction_ptr to the next instruction
            else:
                instruction_ptr += 3
        elif (first_param_mode == imm_mode):
            # Set the instruction_ptr to the value of second parameter
            if (data[instruction_ptr + 1] != 0):
                if (second_param_mode == pos_mode):
                    instruction_ptr = data[data[instruction_ptr + 2]]
                elif (second_param_mode == imm_mode):
                    instruction_ptr = data[instruction_ptr + 2]
            # Move the instruction_ptr to the next instruction
            else:
                instruction_ptr += 3

    elif (opcode == false_jump_upcode):
        if (first_param_mode == pos_mode):
            # Set the instruction_ptr to the value of second parameter
            if (data[data[instruction_ptr + 1]] == 0):
                if (second_param_mode == pos_mode):
                    instruction_ptr = data[data[instruction_ptr + 2]]
                elif (second_param_mode == imm_mode):
                    instruction_ptr = data[instruction_ptr + 2]
            # Move the instruction_ptr to the next instruction
            else:
                instruction_ptr += 3
        elif (first_param_mode == imm_mode):
            # Set the instruction_ptr to the value of second parameter
            if (data[instruction_ptr + 1] == 0):
                if (second_param_mode == pos_mode):
                    instruction_ptr = data[data[instruction_ptr + 2]]
                elif (second_param_mode == imm_mode):
                    instruction_ptr = data[instruction_ptr + 2]
            # Move the instruction_ptr to the next instruction
            else:
                instruction_ptr += 3

    elif (opcode == less_than_opcode):
        if (first_param_mode == pos_mode and second_param_mode == pos_mode):
            if (data[data[instruction_ptr + 1]] < data[data[instruction_ptr + 2]]):
                data[data[instruction_ptr + 3]] = 1;
            else:
                data[data[instruction_ptr + 3]] = 0;
        elif (first_param_mode == pos_mode and second_param_mode == imm_mode):
            if (data[data[instruction_ptr + 1]] < data[instruction_ptr + 2]):
                data[data[instruction_ptr + 3]] = 1;
            else:
                data[data[instruction_ptr + 3]] = 0;
        elif (first_param_mode == imm_mode and second_param_mode == pos_mode):
            if (data[instruction_ptr + 1] < data[data[instruction_ptr + 2]]):
                data[data[instruction_ptr + 3]] = 1;
            else:
                data[data[instruction_ptr + 3]] = 0;
        elif (first_param_mode == imm_mode and second_param_mode == imm_mode):
            if (data[instruction_ptr + 1] < data[instruction_ptr + 2]):
                data[data[instruction_ptr + 3]] = 1;
            else:
                data[data[instruction_ptr + 3]] = 0;

        instruction_ptr += 4

    elif (opcode == equals_opcode):
        if (first_param_mode == pos_mode and second_param_mode == pos_mode):
            if (data[data[instruction_ptr + 1]] == data[data[instruction_ptr + 2]]):
                data[data[instruction_ptr + 3]] = 1;
            else:
                data[data[instruction_ptr + 3]] = 0;
        elif (first_param_mode == pos_mode and second_param_mode == imm_mode):
            if (data[data[instruction_ptr + 1]] == data[instruction_ptr + 2]):
                data[data[instruction_ptr + 3]] = 1;
            else:
                data[data[instruction_ptr + 3]] = 0;
        elif (first_param_mode == imm_mode and second_param_mode == pos_mode):
            if (data[instruction_ptr + 1] == data[data[instruction_ptr + 2]]):
                data[data[instruction_ptr + 3]] = 1;
            else:
                data[data[instruction_ptr + 3]] = 0;
        elif (first_param_mode == imm_mode and second_param_mode == imm_mode):
            if (data[instruction_ptr + 1] == data[instruction_ptr + 2]):
                data[data[instruction_ptr + 3]] = 1;
            else:
                data[data[instruction_ptr + 3]] = 0;

        instruction_ptr += 4
#print(data)
