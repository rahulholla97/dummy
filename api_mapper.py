def hi_earth():
    import requests
    import json
    response_API = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    data=(response_API.text)
    parse_json = json.loads(data)
    print(parse_json)
hi_earth()