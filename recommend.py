'''
Movie Recommender System

A user can rate the movie from 1 to 5 stars, to get their
customized recommendations.
users = number of users
movies = number of movies
r(i, j) = 1 if user j has rated movie i
y(i, j) = rating given by user j to movie i 
(defined only if r(i, j) = 1)
'''

# import numpy as np
import csv
import customer_types

# users = np.loadtxt("data/BX-Users.csv", delimiter=';', skiprows=1)
users = []
with open('data/BX-Users.csv', 'rb') as user_file:
	reader = csv.reader(user_file, delimiter=';')
	reader.next()
	for row in reader:
		users.append(user.User(int(row[0]), str(row[1]), str(row[2])))
# books = np.loadtxt("data/BX-Books.csv")
# book-ratings = np.loadtxt("data/BX-Book-Ratings.csv")

