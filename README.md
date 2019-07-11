# ensemble

*A model ensemble utility optimized for low barrier integration*

**TL;DR** if you find yourself needing to use one function to call many functions, this is what you need.

### Examples

Multiplex between functions:

```
>>> from ensemble import Ensemble
>>> def function1(x):
...     return x**2
...
>>> def function2(y):
...     return y**3
...
>>> my_ensemble = Ensemble(
...     name='e1',
...     model_fns=[function1, function2],
... )
>>> my_ensemble(model='function1', x=2)
4
>>> my_ensemble(model='function2', y=2)
8
```

Easily call them all:

```
>>> my_ensemble.all(x=4, y=3)
{'function1': 16, 'function2': 27}
```

If you have a monolithic codebase you may prefer to specify your models within the same file they are defined, without importing your Ensemble. With `ensemble`, you may simply decorate your model functions in order to attach them to an ensemble:

```
>>> from ensemble import model
>>> @model('e2')
... def func1(x):
...     return x**2
...
>>> @model('e2')
... def func2(x):
...     return x**3
...
>>> e2 = Ensemble('e2')
>>> e2.all(x=3)
{'func1': 9, 'func2': 27}
```

You may even attach a model function to multiple ensembles!

```
>>> @model('e2', 'e3')
... def func3(x, y):
...     return x**3 + y
...
>>> e2 = Ensemble('e2')
>>> e2.all(x=2, y=3)
{'func1': 4, 'func2': 8, 'func3': 11}
>>>
>>> e3 = Ensemble('e3')
>>> e3.all(x=2, y=3)
{'func3': 11}
```
