#!/usr/bin/env python3

import re
import itertools

ROLLNUM_REGEX = "201[0-9]{4}"

class Graph(object):
	name = "Aman Kumar Gupta"
	email = "aman18217@iiitd.ac.in"
	roll_num = "2018217"

	def __init__ (self, vertices, edges):
		"""
		Initializes object for the class Graph

		Args:
			vertices: List of integers specifying vertices in graph
			edges: List of 2-tuples specifying edges in graph
		"""

		self.vertices = vertices
		
		ordered_edges = list(map(lambda x: (min(x), max(x)), edges))
		
		self.edges    = ordered_edges
		
		self.validate()

	def validate(self):
		if (not isinstance(self.name, str)) or self.name == "":
			raise Exception("Name can't be empty")

		if (not isinstance(self.email, str)) or self.email == "":
			raise Exception("Email can't be empty")

		if (not isinstance(self.roll_num, str)) or (not re.match(ROLLNUM_REGEX, self.roll_num)):
			raise Exception("Invalid roll number, roll number must be a string of form 201XXXX. Provided roll number: {}".format(self.roll_num))

		if not all([isinstance(node, int) for node in self.vertices]):
			raise Exception("All vertices should be integers")

		elif len(self.vertices) != len(set(self.vertices)):
			duplicate_vertices = set([node for node in self.vertices if self.vertices.count(node) > 1])

			raise Exception("Vertices contain duplicates.\nVertices: {}\nDuplicate vertices: {}".format(vertices, duplicate_vertices))

		edge_vertices = list(set(itertools.chain(*self.edges)))

		if not all([node in self.vertices for node in edge_vertices]):
			raise Exception("All endpoints of edges must belong in vertices")

		if len(self.edges) != len(set(self.edges)):
			duplicate_edges = set([edge for edge in self.edges if self.edges.count(edge) > 1])

			raise Exception("Edges contain duplicates.\nEdges: {}\nDuplicate vertices: {}".format(edges, duplicate_edges))
	def find_all_paths(self,mygraph, start, end, path=[]):
		path = path + [start]
		if start == end:
			return [path]
		paths = []
		for node in mygraph[start]:
			if node not in path:
				newpaths = graph.find_all_paths(mygraph, node, end, path)
				for newpath in newpaths:
					paths.append(newpath)
		return paths
		raise NotImplementedError
	def min_dist(self,start,end):
		dist=999999
		x=0
		for i in graph.find_all_paths(nygraph,start,end):
			if len(i)<=dist:
				x = len(i)
				dist = len(i)
		return x
		raise NotImplementedError
	def all_shortest_paths(self,start_node, end_node):
		x = graph.min_dist(start_node,end_node)
		abc=[]
		for i in graph.find_all_paths(nygraph,start_node,end_node):
			if len(i)==x:
				abc=abc+[i]
		return abc
		raise NotImplementedError
	def betweenness_centrality(self, node):
		other=[];y=0;x=0
		cdict={}
		sum=0
		for i in vertices:
			i=str(i)
			if i!=node:
				other.append(i)
		for i in range(0,len(other)):
			for j in range(i+1,len(other)):
				num=graph.all_shortest_paths(other[i],other[j])
				for k in num:
					if node in k:
						y+=1
				x+=len(num)
				sum += float(y/x)
				x=0
				y=0
		cdict[node]=sum
		return sum
		raise NotImplementedError
	def top_k_betweenness_centrality(self):
		a=[]
		for i in vertices:
			a.append(graph.betweenness_centrality(str(i)))
		sum=0
		for i in a:
			if(i>sum):
				sum=i
		for i in range(len(a)):
			if(a[i]==sum):
				print(i+1)		
if __name__ == "__main__":
	vertices = [1, 2, 3, 4, 5, 6]
	edges    = [(1, 2), (1, 5), (2, 3), (2, 5), (3, 4),(3,6), (4, 5), (4, 6)]
	list1=[];dist=999999;path=[]
	
	graph = Graph(vertices, edges)
	nygraph={'1': ['2', '5'],'2': ['1', '3','5'],'3': ['2','4','6'],'4': ['3', '5', '6'],'5': ['1', '2', '4'],'6': ['4','3']}
	#print(graph.find_all_paths(nygraph,'1','3'))
	#print(graph.all_shortest_paths('1','3'))
	#print(graph.min_dist('1','3'))
	#print(graph.betweenness_centrality('3'))
	(graph.top_k_betweenness_centrality())
	#print(graph.betweenness_centrality('1'))
	