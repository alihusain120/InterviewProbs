# Towers of Hanoi program
# First half: implement Towers of Hanoi game
# Second half: implement algo that solves game in minimum moves, using stacks
    # Dynamic programming required (probably)


'''

*********************************Towers of Hanoi**************************
Given 3 towers with a total of N disks starting at the left tower.
Each disk is a different size, with the disks sorted in ascending order.

The goal is to move all the disks from the left tower to the right tower given the rules:
1. Only one disk can be moved at a time.
2. A disk is removed from the top of one tower and placed on another tower.
3. A disk cannot be placed on top of a smaller disk.

'''

''' Testing stuff
print('|\t*\t \t  \t    | \n|\t*\t \t  *\t    |')
print('|\t*\t \t  *\t    |')
print('|\t*\t *\t  **\t    |')
print('|\t*\t **\t  ***\t    |')
arr = ["|", "*", "**", "***", "|"]
'''

def make_the_board(num_disks):

    for i in range(1, num_disks+1):
        print('|\t' + ('*' * i) + "\t \t \t|\n")

    print((' \t' + ('_' * num_disks)) * 3)
    
    if(num_disks > 3):
        print((' \t' + ("  L  ")) + (' \t' + ("  M  ")) + (' \t' + ("  R  ")))
    else:
        print((' \t' + (" L ")) + (' \t' + (" M ")) + (' \t' + (" R ")))
    
        
        


