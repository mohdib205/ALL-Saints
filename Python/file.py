import json


# load 
# dump


# d1={"branch":"cs"}

# with open("data1.json" , "r") as f:
#     data= json.load(f)
# print(data)
# data["branch"]="cs"
# with open("data1.json" , "w") as f:
#     json.dump(data , f)

dict1={'fn':'dsffd' , 'ln':'sdsd' , 'contact':111111 , 'salary':232211}

with open("customs.json" , "r") as fp:
    l1=json.load(fp)
    l1["employee"].append(dict1)

with open("customs.json" , "w") as fp:
    json.dump(l1 , fp)

with open("customs.json" , "r") as fp:
    data=json.load(fp)
    print(data)

# d1={"name":"djdk"}
# for d, i in data.items():
#     for k in i:
#         print(k)
#         if k['username']==us and k['password']==ps:
#             k["is_loggedin"]=True
#             print(d)

# def logout(us):


