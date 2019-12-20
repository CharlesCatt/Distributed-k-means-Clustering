#!/usr/bin/python
import sys
import random
from math import sqrt


def get_input(fp):
    if not fp:
        input = sys.stdin
    else:
        input = open(fp, "r")
    clusters = []
    points = []
    for line in input:
        lineArr = line.split(",");
        if lineArr[0] == "c":
            clusters.append(   (list(map(float,lineArr[2:5])), [])   )
        elif lineArr[0] == "p":
            points.append(   (int(lineArr[1]), list(map(float,lineArr[2:5])))   )
    for point in points:
        clusters[point[0]][1].append(point[1])
    return clusters


def to_output(clusters):
    i = 0
    for cluster in clusters:
        print("c,{},{}".format(i, ",".join(map(str, cluster[0]))))
        i+=1
    i = 0
    for cluster in clusters:
        for point in cluster[1]:
            print("p,{}".format(",".join(map(str, point))))
        i+=1


# finds new centroid as the mean of all points in cluster
def new_centroid(cluster):
    centroid = cluster[1][0][:]
    for point in cluster[1][1:]:
        for i in range(len(centroid)):
            centroid[i] += point[i]
    return list(map(lambda x:x/len(cluster[1]), centroid)) # a list of the mean of every dimension


if len(sys.argv) > 1:
    fp = sys.argv[1]
else:
    fp = ""

clusters = get_input(fp)
for cluster in clusters:
    cluster = (new_centroid(cluster), cluster[1])

to_output(clusters)
