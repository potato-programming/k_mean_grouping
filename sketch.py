from p5 import *
import random
from time import sleep

from grouper_algorithm import Grouper


focus_num = 5
centroid_num = 4
set_size = 100


def setup():
	size(600, 600)
	title("k mean grouping")

	# create our focus points
	global focus_points
	focus_points = []
	for i in range(focus_num):
		focus_points.append( Vector(random_uniform(width), random_uniform(height)) )

	# We make a dataset to use for the algorithm
	global dataset
	dataset = []

	for i in range(set_size):
		
		# dist_from is a fraciton of the average size of the window
		dist_from = random_uniform( (width+height / 2) / 10 )

		# define a focus point, choose how far away it is, and flip the relation vector if it is off of the screen
		center = random.choice(focus_points)
		in_relation_to_center = Vector.random_2D() * dist_from
		loc = in_relation_to_center + center
		if (loc.x < 0 or loc.x > width
			or loc.y < 0 or loc.y > height):
			loc *= -1

		dataset.append(center + in_relation_to_center)


	global grouper
	grouper = Grouper(dataset, centroid_num)


def draw():
	background(25)

	for i in range(len(grouper.centroids)):

		for j in range(len(grouper.centroid_sets[i])):

			loc = grouper.centroid_sets[i][j]
			color = grouper.label_colors[i]
			fill(color[0], color[1], color[2])
			no_stroke()
			circle(loc, 4)

	for i in range(len(grouper.centroids)):
		loc = grouper.centroids[i]
		color = grouper.label_colors[i]
		no_stroke()
		fill(color[0], color[1], color[2])
		rect_mode(CENTER)
		square(loc, 10)

	sleep(0.5)
	grouper.execute_algorithm()



run()