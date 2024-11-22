from functools import wraps
from typing import Callable, TypeVar, Type, Union
from requests import Response
from requests.exceptions import RequestException

def as_raw(fn: Callable[..., Response]) -> Callable[..., Union[str, RequestException]]:
    @wraps(fn)
    def wrapped(*args, **kwargs) -> str | RequestException:
        try:
            response:Response = fn(*args, **kwargs)
            response.raise_for_status()
            return response.text
        except RequestException as e:
            raise e
    return wrapped

def as_dict(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs) -> dict | RequestException:
        try:
            response:requests.Response = fn(*args, **kwargs)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            raise e
    return wrapped

T = TypeVar('T')
def as_type(return_type: Type[T]):
    def decorator(fn: Callable[..., Response]) -> Callable[..., T | RequestException]:
        @wraps(fn)
        def wrapped(*args, **kwargs) -> T | RequestException:
            try: 
                response = fn(*args, **kwargs)
                response.raise_for_status()
                return return_type(**response.json())
            except RequestException as e:
                    raise e
        return wrapped
    return decorator
