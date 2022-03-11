def myfunc():
  x = 300
  print(x)
myfunc()
def myfunc():
  x = 300
  def myinnerfunc():
      print(x)
myinnerfunc()
myfunc()
x = 300
def myfunc():
  print(x)
myfunc()
print(x)
def myfunc():
  global x
  x = 300
myfunc()
print(x)
x = 300

def myfunc():
  global x
  x = 200
myfunc()
print(x)
def greeting(name):
  print("Hello, " + name)
import mymodule
mymodule.greeting("Jonathanperson1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
import mymodule
a = mymodule.person1["age"]
print(a)
import mymodule as mx
a = mx.person1["age"]
print(a)
import platform
x = platform.system()
print(x)
import platform
x = dir(platform)
print(x)
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
from mymodule import person1

print (person1["age"])


