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

The decorator will generate the following output for instance:

```function loop_10m took 5.04 s```

