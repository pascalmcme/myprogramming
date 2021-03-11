

#def tripler (num):
#    return num*3
#def doubler (num):
#    return num*2


isMax = True
if isMax:
    fun = lambda num : num*2  # anonymous function - does not have a name (takes num : operation)
else:
    fun = lambda num : num*3

var = fun(10)
print(var)


#sorted

list = [22,23,11,15,9,100]
data = [

{"first":"Alan" , "last":"Franks"},
{"first":"Mark" , "last":"Grimes"},
{"first":"Tom" , "last":"Smith"},


]

newlist = sorted(list)
print(list)
print(newlist)

def sortFun(item):
 return item["first"]

newData = sorted(data, key = sortFun)
for item in newData:
    print(item)