with open("SQL.txt",'r') as file:
    import json
    jso=file.read()
    po = json.loads(jso)
    print(po)
    file.seek(0)
    po = json.load(file)
    print(po)