async def divide(x, y):
    return x / y


async def bad_call():
    a = await divide(1, 1)
    print("a is:", a)


a = bad_call()
try:
    a.send(None)
except Exception as e:
    print("error is: ", e)
