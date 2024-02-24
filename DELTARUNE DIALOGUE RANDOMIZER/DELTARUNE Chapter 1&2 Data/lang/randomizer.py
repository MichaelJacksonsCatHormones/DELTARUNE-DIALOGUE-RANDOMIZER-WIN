import json
import random

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
out = dict(zip(keys, vals))

with open("lang_en_ch1.json", "w") as outF:
    json.dump(out, outF)
print("Finished.")
