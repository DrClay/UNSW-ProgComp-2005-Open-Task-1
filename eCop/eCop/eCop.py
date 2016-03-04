#file = open("Test1.txt")
file = open("Test2.txt")                                                                    # open input file

limit, signal_fine, slow_fine, fast_fine = map(int, file.readline().strip().split())        # read first line as integers

for line in file:                                                                           # for each remaing line in the file
    plate, speed, signal = line.strip().split()                                             # read data into variables
    speed = int(speed)                                                                      # convert speed to integer
    fine = 0                                                                                # initialise fine
    if signal == "red":                                                                     # add fine for red signal
        fine = fine + signal_fine
    if speed - limit > 15:                                                                  # add fine for exceeding speed limit by more than 15 km/h
        fine = fine + fast_fine
    elif speed - limit >= 5:                                                                # add fine for exceeding speed limit by at least 5 km/h
        fine = fine + slow_fine

    if fine > 0:                                                                            # print plate and fine if there is a fine
        print('{:6} ${}'.format(plate, fine))
    