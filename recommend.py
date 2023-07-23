from linkedlist import *
from data import *
from tree import *

recommendtree = Tree('Recommendation')
food_tree = Tree('Food Types')
locations_tree = Tree('Locations')

recoleta = Tree('Recoleta')
providencia = Tree('Providencia')
las_condes = Tree('Las Condes')
vitacura = Tree('Vitacura')
santiago = Tree('Santiago')
metropolitan = Tree('Metropolitan')

alemana = Tree('Alemana')
contemporanea_chilena = Tree('Contemporánea-Chilena')
peruana_chilena = Tree('Peruana-Chilena')
chilena = Tree('Chilena')
ancestral_chilena = Tree('Ancestral-Chilena')
japonesa = Tree('Japonesa')
thai = Tree('Thai')
mediterranea = Tree('Mediterránea')
international = Tree('International')

def tree_creation():
  recommendtree.add_child(food_tree)
  recommendtree.add_child(locations_tree)
  locations_tree.add_child(recoleta)
  locations_tree.add_child(providencia)
  locations_tree.add_child(las_condes)
  locations_tree.add_child(vitacura)
  locations_tree.add_child(santiago)
  locations_tree.add_child(metropolitan)
  food_tree.add_child(alemana)
  food_tree.add_child(contemporanea_chilena)
  food_tree.add_child(peruana_chilena)
  food_tree.add_child(chilena)
  food_tree.add_child(ancestral_chilena)
  food_tree.add_child(japonesa)
  food_tree.add_child(thai)
  food_tree.add_child(mediterranea)
  food_tree.add_child(international)
def locations_addchildren():
  #adds locations to its father tree 
  for location in locations_tree.children:
    #print(location.value)
    for info in data:
      if info[0] == 'Restaurant':
        if location.value in info[5]:
          location.add_child(Tree(info))
          #print('-' + info[2])
          continue
      if location.value in info[4]:
        location.add_child(Tree(info))
        #print('-' + info[1])
def foods_addchildren():
  for food in food_tree.children:
    #print(food.value)
    for info in data:
      if info[0] == 'Restaurant':
        if food.value in info[1]:
          food.add_child(Tree(info))
          #print('-' + info[2])
def hello():
  print("Hello and welcome to your Santiago de Chile's Attractions Recommendation App. \n ")
  print("We will provide you some interesting info about what you can do based on the district you are right now!")
  print("Hungry? Don't worry, we can also assist you with the best Restaurant's on the area!\n")
  userinfo = input("First, tell me... Are you searching for Attractions, Restaurants or Both?: \n")
  while userinfo.lower() != 'attractions' and userinfo.lower() != 'restaurants' and userinfo != 'both'.lower():
    userinfo = input('\nPlease type a valid word: \n')
  return userinfo

tree_creation()   
locations_addchildren()
foods_addchildren()

def recommend():
  if user.lower() == 'attractions':
    userlocation = input("\n\nOk!, Now tell me the district where are you located right now!:\n")
    result = []
    while len(result) != 1:
      for location in locations_tree.children:
        if userlocation.lower() in location.value.lower():
          result.append(location.value)

      if len(result) == 0:
        userlocation = input('\nNo matches found!, please try with another word:\n')
        if userlocation.lower() not in location.value.lower():
          for caca in locations_tree.children:
            print(caca.value)
          userlocation = input('\nThese are the locations available for search, Try again:\n')

      if len(result) > 1:
        print('\nThese are the matches with the answer you provided:\n')
        for loca in result:
          print(loca)
        userlocation = input('\nPlease choose one of them:\n')
        result = []
    
    print(f'\n\nThe attractions available in {result[0]} are:')
    for location in locations_tree.children:
      if location.value == result[0]:
        matches = location.children
        matchesattractions = []
        matchesrestaurants = []
        for info in matches:
          if info.value[0] == 'Attraction':
            matchesattractions.append(info)
          if info.value[0] == 'Restaurant':
            matchesrestaurants.append(info)

        if len(matchesattractions) == 0:
          ans = input('For this location there are no attractions available. Although there are some restaurants that might interest you.\n Do you wanna check them?\n')
          while ans.lower() != 'yes' and ans.lower() != 'no':
            ans = input('\nType yes or no:\n')
          if ans == 'yes':
            print(matchesrestaurants)
        else:
          print(matchesattractions)

user = hello()
recommend()
again = input('\n\nDo you want to search for anything else:\n')
if again.lower() == 'yes':
  recommend()
else:
  print('Bye!')
#for place in places:
  #lower = place.lower().replace(' ','_')
  #print(f"{lower} = Tree('{place}')")
  #print(f'locations_tree.add_child({lower})')
#for food in food_types:
  #lower = food.lower().replace(' ','_')
  #print(f"{lower} = Tree('{food}')")
  #print(f'food_tree.add_child({lower})')

