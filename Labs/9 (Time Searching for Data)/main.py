# Author: David Miller | djm545
# Date: 6/7/23
# Purpose: Compare the time it takes to search for an item in a list vs searching for it in a binary search tree.

import random
from BST import *


def populateList(n, s):
    ##TODO: implement your logic here
    random.seed(s)
    lst = [x for x in range(n)]
    random.shuffle(lst)
    return lst

def searchLength(lst, n):
    num = 0
    for x in lst:
        num += 1
        if x == n:
            return num
    return len(lst)
        
def listToBST(lst):
    binarySearchTree = BST()
    for x in lst:
        binarySearchTree.append(x)
    return binarySearchTree

if __name__ == "__main__":
    ##TODO: implement your logic here
    averageList = []
    averageBST = []
    
    for n in range(1, 1000, 100):
        sumcountlist = 0
        sumcountbst = 0
        numruns = 0
        for s in range(1, 5):
            lst = populateList(n, s)
            bst = listToBST(lst)
            for v in range(n):
                sumcountlist += searchLength(lst, v)
                sumcountbst += bst.searchLength(v)
                numruns += 1
        averageList.append(sumcountlist / numruns)
        averageBST.append(sumcountbst / numruns)
    print(f'Average Search Length for List: {averageList}')
    print(f'Average Search Length for BST: {averageBST}')


