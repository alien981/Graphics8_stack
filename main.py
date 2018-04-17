from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
polygons = []
transform = [
	[[1, 0, 0, 0], 
	[0, 1, 0, 0],
	[0, 0, 1, 0],
	[0, 0, 0, 1]]
	]



parse_file( 'script', edges, polygons, transform, screen, color)

