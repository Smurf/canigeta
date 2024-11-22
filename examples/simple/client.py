from dataclasses import dataclass
import requests
from canigeta import response

@dataclass
class HelloData:
    message: str

@response.as_type(HelloData)
def get_hello() :
    return requests.get(url = "http://127.0.0.1:5000")

@response.as_dict
def get_hello_dict() :
    return requests.get(url = "http://127.0.0.1:5000")

@response.as_raw
def get_hello_raw():
    return requests.get(url = "http://127.0.0.1:5000")

def main():
    print(get_hello())
    print(get_hello_dict())
    print(get_hello_raw())

if __name__ == '__main__':
    main()
