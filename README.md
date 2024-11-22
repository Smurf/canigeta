# Can I Get A (canigeta)

`canigeta` makes getting typed REST responses via the requests library easy.

## Example

```
# Simple example of a typed return from a REST endpoint 
# This endpoint returns {'message': 'Hello, World!'} JSON.
from dataclasses import dataclass
import requests
from canigeta import response

@dataclass
class HelloData:
    message: str

@response.as_type(HelloData)
def get_hello() :
    return requests.get(url = "http://127.0.0.1:5000")

# HelloData(message='Hello, World!')
```
