#file = open("Test1.txt")
file = open("Test2.txt")

limit, signal_fine, slow_fine, fast_fine = map(int, file.readline().strip().split())          # skip first line of input file

for line in file:
    plate, speed, signal = line.strip().split()
    speed = int(speed)
    fine = 0
    if signal == "red":
        fine = fine + signal_fine
    if speed - limit > 15:
        fine = fine + fast_fine
    elif speed - limit >= 5:
        fine = fine + slow_fine

    if fine > 0:
        print('{:6} ${}'.format(plate, fine))
    