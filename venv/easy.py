import helper


# O(n) time | O(n) space
def twoNumberSum(array, target):
    numbers = {}
    for num in array:
        potentialNumber = target - num
        if potentialNumber in numbers:
            return [potentialNumber, num]
        else:
            numbers[num] = True
    return []


# O(n^2) time | O(n) space
def isPalindrome(string):
    reversedString = ""
    for i in reversed(range(len(string))):
        reversedString += string[i]
    return reversedString == string


# O(n ^ 2) time | O(1) space
def bubbleSort(arr):
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:  # if the current number is greather then the next, swap tem
                helper.swap(i, i + 1, arr)
                isSorted = False
    return arr


# O(n2) |  O(1) space
def insertionSort(arr):
    for i in range(1, len(arr)):
        j = 1
        # as long as we are not at the first number and the current number is smaller
        # then the before number swap the numbers and decrement [j]
        while j > 0 and arr[j] < arr[j - 1]:
            helper.swap(j, j - 1, arr)
            j -= 1
    return arr


# O(n2) time | O(1) space
# [4, 2, 3, 1,7,5]
def selectionSort(arr):
    currentIdx = 0
    while currentIdx < len(arr) - 1:  # run until the before last item
        smallestInx = currentIdx
        for i in range(currentIdx + 1, len(arr)):
            if arr[smallestInx] > arr[i]:
                smallestInx = i
        helper.swap(currentIdx, smallestInx, arr)
        currentIdx += 1
    return arr


def getNewLetter(letter, key):
    newLetterCode = ord(letter) + key
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)


# very important - need to know how to implement
def binarySearch(array, target):
    binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    potentialMiddle = array[middle]
    if target == potentialMiddle:
        return middle
    elif target < potentialMiddle:
        return binarySearchHelper(array, target, left, middle - 1)
    else:
        return binarySearchHelper(array, target, middle + 1, right)


# time = o(N) | space = o(D)
def productSum(array, multiplier=1):
    totalSum = 0
    for element in array:
        if type(element) is list:
            totalSum += productSum(element, multiplier + 1)
        else:
            totalSum += element
    return totalSum * multiplier


# start - three largest number
def threeLargestNumbers(arr):
    threeLargest = [None, None, None]
    for number in arr:
        updateLargest(threeLargest, number)

    return threeLargest


def updateLargest(threeLargest, num):
    if num > threeLargest[2]:
        shiftNumber(threeLargest, num, 2)
    if num > threeLargest[1]:
        shiftNumber(threeLargest, num, 1)
    if num > threeLargest[0]:
        shiftNumber(threeLargest, num, 0)


def shiftNumber(arr, num, idx):
    for i in range(idx + 1):
        if i == idx:
            arr[i] = num
        else:
            arr[i] = arr[i + 1]


# end - three largest number

# o(N) time |
def branchSum(root):
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums


def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return

    newRunningSum = runningSum = node.value
    if node.left is None or node.right is None:
        sums.append(newRunningSum)
        return

    calculateBranchSums(node.left, runningSum, sums)
    calculateBranchSums(node.right, runningSum, sums)


# o(n^2) time | o(n) space
def fib(n):
    if n == 2:
        return 1
    if n == 1:
        return 0
    else:
        return fib(n - 1) + fib(n - 2)
