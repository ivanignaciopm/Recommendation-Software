class Node:
  def __init__(self, value = None):
    self.value = value
    self.next_node = None

class LinkedList:
  def __init__(self, head_node = None):
    self.head_node = head_node
  
  def insert_beginning(self, new_node):
    new_node = Node(new_node)
    new_node.next_node = self.head_node
    self.head_node = new_node
  
  def remove_node(self, value_to_remove):
    current_node = self.head_node
    if current_node.value == value_to_remove:
      self.head_node = self.head_node.next_node
      current_node = None
    
    while current_node:
      next_node = current_node.next_node
      if next_node.value == value_to_remove:
        current_node.next_node = next_node.next_node
        current_node = None
      else:
        if next_node is not None:
          current_node = next_node
        else:
          print("no value found")
          break
        