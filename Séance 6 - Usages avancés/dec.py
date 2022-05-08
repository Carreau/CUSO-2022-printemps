from functools import wraps

from datetime import datetime

def time_me(f):

    @wraps(f)
    def _inner(*args, **kwargs):
        now = datetime.now()
        print(f.__name__ ,'called on', now.isoformat())
        f(*args, **kwargs)
        then = datetime.now()
        print(f.__name__ ,'done on', then.isoformat(), 'after', then-now, 'sec')
    return _inner



