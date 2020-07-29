# decorator definition
def timer(func):
	from time import time

	def wrapper(*args,**kwargs):
		start = time()
		func_output = func(*args,**kwargs)
		total = time() - start
		print('function {} took {} s'.format(func.__name__, round(total,2)))

		return func_output

	return wrapper




@timer
def loop(n):
	for i in range(n):
		pass

	return 'done'


print(loop(10000001))

