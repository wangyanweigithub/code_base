1. 使用contextmanager的装饰器,函数需要定义一个yield.
如果需要使用with的as关键字,yield需要一个参数.

2. contextmanager返回一个helper函数,helper函数返回一个_GeneratorContextManager.
这个类实现了with的`__enter_`和`__exit_`_魔法方法.

3. _GeneratorContextManager定义的__call__方法,不知道用在什么场景.通过这个也可以利用到with.
但使用方法并没有使用装饰器直接.
