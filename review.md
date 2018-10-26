# Peer-review report

> Welcome to THE GAME. Over the course of peer review you are going to win and lose points. Here are the rules:
> * You work for Correctness points. The minimum is **0**. The maximum is **50**.
> * In general, you start with **25** points.
> * You will start with **0** points if TA find an obvious mistake in the output.
> * You will not know your start amount until THE GAME is finished.
> * You lose **1** points for every *performance problem* found in your code.
> * You lose **3** points for every *wrong output problem* found in your code.
> * You lose **10** points for every distinct case of *hang or crash*.
> * You gain **1** point for every distinct problem correctly *reported*.
> * You gain **3** points if the problem is *reported and located*.
> * You gain **10** points if the problem is *reported, located and fixed*.
> * The problems are considered distinct if they have different origin.
> * In your team list across **your variant**, you get to review only the team listed directly above and the team directly below. If you are the top one, you get to review the second and the last. If you're the last one, you get to review one before last and the first.
> This implies that you *can't* report on yourself or your teammates. 

## Assignment data
**Homework:** HA-3

**Variant:** python

**Language of implementation:** java

**Authors:** Dinar Salakhutdinov & Anastasia Kirdysheva

**Reviewers:** Victoria Rotaru & Elizaveta Batanina

## Overall evaluation

### Correct parts
```
import curses
from curses import KEY_RIGHT, KEY_LEFT

curses.initscr()
win = curses.newwin(20, 60, 0, 0)

score = 0

snake = [[4,10], [4,9]]

win.addch(food[0], '*')

while key != 27:

    if key == ord(' '):
        key = -1
        continue
    else:
        last = snake.pop()

for i in range(10):
    print("\nScore - " + str(score))
```

### General characteristics
* How fast it works:

It works fast enough. No problems at this step.
* How easy was it to launch the program

In the README.md I found explicit steps of installation dependences and launching program.  
* How easy it was to read and understand the code

Code has comments and explicit names for variables, therefore it was not difficult to read.


## Found errors

### Error #1 (test not passes)

#### Kind of error: PROGRAM CRASHES
The test didn't pass. The `testJSON` and `realJSON` has one difference.
`"text": "\r\n"` and `"text": "\n"`

#### How was it found? 
I run the test `TreePrinterTest.java` and the test didn't pass.

#### How to reproduce

Run `TreePrinterTest.java`.

#### Expected behaviour

The test should've pass.

#### Actual behavour

`TreePrinterTest.java` should've been replaced `\r` in the `testGSON.txt`, but because it didn't work the output of the program
was different from the output of the test file. So the test didn't pass.

#### Location of the problem

The problem is in the file `TreePrinterTest.java` at line 21. This 2 slashes are just for the compiler but regex engine 
needs 2 slashes too. Therefore test didn't pass because code didn't replace `\r`.  
```
testJSON = testJSON.replaceAll("\\r", "");
```

#### Solution to the problem

The solution is to add 2 more slashes, 2 for the compiler and 2 for the regex engine.
```
testJSON = testJSON.replaceAll("\\\\r", "");
```

