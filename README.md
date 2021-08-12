# badif
for when you hate if statements


example
```python

from badif import If

x = 4

@If(x > 5)
def _():
    print('bigger than 5')

    @If(x > 10)
    def __():
        print('bigger than 10')

    @__.Elif(x < 10)
    def __():
        print('smaller than 10')


@_.Elif(x < 5)
def _():
    print('smaller than 5')


@_.Else
def _():
    print('equals 5')
```



