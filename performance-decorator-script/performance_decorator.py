from time import time

'''Performance Decorator
 Simple decorator created to measure the time taken by different functions
'''

def performance_monitor(fn):
	
	def wrapped_func(*args, **kwargs):
		t1 = time()
		result = fn()
		t2 = time()
		print(f'took {t2-t1} secs for the function \'{fn.__name__}\' to run')
		return result
	return wrapped_func

@performance_monitor
def random_func():
	for i in range(0,100000):
		print(i*5)

random_func()

