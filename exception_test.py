#捕获单个异常
try:
    i=j
except NameError as e:
    print(e)
#捕获多个异常
try:
    i=j
except (NameError,ValueError) as e:
    print(e)

