with open("SQL.txt","a") as file:
    import json
    po={'intro':['hai','python'],'name':"harshad sir",'age':30,'male':True,'gender':False,'gf':None}
    jso=json.dumps(po)
    print(jso)
    file.write(jso)
    json.dump(po,file)