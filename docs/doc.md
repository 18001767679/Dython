# Dython Documentation
**Dython** is an open-source Python library created by [Daniel Lawson](https://github.com/Sombrero64), that includes functions that saves room and time.

### Table of Contents

[Instailing Dython](#instailing-dython)

[Oprations](#oprations)

[Temporary Variables](#temporary-variables)

[Console](#console)

## Instaling Dython
1. Download Dython, and extract it. ([ZIP](https://github.com/Sombrero64/Dython/zipball/master)/[TAR](https://github.com/Sombrero64/Dython/tarball/master))
2. Take the Dython's script, **Dython.py**, and insert in your project's folder.
3. Edit scripts that requires Dython's functions, and add an `import` command.

```py
from Dython import *
```

## Operations
The operations (`math`) class contains functions regrading oprating values and objects. There are currently 9 functions under this class.
  
- `itemsAdd()`&`itemsMulti()`: returns the sum or product of all items in a list (argument).

  ```py
  print(math().itemsAdd([1, 2, 3]))
  print(math().itemsMulti([5, 5, 4]))
  ```
  ```
  6.0
  100.0
  ```
  
- `joinStrs()`: returns a joined string of all items in a list (argument).

  ```py
  name = "Davis"
  print(math().joinStrs(["Hello, ", name, "!"]))
  ```
  ```
  Hello, Davis!
  ```
  
- `itemCount()`: returns the amount of items in a list (first argument) that matches the secound argument.(Can be replaced by list.count)

  ```py
  print(math().itemCount(["a", "a", "b"], "a"))
  print(math().itemCount(["a", "a", "b"], "b"))
  print(math().itemCount(["a", "a", "b"], "c"))
  ```
  ```
  2
  1
  0
  ```
  
- `rangeLimit()`: sets a limit to a number's (first) range with a minimum and maximum (secound and third arguments).

  ```py
  print(math().rangeLimit(5, 0, 10))
  print(math().rangeLimit(11, 0, 10))
  print(math().rangeLimit(-3, 0, 10))
  print(math().rangeLimit(7, 0, 10))
  ```
  ```
  5
  10
  0
  7
  ```
  
- `feturn()`: returns either the secound or third argument depending on a Boolean (first). If true, secound. Otherwise, third.
  
  ```py
  print(math().feturn(False, "Yes", "No"))
  print(math().feturn(True, "Yes", "No"))
  
  print('')
  
  print(math().feturn(False, "On", "Off"))
  print(math().feturn(True, "On", "Off"))
  ```
  ```
  No
  Yes
  
  Off
  On
  ```
  

- `listInits()`: returns a list of numbers regrading instances of items matching the secound argument in a list (first argument). If no such item exists, it returns _None_.

  ```py
  print(math().listInits([4, 0, 2, 5, 0, 3, 0], 0))
  ```
  ```
  [1, 4, 6]
  ```
  
- `filterList()`: returns a list (first) without items matching the secound argument.

  ```py
  print(math().filterList([0, 1, 0, 0, 2, 3, 0, 4, 5], 0))
  ```
  ```
  [1, 2, 3, 4, 5]
  ```
-`map`: simalar to Snap! map

## Temporary Variables
Temporary Variables are variables that were designed for temporary use. After their use is over, they are easily removed. All functions that uses them are from the `temp` class, which contains over 4 functions.

- `define()`: defines a temporary variable. Its name is the first argument, and its starting value is the secound argument.

  ```py
  a=temp()
  a.define("myTemp", 0)
  ```
  
  It doesn't do anything if there was already a temporary variable named as such.

- `get()`: returns the value of a temporary variable (first argument). It returns _None_ if the temporary variable doesn't exist.

  ```py
  a=temp()
  a.define("myTemp", 25)
  print(a.get("myTemp"))
  ```
  ```
  25
  ```

- `set()`: sets the value of a temporary variable (first argument) to the secound argument.

  ```py
  a=temp()
  a.define("myTemp", 0)
  print(a.get("myTemp"))
  
  a.set("myTemp", 50)
  print(a.get("myTemp"))
  ```
  ```
  0
  50
  ```
  
- `remove()`: removes a temporary variable.

  ```py
  a=temp()
  a.remove("myTemp")
  ```


  You can use the list `temps` for advanced purposes.
  
  > `[name, value]`
  
  ```py
  a=temp()
  a.define("VarA", 0)
  a.define("VarB", "abc")
  a.define("VarC", True)
  a.define("VarD", [0, 1, 2])

  print(a.temps)
  ```
  ```
  [['VarA', 0], ['VarB', 'abc'], ['VarC', True], ['VarD', [0, 1, 2]]]
  ```
  > Please refrain from using the temps variable differently, such as setting it as a different type. If you do this, these functions above might not work.
  > ```py
  > a=temp()
  > a.temps = "abc"
  >
  > a.define("dummy", None)
  >
  > print(a.temps)
  > ```
  > ```
  > abc
  > ```
  
# Console
The `console` class contains functions regrading the console. There is only one function.

- `menu()`: allows you to apply a multichoice input into the console, allowing the user to pick an option.
  
  ```py
  answer = console().menu(None, ["a", "b", "c", "d"], False)
  ```
  ```
  0: a
  1: b
  2: c
  3: d
  ```
  
  The first argument allows you to provide a caption, such as the question. Leaving it as a blank string, or providing _None_ would not make a caption.
  
  The secound argument is your options from a list.
  
  To allow an empty anwser to be provided, set the third argment to True. If the user provides an empty anwser, it will return _None_. Otherwise, set it False.
