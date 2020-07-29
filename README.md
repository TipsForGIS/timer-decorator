# timer-decorator

This is a Python decorator for timing functions

e.g.

```
@timer
def loop_10m(a,b,c,..):
  for i in range(10000000):
    a = i * 3
    b = a - c
    c = c * c
```
