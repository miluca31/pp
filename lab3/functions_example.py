#1
def my_function():
  print("Hello from a function")
#2
def my_function():
  print("Hello from a function")
my_function()
#3
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")
#4
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
#5
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil")
#6
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
#7
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
#8
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
#9
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
#10
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)
#11
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
#12
def myfunction():
  pass
#13
def my_function(x, /):
  print(x)

my_function(3)
#14
def my_function(x):
  print(x)

my_function(x = 3)
#15
def my_function(x, /):
  print(x)
my_function(x = 3)
#16
def my_function(*, x):
  print(x)
my_function(x = 3)
#17
def my_function(x):
  print(x)

my_function(3)
#18
def my_function(*, x):
  print(x)

my_function(3)
#19
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)
#20
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

