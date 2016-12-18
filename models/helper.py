from __future__ import unicode_literals

from functools import wraps


def non_strict(checker_func):
    @wraps(checker_func)
    def nfunc(*args, **kwargs):
        try:
            return checker_func(*args, **kwargs)
        except AssertionError:
            return False
        return True
    return nfunc


def precon(con, error_msg='precondition not met'):
    def deco(func):
        @wraps(func)
        def nfunc(*args, **kwargs):
            assert con(*args, **kwargs), error_msg
            return func(*args, **kwargs)
        return nfunc
    return deco

