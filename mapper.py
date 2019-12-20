#!/usr/bin/python
import sys
import random
from math import sqrt


def get_input(fp):
    if not fp:
        input = sys.stdin
    else:
        input = open(fp, "r")
    k = 0
    clusters = []
    points = []
    for line in input:
        lineArr = line.split(",");
        if lineArr[0] == "c":
            clusters.append(   (list(map(float,lineArr[2:5])), [])   )
            # k will be updated to the number of clusters
            if k < int(lineArr[1])+1:
                k = int(lineArr[1])+1
        elif lineArr[0] == "p":
            points.append(list(map(float,lineArr[1:4])))
    return k, points, clusters


def to_output(clusters):
    i = 0
    for cluster in clusters:
        print("c,{},{}".format(i, ",".join(map(str, cluster[0]))))
        i+=1
    i = 0
    for cluster in clusters:
        for point in cluster[1]:
            print("p,{},{}".format(i, ",".join(map(str, point))))
        i+=1

def cluster(k, points, clusters):
    # for every point, find closest centroid
    for p in points:
        if not in_clusters(p, clusters):
            min_cluster = 0
            min_distance = distance(p, clusters[0])
            # find closest centroid
            for i in range(len(clusters)):
                if distance(p, clusters[i]) < min_distance:
                    min_cluster = i
            # add point to cluster of that centroid
            clusters[min_cluster][1].append(p)
    return clusters;

# if point is in the clusters
def in_clusters(point, clusters):
    for cluster in clusters:
        if point in cluster[1]:
            return True
    return False

# finds the distance from the point to the centroid of the cluster
def distance(point, cluster):
    arr = []
    for i in range(len(point)):
        arr.append(point[i] - cluster[0][i])
    return sqrt(sum(map(lambda x:x*x, arr))) # square root of the sum of the squares in the array
#

# cluster is in the form ([coordinates of centroid], [points assigned to this cluster])

if len(sys.argv) > 1:
    fp = sys.argv[1]
else:
    fp = ""

k, points, clusters = get_input(fp)
to_output(cluster(k, points, clusters))



#
