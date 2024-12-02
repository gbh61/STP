import re

string = "The ghost that says boo hunts the loo."

matches = re.findall(".oo", string, re.IGNORECASE)

print(matches)
