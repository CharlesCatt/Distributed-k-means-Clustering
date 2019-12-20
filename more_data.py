import random

f = open("iris.data", "r")
output = open("big.data", "w")
if f.mode == "r":
    lines = f.readlines();
    for line in lines:
        lineArr = line.split(",")[:-2]
        if lineArr:
            line1 = []
            line2 = []
            line3 = []
            for element in lineArr:
                line1.append("{:.1f}".format(float(element) + random.random()/2 - 0.5));
                line2.append("{:.1f}".format(float(element) + random.random()/2 - 0.5));
                line3.append("{:.1f}".format(float(element) + random.random()/2 - 0.5));
            output.write("p," + ",".join(lineArr) + "\n")
            output.write("p," + ",".join(line1) + "\n")
            output.write("p," + ",".join(line2) + "\n")
            output.write("p," + ",".join(line3) + "\n")
f.close()
output.close();
