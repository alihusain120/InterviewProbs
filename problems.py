import math
import random

def findWords(words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        topRow = 'QWERTYUIOPqwertyuiop'
        middleRow = 'ASDFGHJKLasdfghjkl'
        bottomRow = 'ZXCVBNMzxcvbnm'
        
        # check first letter for row
        
        for x in words:
            
            
            if x[0] in bottomRow:
                
                words.remove(x)
                
            elif x[0] in topRow:
                # check rest of letters are in topRow
                for i in range(1, len(x)):
                    if x[i] not in topRow:
                        
                        words.remove(x)
                        
            elif x[0] in middleRow:
                # check rest of letter are in middleRow
                for i in range(1, len(x)):
                    if x[i] not in middleRow:
                        
                        words.remove(x)
                 
        return words

def amazonProblem(inputStr, num):
    
    toReturn = []
    
    for i in range(len(inputStr) - num):
        currentStr = inputStr[i:i+4]
        if isUnique(currentStr) and currentStr not in toReturn:
            toReturn.append(currentStr)
        
    return toReturn
                
        
        
        
def isUnique(inputStr):
    for i in range(len(inputStr)):
        if inputStr[i] in inputStr[i+1:]:
            return False
    
    return True

# calculate sqrt by babylonian algo
def babylonian_sqrt(S):
    # Your code goes here!
    if S < 0:
        return "undefined"
    
    initial_guess = S // 2
    guess = float(initial_guess)
    while guess != round(math.sqrt(S), 15):
        guess = (guess + (S / guess)) / 2
    return guess


# give change for given amount of cents
def num_coins(cents):
        num_quarters = cents // 25
        cents -= (num_quarters*25)

        num_dimes = cents // 10
        cents -= (num_dimes*10)

        num_nickels = cents // 5
        cents -= (num_nickels*5)

        num_pennies = cents

        return num_quarters + num_dimes + num_nickels + num_pennies



#return number of trailing zeroes
def fac_zeros(n):
        facs = [1]* (n+1)
        return fac_zeros2(n, facs)

def fac_zeros2(n, facs):
        if n == 0 or n == 1:
                return 1

        if facs[n] == 1:
                facs[n] = fac_zeros2(n-1, facs) * n

        return facs[n]


class Node:

        def __init__(self, value, nextNode):
                self.value = value
                self.nextNode = nextNode

        def hasNext(self):
                return True if self.nextNode != None else False


def main():


        '''
        # Following for testing Node class and remove_dups()

        
        node1 = Node(1, None)
        node2 = Node(2, None)

        node1.nextNode = node2
        
        # print(node1.value)
        # print(node1.nextNode.value)
        
        mainHead = node1
        head = node1
        
        for i in range(3, 20):
                node2.nextNode = Node(random.randint(1, 11), None)
                                      
                node1 = node2
                node2 = node2.nextNode

        while(head != None):
                print(head.value)
                head = head.nextNode

        print("----After remove dups:")
        head = mainHead
        
        remove_dups(head)
        while(head != None):
                print(head.value)
                head = head.nextNode

        '''
        stacky = Stack()
        node0 = Node(0, None)
        noder = node0
        stacky.push(noder.value)
        for i in range(10):
                noder.nextNode = Node(random.randint(1, 11), None)
                noder = noder.nextNode
                stacky.push(noder.value)

        noder = node0

        stackTest = stacky
                
        while(noder != None):
                print(str(noder.value) + "\t" + str(stacky.pop()))
                noder = noder.nextNode

        print("------")
        stacky.push(19)

        while(not stackTest.is_empty()):
                print(stackTest.pop())
        # print(is_palindrome(node0))
        
              
def remove_dups(head):
        arr = []
        return remove_dups_helper(head, arr)

def remove_dups_helper(head, arr):
        curr = head
        nextn = head.nextNode
        arr.append(curr.value)
        while nextn != None:
                if nextn.value in arr:
                        curr.nextNode = nextn.nextNode
                        nextn = curr.nextNode
                else:
                        arr.append(nextn.value)
                        curr = nextn
                        nextn = curr.nextNode
        return head


def fibonacci(i):
        return fibonacci_helper(i, [0]*(i+1))

def fibonacci_helper(i, memo):
        if i == 0 or i == 1:
                return i

        if memo[i] == 0:
                memo[i] = fibonacci_helper(i-1, memo) + fibonacci_helper(i-2, memo)

        return memo[i]

def power_set(arr):
        
        memo = [[arr[0]]]

        for i in range(1, len(arr)):
                memo.append(memo[-1] + [arr[i]])

        return memo

def permutations_without_dups(given_str):
        list_perms = []

        if len(given_str) == 1:
                list_perms.append(given_str)

        else:
                first_char = given_str[0]
                rest = given_str[1:]
                list_rest = permutations_without_dups(rest)

                for word in list_rest:
                        for i in range(len(word)+1):
                                list_perms.append(insert_char_at(first_char, word, i))

        return list_perms

def insert_char_at(ch, given, index):
        if index >= len(given):
                toReturn = given + str(ch)

        else:
                toReturn = given[0:index] + ch + given[index:]

        return toReturn


class Stack:
        def __init__(self):
                self.top = None

        def push(self, value):
                thisNode = Node(value, self.top)
                self.top = thisNode

        def pop(self):
                toReturn = self.top.value
                self.top = self.top.nextNode
                return toReturn

        def peek(self):
                return self.top

        def is_empty(self):
                if self.top is None:
                        return True
                else:
                        return False


def is_palindrome(head):
        myStack = Stack()
        iterator = head

        while iterator is not None:
                myStack.push(iterator)
                iterator = iterator.nextNode

        while head is not None:
                if head.value != myStack.pop().value:
                        return False
                head = head.nextNode

        return True



def tester():
        for i in range(0, 10, 1):
                print(i)

        print("---")
        for j in range(10, -1, -1):
                print(j)


def minimumGroups(predators):
        maxHeight = 0
        for i in range(len(predators)):
                maxHeight = max(maxHeight, minGroupsRecurse(i, predators))

        return maxHeight

def minGroupsRecurse(i, predators):
        if predators[i] == -1:
                return 1
        else:
                return 1 + minGroupsRecurse(predators[i], predators)


def removeDuplicates(nums) -> int:
        #Empty, 1 element
        
        counter = 0
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                counter += 1
                
                
        return len(nums)-counter
                
def one_move_away(word1, word2):
