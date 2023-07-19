from linkedlist import *
from data import *
from tree import *

def hello():
  print("~~~<< Hello and welcome to your Santiago de Chile's Attractions Recommendation App >>~~~ \n ")
  userinfo = input("First, tell me... Do you want to visit an interesting place or know the best restaurants in the zone? (type Attraction or Restaurant): ")
  while userinfo.lower() != 'attraction' and userinfo.lower() != 'restaurant':
    userinfo = input('Please type a valid word: ')
  return userinfo

def importdata():
  trees = {}
  for sublist in data:
    copia = sublist.copy()
    name = copia[1].replace(' ','_').replace('á','a').lower()
    treenode = Tree(copia)
    trees[name] = treenode
  return trees

sol = importdata()
for ele in sol:
    print(sol[ele])