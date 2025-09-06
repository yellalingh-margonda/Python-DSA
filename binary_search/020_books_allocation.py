import sys


# function to check if it is possible to allocate the books
# such that the maximum number of pages assigned to any student is numPages
def isPossible(pages, n, m, numPages):
    cntStudents = 1
    curSum = 0
    for i in range(n):
        # if a book has more pages than numPages, return False
        if pages[i] > numPages:
            return False

        # if the current sum of pages exceeds numPages,
        # assign the current book to the next student and update curSum
        if curSum + pages[i] > numPages:
            cntStudents += 1
            curSum = pages[i]

            # if the count of students becomes greater than given no. of students, return False
            if cntStudents > m:
                return False
        else:
            # else assign this book to the current student and update curSum
            curSum += pages[i]
    return True


def allocateBooks(pages, n, m):
    # if number of students is more than number of books
    if n < m:
        return -1
    sum = 0
    for i in range(n):
        sum += pages[i]
    start = 0
    end = sum
    result = sys.maxsize
    # traverse until start <= end , binary search
    while start <= end:
        mid = start + (end - start) // 2
        # checking if it is possible to distribute books by using mid as current maximum
        if isPossible(pages, n, m, mid):
            result = min(result, mid)
            end = mid - 1
        else:
            start = mid + 1
    return result


n = 4
m = 2
pages = [10, 20, 30, 40]
print("The minimum value of the maximum number of pages in book allocation is:", allocateBooks(pages, n, m))