# i/o shit
n = int(input().strip())
s = input().strip()
n, m = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
for _ in range(int(input().strip()))
grid = [list(input().strip()) for _ in range(n)]

# Useful facts
# formula for finding end position after b steps when starting from pos a in 1-n roundhouse: ((a+b-1)%n)+1
# interior angle of a regular polygon : (n-2)*180/n
# formula for finding digital_root of number digsum(digsum(...(n))) : (n-1) mod 9 + 1
# floor to ceil --> ceil(n/m) = (n+m-1)//2
# ceil to floor --> n//m = ceil((n-m+1)/2) 

# split a string where consecutive letters are diff
arr = [m.group(0) for m in re.finditer(r"([a-z])\1*", s)]


def modinv(a, m):
	def egcd(a, b):
		if a == 0:
			return (b, 0, 1)
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)
	g, x, y = egcd(a, m)
	return x % m

def printGrid(grid):
	for row in grid:
		print(' '.join(list(map(str, row))))

def isPrime(n):
	# a prime(except 2 or 3) is of the form 6k-1 or 6k+1
	if n == 2 or n == 3:
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False
	i = 5
	w = 2
	sqN = int(pow(n, .5))
	while i <= sqN:
		if n % i == 0:
			return False
		i += w
		w = 6 - w
	return True

# finds factors of n <= 10**14 in 1.5s
def factors(n):
	from functools import reduce
	return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))	

# is x a subsequence of s
def isSubseq(s, x):
	i, j = 0, 0
	while True:
		if j == len(x):
			return True
		if i == len(s):
			return False
		if s[i] == x[j]:
			j += 1
		i += 1

# RightRotate a number (without zeros)
def rotate_right(n):
	# 12345 -> 51234
	return n%10*(10**(len(str(n))-1)) + n//10

# LeftRotate a number (without zeros)
def rotate_left(n):
	# 12345 -> 23451
	return (n%(10**(len(str(n))-1)))*10  + n//(10**(len(str(n))-1))

# Generate primes <= n
def genPrimes(n):
	sieve = [True]*(n+1)
	p = 2
	while p*p <= n:
		if sieve[p]:
			for i in range(p*p, n+1, p):
				sieve[i] = False
		p += 1
	primes = []
	for i in range(2, n+1):
		if sieve[i]:
			primes.append(i)
	return primes

# Bitmasking
arr = [1, 2, 3]
n = 3
for i in range(1<<n):
	s = []
	for j in range(n):
		if i & (1<<j):
			s.append(arr[j])
	print(s)

# Prints 2D array without stupid commas
def printGrid(grid):
	for row in range(len(grid)):
		print(*[grid[row][col] for col in range(len(grid[row]))])	

# Maximum sum subarray
def kadane(a):
	currMax = globalMax = a[0]
	for i in range(1, len(a)):
		currMax = max(a[i], currMax+a[i])
		globalMax = max(currMax, globalMax)
	return globalMax

# Longest increasing subsequence
def longest_inc_subs(arr):
	n = len(arr)
	dp = [1]*n
	for i in range(1, n):
		for j in range(i):
			if arr[i] >= arr[j]:
				dp[i] = max(dp[i], dp[j]+1)
	return max(dp)

'''TREE'''
from queue import Queue
class Node:
	def __init__(self, val):
		self.data = val
		self.left = None
		self.right = None

	def bfs(root):
		if root is None:
			return
		q = Queue()
		q.put(root)
		while not q.empty():
			node = q.get()
			print(node.data)
			if node.left:
				q.put(node.left)
			if node.right:
				q.put(node.right)

	def dfsInorder(root):
		# inorder
		if root:
			dfsInorder(root.left)
			print(root.data)
			dfsInorder(root.right)

	def maxDepth(root):
		if root is None:
			return 0
		lDepth = maxDepth(root.left)
		rDepth = maxDepth(root.right)
		return max(lDepth, rDepth) + 1


# Segment Tree
# AMAZING REF: https://codeforces.com/blog/entry/18051
from math import inf
N = int(1e5)+3
tree = [0]*(2*N)
def build():
	for i in range(n-1, -1, -1):
		tree[i] = min(tree[2*i], tree[2*i+1])

def modify(ind, val):
	ind += n
	tree[ind] = val
	while ind > 1:
		ind //= 2
		tree[ind] = min(tree[2*ind], tree[2*ind+1])

def query(left, right):
	# [left, right)
	left += n
	right += n
	mini = inf
	while left < right:
		# if either of left or right is odd, incr or decr so we can 
		# divide them by 2 to move to the above layer
		if left%2:
			mini = min(mini, tree[left])
			left += 1
		if right%2:
			right -= 1
			mini = min(mini, tree[right])
		left //= 2
		right //= 2
	return mini
