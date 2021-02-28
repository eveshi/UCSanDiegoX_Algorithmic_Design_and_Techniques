import sys, threading
import math

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  if not len(tree):
    return True

  def dfs(pos, less_than, greater_than):
    if pos == -1:
      return True
    if tree[pos][0] >= less_than or tree[pos][0] <= greater_than:
      return False

    return dfs(tree[pos][1], tree[pos][0], greater_than) and dfs(tree[pos][2], less_than, tree[pos][0]-1)

  return dfs(0, math.inf, -math.inf)
     


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()