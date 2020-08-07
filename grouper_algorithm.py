from p5 import *
import random


class Grouper:

	def __init__(self, dataset, centroid_num):

		# we put dataset first so that the centroids can be near random dataset values
		self.dataset = dataset

		# holds the centroid sets, which hold all of the data_points associated with a particular centroid
		self.centroid_sets = []
		average_set_len = int( len(self.dataset) / centroid_num )

		avaliable_data_points = self.dataset.copy()
		for i in range(centroid_num):
			centroid_set = []

			# make sure we use all data_points
			if (i == centroid_num - 1):
				set_len = len(avaliable_data_points)
			else:
				set_len = average_set_len

			# fill a centroid_set and make sure that there are no repeats.
			for j in range(set_len):
				data_point = random.choice(avaliable_data_points)

				avaliable_data_points.remove(data_point)
				centroid_set.append(data_point)

			self.centroid_sets.append(centroid_set)

		# centroids start as the geometrid mean of our centroid sets.
		self.centroids = []
		for i in range(len(self.centroid_sets)):
			self.centroids.append(self.find_set_mean(i))

		self.centroid_num = centroid_num
			

		# holds the label of each data_point in the dataset
		self.data_labels = []

		# here the centroid sets change, so we will need to recalcalculate the centroids.
		self.label_dataset()

		self.label_colors = []
		for i in range(len(self.centroids)):
			color = (random_uniform(255, 100), random_uniform(255, 100), random_uniform(255, 100))
			self.label_colors.append(color)



	def label_dataset(self):

		#clear centroid_sets
		for centroid_set in self.centroid_sets:
			centroid_set.clear()

		# find closest centroid for each datapoint
		for data_point in self.dataset:

			closest_centroid = self.centroids[0]
			closest_dist = distance(data_point, self.centroids[0])
			closest_centroid_index = 0

			for i in range(len(self.centroids)):

				dist_to_centroid = distance(data_point, self.centroids[i])

				if (dist_to_centroid < closest_dist):
					closest_centroid = self.centroids[i]
					closest_dist = dist_to_centroid
					closest_centroid_index = i

			# label the data_point and put it in the associated centroid set
			self.data_labels.append(closest_centroid_index)
			self.centroid_sets[closest_centroid_index].append(data_point)


	# finds the mean of a set of data_points
	# it doesn't find the mean of the whole dataset, only a labeled part of it.
	def find_set_mean(self, set_index):

		x_total = 0
		y_total = 0

		centroid_set = self.centroid_sets[set_index]

		if (len(centroid_set) == 0):
			return None

		else:

			for data_point in centroid_set:
				x_total += data_point.x
				y_total += data_point.y

			mean_x = x_total / len(centroid_set)
			mean_y = y_total / len(centroid_set)

			mean = Vector(mean_x, mean_y)

			return mean



	def execute_algorithm(self):

		for i in range(len(self.centroids)):
			set_mean = self.find_set_mean(i)

			if (set_mean == None):
				self.centroids[i] = random.choice(self.dataset)
			else:
				self.centroids[i] = self.find_set_mean(i)
		
		self.label_dataset()
