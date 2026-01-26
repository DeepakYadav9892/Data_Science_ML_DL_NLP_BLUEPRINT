from functools import wraps


""""
Logger Decorator  Structure

def logger(func):
    def wrapper(*args, **kwargs):
        # log before
        result = func(*args, **kwargs)
        # log after
        return result
    return wrapper



"""

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling:{func.__name__}")
        result=func(*args,**kwargs)
        print(f"Finished :{func.__name__}")
        return result
    return wrapper

@log_activity 
def brew_chai(type):
    print(f"Brewing {type}chai and milk status ")
brew_chai("Masala")