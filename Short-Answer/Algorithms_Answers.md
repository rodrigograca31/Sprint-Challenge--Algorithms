#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n/2) = O(n)

b) O(n log n)

c) O(n!)

## Exercise II

Since the floor numbers are sequential and ordered I can use a divide and conquer algorithm to find the floor where the eggs break with th minimum amount of drops thus minimum amount of broken egs.

For that I will choose a floor at the middle, then drop an egg and see if it broke or not. If it does break I will got to half of my floor number and drop another egg. If it didnt break I will go to my current floor number + half of the ones above me.

And I repeat until I'm only 1 floor apart from the last broken and can't go up because I already know the next one breaks the egg

Something like:

```python
go_to_floor(n/2)
    if n>2:
        drop_egg
        if it_broke:
            go_to_floor(n/2)
        else:
            go_to_floor(n+n/2)
    else:
        return n
```

This algorithm would have a `O(log(n))` because its a binary search where we only search half of it each iteration
