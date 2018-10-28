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

**Language of implementation:** python

**Authors:** Dmitry Turenko & Amir Nazyrov

**Reviewers:** Victoria Rotaru & Elizaveta Batanina

## Overall evaluation

### Correct parts
```
x = 0

while x <= 0:
     print(x)

```

### General characteristics
* How fast it works:

It works fast enough. No problems at this step.
* How easy was it to launch the program:

In the `README.md` I found explicit steps of installation dependences and launching program.  Program also conatins requirements.txt that makes it easy to set requirements
* How easy it was to read and understand the code:

Code contains docstrings which describe function behavior -> it is esy to understand code. 
* Any other comments of general nature, with examples as needed:

Tests doesn't cover all functionality that was mentioned in task. Better add tests that demonstrate that all language constructs are parsed well

## Error #1(wrong output value) 
If you try to test program on following code:
```angular2html
from time import time

def donno_how_to_call():
    x = [1, 2, 4, 21213, 42]
    for i, _x in enumerate(x):
        print(_x * x[i+1 if i != len(x)-1 else 0])

```
The output will contain wrong values for token:
```angular2html
                                  {
                                    "Type": "NEWLINE",
                                    "Value": ")"
                                  }
                                ]
                              }
                            },
                            {
                              "Type": "DEDENT",
                              "Value": ")"
                            }
                          ]
                        }
                      ]
                    }
                  }
                },
                {
                  "Type": "DEDENT",
                  "Value": ")"
                }
              ]
            }
          ]
        }
      }
    },
    {
      "Type": "DEDENT",
      "Value": "e 0])"
    }
  ]
}
```

### Kind of error: WRONG OUTPUT

### How was it found:
Just placing code mentioned earlier in in.txt

### How to reproduce:
Place code in in.txt and run launcher.py (you may also exclude running lines 110 and 111 in launcher.py)

### Expected behaviour:
Output should contain right values of tokens:
```angular2html
"Type": "NEWLINE",
"Value": "\n" # as stated in Python3.g4 that NEWLINE is actually '\n' char

```
```angular2html
 {
      "Type": "DEDENT",
      "Value": "<EOF>"
    }
```
### Actual behaviour:
Wrong output. See description of an error
