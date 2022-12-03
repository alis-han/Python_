mydict={"name":"Alishan","age":20,"percantage":80}
print(mydict)
mydict["roll no."]=6
# ordered,mutable,no duplicate values
print(mydict["age"])
percant=mydict.get("percantage")
print(percant)
print(mydict.keys())
print(mydict.values())
print(mydict.items())
print(mydict.pop("name"))
print(mydict.popitem())
# Merge Two dictionary in one__...
dict1={"one":1,"two":2,"three":3}
dict2={"four":4,"five":5,"six":6}
dict1.update(dict2)
print(dict1)

# Nested_Dictionary
dict = {
    "class":{
        "student":{
            "name":"xyz",
            "marks":{
                "python":100,
                "web":90
            }
        }
    }
}
print(dict["class"]["student"]["marks"]["web"])