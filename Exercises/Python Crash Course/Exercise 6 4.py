myDict={}
myDict = {
'set':'Like a dict, but no dups',
'list':'Like a tuple, but mutable',
'dict':'Key and Value pairs',
'sort':'Sort in alpa order',
'string':'Use for text'
}
#for theItems in myDict.items():
#    print(theItems)
#This version looks better.
for k, v in myDict.items():
    print(k + ': ' + v)
