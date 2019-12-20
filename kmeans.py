#!/usr/bin/python
import sys
import random
from math import sqrt
# def find_k(points):

def initial_clusters(points, k):
    # pick a random point
    rand = random.randint(0,len(points)-1)
    clusters = [(points[rand], [points[rand]])]
    clusters_indexes = [rand]
    # loop, adding the furthest point until number of initial clusters is k
    while len(clusters) < k:
        max_dist = 0
        max_index = 0
        # for point in points, not including those that are clusters already
        for i in range(0,len(points)):
            if i not in clusters_indexes:
                # find the minimum distance from the point to one of the clusters
                min_dist = distance(points[i], clusters[0])
                for j in range(1,len(clusters)):
                    if distance(points[i], clusters[j]) < min_dist:
                        min_dist = distance(points[i], clusters[j])
                if min_dist > max_dist:
                    max_dist = min_dist
                    max_index = i
        clusters.append((points[max_index], [points[max_index]]))
        clusters_indexes.append(max_index)
    return clusters

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
# finds new centroid as the mean of all points in cluster
def new_centroid(cluster):
    centroid = cluster[1][0][:]
    for point in cluster[1][1:]:
        for i in range(len(centroid)):
            centroid[i] += point[i]
    return list(map(lambda x:x/len(cluster[1]), centroid)) # a list of the mean of every dimension

#
# performs clustering operation, from psuedocode given in part 7.3.1 of the text-book
def cluster(k, points, clusters):
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
            # calculate new centroid for that cluster
            clusters[min_cluster] = (new_centroid(clusters[min_cluster]), clusters[min_cluster][1])
    return clusters;

def get_input(fp):
    if not fp:
        input = sys.stdin
    else:
        input = open(fp, "r")
    points = []
    for line in input:
        try:
            points.append(list(map(float,line.split(",")[0:4])))
        except:
            # print("error when reading input, line:\n{}".format(line))
            # print("")
            a = 1
    return points

def to_output(clusters):
    i = 0
    for cluster in clusters:
        print("c,{},{}".format(i, ",".join(map(str, cluster[0]))))
        i+=1
    # i = 0
    # for cluster in clusters:
    #     for point in cluster[1]:
    #         print("p,{},{}".format(i, ",".join(map(str, point))))
    #     i+=1

# generates a new k, equal to the number of sets that contain more than one point
# assuming that if there is more than one point in a cluster, the cluster is viable
# gives the new list of clusters (with no items, only the new centroid)
def new_k(clusters):
    k = 1
    new_clusters = []
    for cluster in clusters:
        if len(cluster[1]) > 1:
            k+=1
            new_clusters.append((cluster[0], []))
    return (k, new_clusters)

def test_k(k, points):
    for i in range(10):
        viable_k = True
        clusters = cluster(k, points, initial_clusters(points, k))
        for c in clusters:
            if len(c[1]) < 2:
                viable_k = False
        if viable_k:
            return clusters
    return []

if len(sys.argv) > 1:
    k = int(sys.argv[1])
else:
    exit(-1)
if len(sys.argv) > 2:
    fp = sys.argv[2]
else:
    fp = ""

points = get_input(fp)
test_clusters = test_k(k, points)
while not test_clusters:
    k-=1
    test_clutsers = test_k(k, points)

k, c = new_k(cluster(k, points, test_clusters))
to_output(cluster(k, points, c))
