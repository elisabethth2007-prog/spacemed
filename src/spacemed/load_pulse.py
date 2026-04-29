def read_pulse(fname):
    dataFile = open(fname)
    time = []
    absorption = []

    dataFile.readline()  # discarding first line (header)
    for line in dataFile.readlines():
        line = line.split(",")
        time.append(float(line[0]))
        absorption.append(float(line[1]))
    return time, absorption
