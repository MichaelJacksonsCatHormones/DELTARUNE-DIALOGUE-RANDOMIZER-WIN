import json
import random
import re

print("Randomizing dialog....")
filename = "lang_en_ch1_old.json"
# Read in the total number of lines
with open(filename) as f:
    c = json.load(f)
    #print(c[0])

# Get the "answers" to each key as a single array
# Shuffle the order of that array of "answers"
# Now edit the json -- create a new dict like the original
# Pair original key array to the new array of "answers"
# Profit
keys = list(c.keys())
vals = list(c.values())

random.shuffle(vals)

# Regular expressions
pat1 = r'\^(\d)'
pat2 = r'\\M.'

# Now apply postprocessing to ensure we r good
for index, v in enumerate(vals):
    og = list(c.values())[index]
    matches = re.findall(pat1, og)
    for match in matches:
        v += " ^" + match + " "

    if og[-2:] == "/%" and v[-2:] != "/%":
        v += "/%"
    
    matches = re.findall(pat2, og)
    for match in matches:
        v = match + v
    if "%%" in og and "%" not in v:
        v += " %%"
    elif " %" in og  and "%" not in v:
        v += " %"
    #print(v)
    vals[index] = v
        


out = dict(zip(keys, vals))

with open("lang_en_ch1.json", "w") as outF:
    json.dump(out, outF)
print("Finished.")



#TODO
'''
Now that basic stuff is working, we need to try and edit everything to make sure it is advanceabl
'''
