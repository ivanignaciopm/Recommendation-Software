from data import *
from tree import *
import unicodedata
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
chilena = Tree('Chilena Tradicional')
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
  print("\nHello and welcome to your Santiago de Chile's Attractions Recommendation App. \n ")
  print("We will provide you some interesting info about what you can do based on the district you are right now!")
  print("Hungry? Don't worry, we can also assist you with the best Restaurant's on the area!")
tree_creation()   
locations_addchildren()
foods_addchildren()
hello()


def recommend():
  userinfo = input("\nFirst, tell me... Are you searching for Attractions or Restaurants?:(Type 'A' or 'R') \n")
  while userinfo.lower() != 'a' and userinfo.lower() != 'r':
    userinfo = input('\nPlease type a valid word: \n')
  if userinfo.lower() == 'a':
    userlocation = input("\nOk!, Now tell me the district where are you located right now!:\n")
    result = []
    while len(result) != 1:
      for location in locations_tree.children:
        if userlocation.lower() in location.value.lower():
          result.append(location.value)

      if len(result) == 0:
        userlocation = input('\nNo matches found!, please try with another word:\n')
        for location in locations_tree.children:
          if userlocation.lower() in location.value.lower():
            result.append(location.value)
        if len(result) == 0:
          for caca in locations_tree.children:
            print(caca.value)
          userlocation = input('\nThese are the locations available for search, Try again:\n')

      if len(result) > 1:
        print('\nThese are the matches with the answer you provided:\n')
        for loca in result:
          print(loca)
        userlocation = input('\nPlease choose one of them:\n')
        result = []
    
    print(f'\nThe attractions available in {result[0]} are:')
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
          ans = input('For this location there are no attractions available. Although there are some restaurants that might interest you.\nDo you wanna check them?\n')
          while ans.lower() != 'yes' and ans.lower() != 'no':
            ans = input('\nType yes or no:\n')
          if ans == 'yes':
            print(matchesrestaurants)
        else:
          print(matchesattractions)

  if userinfo.lower() == 'r':
    userfood = input('\nNice!, what type of food are you searching for?\n')
    normalized =  userfood.replace('á','a').replace('é','e').replace('ó','o').lower()
    result = []
    while len(result) != 1:
      for food in food_tree.children:
        normfood = food.value.replace('á','a').replace('é','e').replace('ó','o').lower()
        if normalized in normfood:
          result.append(food.value)

      if len(result) == 0:
        userfood = input('\nNo matches found!, please try with another word:\n')
        normalized =  userfood.replace('á','a').replace('é','e').replace('ó','o').lower()
        for food in food_tree.children:
          normfood = food.value.replace('á','a').replace('é','e').replace('ó','o').lower()
          if normalized in normfood:
            result.append(food.value)
        if len(result) == 0:
          for food in food_tree.children:
            print(food.value)
          userfood = input('\nThese are the locations available for search, Try again:\n')
          normalized =  userfood.replace('á','a').replace('é','e').replace('ó','o').lower()

      if len(result) > 1:
        print('\nThese are the matches with the answer you provided:\n')
        for loca in result:
          print(loca)
        userfood = input('\nPlease choose one of them:\n')
        normalized =  userfood.replace('á','a').replace('é','e').replace('ó','o').lower()
        result = []

    print(f'\nThe restaurants available of {result[0]} food are:')
    for food in food_tree.children:
      if food.value == result[0]:
        matches = food.children
        for restaurant in matches:
          if len(restaurant.value) != 0:
           print(f'\n{restaurant.value[2]}:\n - Food type:{ restaurant.value[1]} \n - Food Rating:{ restaurant.value[3]}\n - Attention:{ restaurant.value[4]}\n - Adress:{ restaurant.value[5]}\n')
  again = input('\nDo you want to search for anything else:\n')
  if again.lower() == 'yes':
    recommend()
  else:
    print('Bye!')

recommend()

#for place in places:
  #lower = place.lower().replace(' ','_')
  #print(f"{lower} = Tree('{place}')")
  #print(f'locations_tree.add_child({lower})')
#for food in food_types:
  #lower = food.lower().replace(' ','_')
  #print(f"{lower} = Tree('{food}')")
  #print(f'food_tree.add_child({lower})')

