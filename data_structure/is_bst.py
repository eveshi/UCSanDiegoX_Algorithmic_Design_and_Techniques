import sys, threading
import math

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class IsBinarySearchTree:

  def __init__(self, tree):
    self.prev = -math.inf
    self.tree = tree

  def check(self):
  # Implement correct algorithm here
    if not len(self.tree):
        return True

    def dfs(pos):
      if pos == -1:
          return True
      if not dfs(self.tree[pos][1]):
          return False
      if self.tree[pos][0] <= self.prev:
          return False
      self.prev = self.tree[pos][0]
      return dfs(self.tree[pos][2])

    return dfs(0)
     


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree).check():
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()