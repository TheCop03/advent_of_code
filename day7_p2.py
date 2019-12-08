from itertools import permutations

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
with open('day7_data.txt') as file:
    memory = file.read().split(',')

file_data = [int(x) for x in memory]
phaseSettings = list(permutations([5, 6, 7, 8, 9]))
# phaseSettings = [[9,8,7,6,5]]
maxThrust = 0

# do the Intcode program
for phase in phaseSettings:

    # Starting instruction_ptr[amplifierNum]
    instruction_ptr = [0, 0, 0, 0, 0]
    inputSignal = 0
    wantPhase = [True, True, True, True, True]
    amplifierNum = 0
    data = [file_data] * 5
    opcode = int(str(data[amplifierNum][instruction_ptr[amplifierNum]])[-2:])

    while (opcode != stop_opcode or amplifierNum != 4):
        opcode = int(str(data[amplifierNum][instruction_ptr[amplifierNum]])[-2:])
        print("AmpNum: " + str(amplifierNum) + " opcode: " + str(opcode) + " inst: " + str(instruction_ptr[amplifierNum]))

        try:
            first_param_mode = int(str(data[amplifierNum][instruction_ptr[amplifierNum]])[-3])
        except IndexError as e:
            first_param_mode = pos_mode
        try:
            second_param_mode = int(str(data[amplifierNum][instruction_ptr[amplifierNum]])[-4])
        except IndexError as e:
            second_param_mode = pos_mode
        try:
            third_param_mode = int(str(data[amplifierNum][instruction_ptr[amplifierNum]])[-5])
        except IndexError as e:
            third_param_mode = pos_mode

        # Add the two if 1
        if (opcode == add_opcode):
            if (first_param_mode == pos_mode and second_param_mode == pos_mode):
                data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 3]] = data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 1]] + data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 2]];
            elif (first_param_mode == pos_mode and second_param_mode == imm_mode):
                data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 3]] = data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 1]] + data[amplifierNum][instruction_ptr[amplifierNum] + 2];
            elif (first_param_mode == imm_mode and second_param_mode == pos_mode):
                data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 3]] = data[amplifierNum][instruction_ptr[amplifierNum] + 1] + data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 2]];
            elif (first_param_mode == imm_mode and second_param_mode == imm_mode):
                data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 3]] = data[amplifierNum][instruction_ptr[amplifierNum] + 1] + data[amplifierNum][instruction_ptr[amplifierNum] + 2];

            instruction_ptr[amplifierNum] += 4

        # Multiply the two if 2
        elif (opcode == mult_opcode):
            if (first_param_mode == pos_mode and second_param_mode == pos_mode):
                data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 3]] = data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 1]] * data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 2]];
            elif (first_param_mode == pos_mode and second_param_mode == imm_mode):
                data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 3]] = data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 1]] * data[amplifierNum][instruction_ptr[amplifierNum] + 2];
            elif (first_param_mode == imm_mode and second_param_mode == pos_mode):
                data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 3]] = data[amplifierNum][instruction_ptr[amplifierNum] + 1] * data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 2]];
            elif (first_param_mode == imm_mode and second_param_mode == imm_mode):
                data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 3]] = data[amplifierNum][instruction_ptr[amplifierNum] + 1] * data[amplifierNum][instruction_ptr[amplifierNum] + 2];

            instruction_ptr[amplifierNum] += 4

        elif (opcode == in_opcode):

            if (wantPhase[amplifierNum]):
                print("amplifierNum: " + str(amplifierNum) + " phase: " + str(phase[amplifierNum]))
                data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 1]] = phase[amplifierNum]
                wantPhase[amplifierNum] = False
            else:
                print("amplifierNum: " + str(amplifierNum) + " input: " + str(inputSignal))
                data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 1]] = inputSignal

            instruction_ptr[amplifierNum] += 2

        elif (opcode == out_opcode):
            if first_param_mode == pos_mode:
                inputSignal = data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 1]]
            elif first_param_mode == imm_mode:
                inputSignal = data[amplifierNum][instruction_ptr[amplifierNum] + 1]

            if (amplifierNum == 4):
                # print("Phase: " + str(phase) + " thrust: " + str(thrust) + " MaxThrust: " + str(maxThrust))
                instruction_ptr[amplifierNum] += 2
                amplifierNum = 0
            else:
                instruction_ptr[amplifierNum] += 2
                amplifierNum += 1

        elif (opcode == true_jump_opcode):
            if (first_param_mode == pos_mode):
                # Set the instruction_ptr[amplifierNum] to the value of second parameter
                if (data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 1]] != 0):
                    if (second_param_mode == pos_mode):
                        instruction_ptr[amplifierNum] = data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 2]]
                    elif (second_param_mode == imm_mode):
                        instruction_ptr[amplifierNum] = data[amplifierNum][instruction_ptr[amplifierNum] + 2]
                # Move the instruction_ptr[amplifierNum] to the next instruction
                else:
                    instruction_ptr[amplifierNum] += 3
            elif (first_param_mode == imm_mode):
                # Set the instruction_ptr[amplifierNum] to the value of second parameter
                if (data[amplifierNum][instruction_ptr[amplifierNum] + 1] != 0):
                    if (second_param_mode == pos_mode):
                        instruction_ptr[amplifierNum] = data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 2]]
                    elif (second_param_mode == imm_mode):
                        instruction_ptr[amplifierNum] = data[amplifierNum][instruction_ptr[amplifierNum] + 2]
                # Move the instruction_ptr[amplifierNum] to the next instruction
                else:
                    instruction_ptr[amplifierNum] += 3

        elif (opcode == false_jump_upcode):
            if (first_param_mode == pos_mode):
                # Set the instruction_ptr[amplifierNum] to the value of second parameter
                if (data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 1]] == 0):
                    if (second_param_mode == pos_mode):
                        instruction_ptr[amplifierNum] = data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 2]]
                    elif (second_param_mode == imm_mode):
                        instruction_ptr[amplifierNum] = data[amplifierNum][instruction_ptr[amplifierNum] + 2]
                # Move the instruction_ptr[amplifierNum] to the next instruction
                else:
                    instruction_ptr[amplifierNum] += 3
            elif (first_param_mode == imm_mode):
                # Set the instruction_ptr[amplifierNum] to the value of second parameter
                if (data[amplifierNum][instruction_ptr[amplifierNum] + 1] == 0):
                    if (second_param_mode == pos_mode):
                        instruction_ptr[amplifierNum] = data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 2]]
                    elif (second_param_mode == imm_mode):
                        instruction_ptr[amplifierNum] = data[amplifierNum][instruction_ptr[amplifierNum] + 2]
                # Move the instruction_ptr[amplifierNum] to the next instruction
                else:
                    instruction_ptr[amplifierNum] += 3

        elif (opcode == less_than_opcode):
            if (first_param_mode == pos_mode and second_param_mode == pos_mode):
                if (data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 1]] < data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 2]]):
                    data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 3]] = 1;
                else:
                    data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 3]] = 0;
            elif (first_param_mode == pos_mode and second_param_mode == imm_mode):
                if (data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 1]] < data[amplifierNum][instruction_ptr[amplifierNum] + 2]):
                    data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 3]] = 1;
                else:
                    data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 3]] = 0;
            elif (first_param_mode == imm_mode and second_param_mode == pos_mode):
                if (data[amplifierNum][instruction_ptr[amplifierNum] + 1] < data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 2]]):
                    data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 3]] = 1;
                else:
                    data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 3]] = 0;
            elif (first_param_mode == imm_mode and second_param_mode == imm_mode):
                if (data[amplifierNum][instruction_ptr[amplifierNum] + 1] < data[amplifierNum][instruction_ptr[amplifierNum] + 2]):
                    data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 3]] = 1;
                else:
                    data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 3]] = 0;

            instruction_ptr[amplifierNum] += 4

        elif (opcode == equals_opcode):
            if (first_param_mode == pos_mode and second_param_mode == pos_mode):
                if (data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 1]] == data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 2]]):
                    data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 3]] = 1;
                else:
                    data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 3]] = 0;
            elif (first_param_mode == pos_mode and second_param_mode == imm_mode):
                if (data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 1]] == data[amplifierNum][instruction_ptr[amplifierNum] + 2]):
                    data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 3]] = 1;
                else:
                    data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 3]] = 0;
            elif (first_param_mode == imm_mode and second_param_mode == pos_mode):
                if (data[amplifierNum][instruction_ptr[amplifierNum] + 1] == data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 2]]):
                    data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 3]] = 1;
                else:
                    data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 3]] = 0;
            elif (first_param_mode == imm_mode and second_param_mode == imm_mode):
                if (data[amplifierNum][instruction_ptr[amplifierNum] + 1] == data[amplifierNum][instruction_ptr[amplifierNum] + 2]):
                    data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 3]] = 1;
                else:
                    data[amplifierNum][data[amplifierNum][instruction_ptr[amplifierNum] + 3]] = 0;

            instruction_ptr[amplifierNum] += 4

        print(data[amplifierNum])

    if (inputSignal > maxThrust):
        maxThrust = inputSignal

print("Max Thrust: " + str(maxThrust))
print(instruction_ptr)
print(data)
