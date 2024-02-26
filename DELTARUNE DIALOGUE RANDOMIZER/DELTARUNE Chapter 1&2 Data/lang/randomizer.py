import json
import random
import re
import time 

def insert(string, substring):
    if len(string) <= 4:
        string = string + substring
        return string
    random_index = random.randint(0, len(string)-2)
    string = string[:random_index] + substring + string[random_index:]
    return string

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
pat1 = r'\^(\d)+'
pat2 = r'\\[a-zA-Z].'

# Now apply postprocessing to ensure we r good
for index, v in enumerate(vals):
    # Remove things
    #v = re.sub(pat1, "", v);
    v = re.sub(pat2, "", v);
    #v = v.replace("\\", "");
    v = v.replace("%", "");
    v = v.replace("/", "")
    
    og = list(c.values())[index]
    matches = re.findall(pat1, og)
    #for match in matches:
    #    #print(match)
    #    v += " ^1 "

    if  "/%" in og and '/%' not in v:
        v += "/%"
    
    matches = re.findall(pat2, og)
    for match in matches:
        v = " " + match + " " + v
    if "%%" in og and "%" not in v:
        v += " %%"
    elif " %" in og  and "%" not in v:
        v += " %"
    #print(v)
    if "//" in og and "//" not in v:
        v = "//" + v
    if "\\" in og and "\\" not in v:
        v += "\\"
    #v = v[0:len(v)-3] + og[-3:]
    matches = re.findall(pat1, v)
    for match in matches:
        v = v.replace("^"+match, "^1")
        if len(v) > len(og):
            v = v[0:len(og)]
    vals[index] = v + "/%"
    #print("old: " + og)
    #print("new: " + v)
    #time.sleep(1)
    
        


out = dict(zip(keys, vals))

with open("lang_en_ch1.json", "w") as outF:
    json.dump(out, outF)
print("Finished.")



#TODO
'''
Now that basic stuff is working, we need to try and edit everything to make sure it is advanceabl
'''
